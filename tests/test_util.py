#!/usr/bin/env python3

from pathlib import Path

from hooks import util


def test_get_input_files_one_arg():
    rv = util.get_input_files(["foo.txt"])
    assert rv == [Path("foo.txt")]


def test_get_input_files_multiple_args():
    rv = util.get_input_files(["foo.txt", "bar.txt"])
    assert rv == [Path("foo.txt"), Path("bar.txt")]
