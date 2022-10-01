#!/usr/bin/env python3

import pytest

from hooks.authenticode import main
from testing.util import get_test_file


@pytest.mark.parametrize(
    ("filename", "expected_rv"),
    (
        ("pwsh_signed.ps1", 1),
        ("pwsh_unsigned.ps1", 0),
    ),
)
def test_main(filename, expected_rv):
    assert main([get_test_file(filename)]) == expected_rv
