#!/usr/bin/env powershell

param(
    [string]$Files
)

$ExitCode = 0

foreach ($File in $Files) {
    if ($null -ne (Select-String -Pattern '^# SIG # Begin signature block' -Path $File)) {
        Write-Host "$File contains an Authenticode signature."
        $ExitCode = 1
    }
}

exit $ExitCode
