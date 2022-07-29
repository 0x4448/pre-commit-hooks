#!/usr/bin/env python3

import logging
import re

from . import util

log = logging.getLogger(__name__)


def find_signature(path):
    pattern = re.compile("^# SIG # Begin signature block")
    matches = util.find_matching_lines(path, pattern)
    if matches:
        for match in matches:
            log.error(f"{path}:{match.line_number}: {match.match}")
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
