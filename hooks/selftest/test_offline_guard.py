"""Selftest for hooks/offline-guard.py, through its real entry point."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / "offline-guard.py"


def run(root, tool, tool_input, harness="claude"):
    env = {k: v for k, v in os.environ.items() if k != "HOOKS_QUIET"}
    env["CLAUDE_PROJECT_DIR"] = root
    payload = {"hook_event_name": "PreToolUse", "tool_name": tool, "cwd": root, "tool_input": tool_input}
    return subprocess.run([sys.executable, str(HOOK), "--harness", harness], input=json.dumps(payload),
                          capture_output=True, text=True, env=env, timeout=30)


class OfflineGuard(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def set_offline(self, on):
        Path(self.root, "project.toml").write_text(f"[web]\noffline = {'true' if on else 'false'}\n")

    def test_online_allows_everything(self):
        self.set_offline(False)
        self.assertEqual(run(self.root, "WebSearch", {"query": "x"}).returncode, 0)
        self.assertEqual(run(self.root, "Bash", {"command": "curl -O https://arxiv.org/x"}).returncode, 0)

    def test_no_setting_allows(self):
        self.assertEqual(run(self.root, "WebFetch", {"url": "https://x"}).returncode, 0)

    def test_offline_blocks_web_tools(self):
        self.set_offline(True)
        for tool in ("WebSearch", "WebFetch"):
            r = run(self.root, tool, {"query": "x", "url": "https://x"})
            self.assertEqual(r.returncode, 2, tool)
            self.assertIn("offline", r.stderr)

    def test_offline_blocks_downloads_not_other_shell(self):
        self.set_offline(True)
        for cmd in ("curl -sL https://x -o a", "cd x && wget https://y", "/usr/bin/curl x",
                    "echo $(curl x)", "http GET example.org"):
            self.assertEqual(run(self.root, "Bash", {"command": cmd}).returncode, 2, cmd)
        for cmd in ("git push origin main", "ls source/", "grep -r curl docs", "bin/checks verify",
                    "python3 -c 'print(1)'"):
            self.assertEqual(run(self.root, "Bash", {"command": cmd}).returncode, 0, cmd)

    def test_codex_shell(self):
        self.set_offline(True)
        r = run(self.root, "shell", {"command": ["bash", "-lc", "curl https://x"]}, harness="codex")
        self.assertEqual(r.returncode, 2)


if __name__ == "__main__":
    unittest.main()
