#!/usr/bin/env python3
from __future__ import annotations

import logging
import re

from typing import Sequence

from . import util

log = logging.getLogger(__name__)
util.configure_logging()


def find_signature(path):
    pattern = re.compile("^# SIG # Begin signature block")
    matches = util.find_matching_lines(path, pattern)
    if matches:
        for match in matches:
            log.error(f"{path}:{match.line_number}: {match.match}")
        return True
    return False


def main(argv: Sequence[str] | None = None) -> int:
    rv = 0
    for path in util.get_input_files(argv):
        if find_signature(path):
            rv = 1
    return rv


if __name__ == "__main__":
    raise SystemExit(main())
