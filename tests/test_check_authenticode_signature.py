#!/usr/bin/env python3

import pytest  # noqa: F401

from hooks.check_authenticode_signature import find_signature


def test_signature_found(mock_pwsh_with_sig):
    assert find_signature("path")


def test_signature_not_found(mock_pwsh_without_sig):
    assert not find_signature("path")
