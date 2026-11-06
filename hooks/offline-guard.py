#!/usr/bin/env python3
"""offline-guard: while the workspace is offline, refuse web tools and shell downloads.

Event: PreToolUse, actions `web` (Claude Code's WebSearch and WebFetch) and `shell`.
Acts only when project.toml has `[web] offline = true`, which `bin/offline on` sets; it does
nothing otherwise. Offline mode exists so that nothing about the work (a colleague's
unpublished draft, a confidential problem) leaves the computer in a search query or a
download. HARD BLOCK, every time:
  - a web search or fetch (on Codex, `web_search = "disabled"` in .codex/config.toml turns
    the tool off instead, since its web search does not reach hooks);
  - a shell command that runs a download client: curl, wget, httpie (http, https), aria2c,
    lynx, w3m.
git is not blocked: pushing to the owner's own private remote is the owner's call.
Lift: `bin/offline off` (the owner's). See docs/OWNER.md, "Web access".
"""
import re
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _payload  # noqa: E402
import guard  # noqa: E402  (its shell parser: pipes, $(...), sh -c, heredocs)

HOOK = "offline-guard"
CLIENTS = {"curl", "wget", "http", "https", "aria2c", "lynx", "w3m"}
WRAPPERS = {"env", "command", "exec", "nice", "nohup", "time", "sudo", "doas", "xargs", "timeout", "stdbuf"}
ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")


def downloads(cmd: str) -> str | None:
    """The download client run in command position anywhere in `cmd`, if any."""
    for words, _t in guard.parse(cmd):
        i = 0
        while i < len(words):
            w = words[i]
            b = guard._basename(w)
            if ASSIGN.match(w) or (i and w.startswith("-")) or (i and b.replace(".", "").isdigit()):
                i += 1
                continue
            if b in CLIENTS:
                return b
            if b in WRAPPERS:
                i += 1
                continue
            break
    return None


def offline(root: str) -> bool:
    try:
        with open(Path(root) / "project.toml", "rb") as f:
            return bool(tomllib.load(f).get("web", {}).get("offline", False))
    except (OSError, tomllib.TOMLDecodeError):
        return False


def main(ev):
    if ev.action not in ("web", "shell") or not offline(ev.root):
        return
    if ev.action == "web":
        _payload.block("offline-guard: this workspace is offline ([web] offline = true in "
                       "project.toml), so no web search or fetch. Work from what is in the "
                       "workspace; mark a citation you could not check as 'not verified "
                       "(offline)'. Only the owner turns this off (bin/offline off).")
    if downloads(guard.raw_command(ev)):
        _payload.block("offline-guard: this workspace is offline, so no downloads from the "
                       "shell. If the owner has the file, ask them for it (bin/doc new ... "
                       "--file <path>). Only the owner turns this off (bin/offline off).")


if __name__ == "__main__":
    _payload.run(main, HOOK)
