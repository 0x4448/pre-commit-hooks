#!/usr/bin/env python3

import pytest

PWSH_WITH_SIG = """
#!/usr/bin/env pwsh
Write-Host "Hello world!"
# SIG # Begin signature block
...
# SIG # End signature block
"""

PWSH_WITHOUT_SIG = """
#!/usr/bin/env pwsh
Write-Host "Hello world!"
"""


@pytest.fixture
def mock_pwsh_with_sig(mocker):
    data = mocker.mock_open(read_data=PWSH_WITH_SIG)
    mocker.patch("builtins.open", data)


@pytest.fixture
def mock_pwsh_without_sig(mocker):
    data = mocker.mock_open(read_data=PWSH_WITHOUT_SIG)
    mocker.patch("builtins.open", data)
