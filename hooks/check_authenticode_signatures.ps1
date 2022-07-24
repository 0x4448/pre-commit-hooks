param(
    [string]$Files
)

foreach ($File in $Files) {
    if ($null -ne (Select-String -Pattern '# SIG # Begin signature block' -Path $File)) {
        exit 1
    }
}
