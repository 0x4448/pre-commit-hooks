#!/usr/bin/env python3

from pathlib import Path


def get_test_file(filename) -> str:
    path = Path(__file__).parent / "files" / filename
    return str(path)
