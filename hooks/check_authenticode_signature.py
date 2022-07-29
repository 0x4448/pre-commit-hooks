#!/usr/bin/env python3

import logging

from . import util

log = logging.getLogger(__name__)


def find_signature(path):
    with open(path) as fp:
        for line_num, line in enumerate(fp):
            if line.startswith("# SIG # Begin signature block"):
                log.error(f"{path}:{line_num}: signature found")
                return True
    return False


def main() -> int:
    rv = 0
    for path in util.get_input_files():
        if find_signature(path):
            rv = 1
    return rv


if __name__ == "__main__":
    raise SystemExit(main())
