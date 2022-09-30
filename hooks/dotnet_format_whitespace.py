#!/usr/bin/env python3

import logging
import os
import subprocess

from . import util  #noqa: F401


log = logging.getLogger(__name__)


def check_dotnet() -> bool:
    try:
        subprocess.check_call(["dotnet", "format", "--version"])
        return True
    except FileNotFoundError:
        message = "dotnet command not found"
        if os.environ.get("GITHUB_ACTION"):
            print(f"::warning {message}")
        else:
            log.warning(message)
        return False


def dotnet_format_whitespace() -> bool:
    rv = True
    try:
        command = [
            # fmt: off
            "dotnet", "format", "whitespace",
            "--folder", "Assets",
            "--verify-no-changes",
            # fmt: on
        ]
        subprocess.check_output(command, text=True)

    except subprocess.CalledProcessError:
        rv = False

    return rv


def main() -> int:
    rv = 0

    if check_dotnet():
        if not dotnet_format_whitespace():
            rv = 1

    return rv


if __name__ == "__main__":
    raise SystemExit(main())
