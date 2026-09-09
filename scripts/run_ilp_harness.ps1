#Requires -Version 5.1
param(
    [string]$BaseUrl = "http://localhost:8000",
    [switch]$SkipPost
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$PacksDir = Join-Path $RepoRoot "packs"
$ValidateScript = Join-Path $RepoRoot "scripts\validate_ilp_json.py"

Write-Host "=== ILP harness runner ===" -ForegroundColor Cyan
Write-Host "Repo: $RepoRoot"

$packHarnesses = Get-ChildItem $PacksDir -Recurse -Filter "run_profile.ps1" |
    Where-Object { $_.FullName -notmatch '\\_harness\\' } |
    Sort-Object FullName

if ($packHarnesses.Count -eq 0) {
    throw "No pack harness scripts found under packs/"
}

$failures = @()
foreach ($harness in $packHarnesses) {
    $packName = Split-Path (Split-Path $harness.DirectoryName -Parent) -Leaf
    Write-Host "`n--- Running $packName ---" -ForegroundColor Cyan
    $harnessArgs = @("-File", $harness.FullName, "-BaseUrl", $BaseUrl)
    if ($SkipPost) { $harnessArgs += "-SkipPost" }
    & powershell @harnessArgs
    if ($LASTEXITCODE -ne 0) {
        $failures += $packName
    }
}

Write-Host "`n--- Modeling Base seeds ---" -ForegroundColor Cyan
python $ValidateScript seeds
if ($LASTEXITCODE -ne 0) { $failures += "modeling-base-seeds" }

if ($failures.Count -gt 0) {
    Write-Host "`nFAILED: $($failures -join ', ')" -ForegroundColor Red
    exit 1
}

Write-Host "`n=== All ILP harnesses passed ===" -ForegroundColor Green
