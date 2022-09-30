#!/usr/bin/env python3

import logging
import subprocess

from pathlib import Path

from . import util


log = logging.getLogger(__name__)
util.configure_logging()


def check_dotnet() -> bool:
    try:
        subprocess.check_call(["dotnet", "format", "--version"])
        return True
    except FileNotFoundError:
        log.warning("dotnet command not found")
        return False


def get_solution() -> str:
    solution = list(Path(".").glob("*.sln"))

    if len(solution) == 1:
        return str(solution[0])
    elif len(solution) > 1:
        log.warning("Multiple solutions found")

    return ""


def dotnet_format() -> bool:
    rv = True
    solution = get_solution()
    files = [str(f) for f in util.get_input_files()]

    try:
        command = [
            # fmt: off
            "dotnet", "format", solution,
            "--verify-no-changes",
            "--severity", "warn",
            "--include", *files,
            # fmt: on
        ]
        print(command)
        subprocess.check_output(command, text=True)

    except subprocess.CalledProcessError:
        rv = False

    return rv


def main() -> int:
    rv = 0

    if check_dotnet():
        if not dotnet_format():
            rv = 1

    return rv


if __name__ == "__main__":
    raise SystemExit(main())
