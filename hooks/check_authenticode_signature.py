#!/usr/bin/env python3

import argparse

from hooks.util import log


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", type=str, nargs="+")
    args = parser.parse_args()

    status = 0

    for path in args.paths:
        if find_signature(path):
            status = 1

    return status


def find_signature(path):
    with open(path) as fp:
        for line_num, line in enumerate(fp):
            if line.startswith("# SIG # Begin signature block"):
                log.error(f"{path}:{line_num}: signature found")
                return True
    return False


if __name__ == "__main__":
    SystemExit(main())
