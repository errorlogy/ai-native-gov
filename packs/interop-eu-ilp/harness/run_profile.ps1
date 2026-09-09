#Requires -Version 5.1
param(
    [string]$BaseUrl = "http://localhost:8000",
    [switch]$SkipPost
)

$ErrorActionPreference = "Stop"
$PackRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$RepoRoot = Resolve-Path (Join-Path $PackRoot "..\..")
$EventsDir = Join-Path $PackRoot "examples\events"
$ManifestPath = Join-Path $PackRoot "manifest.json"
$ValidateScript = Join-Path $RepoRoot "scripts\validate_ilp_json.py"

Write-Host "=== interop-eu-ilp harness ===" -ForegroundColor Cyan

$manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json
$required = @("pack_id", "pack_slug", "institution_layers", "schema_refs", "min_errorlogy_ref", "modeling_profile_id", "epistemic_label")
foreach ($field in $required) {
    if (-not ($manifest.PSObject.Properties.Name -contains $field)) {
        throw "manifest.json missing required field: $field"
    }
}
Write-Host "[OK] manifest.json ($($manifest.pack_id))" -ForegroundColor Green

$eventFiles = Get-ChildItem $EventsDir -Filter "*.json"
foreach ($file in $eventFiles) {
    $event = Get-Content $file.FullName -Raw | ConvertFrom-Json
    foreach ($req in @("story_id", "event_type", "activated_layers", "epistemic_label")) {
        if (-not ($event.PSObject.Properties.Name -contains $req)) {
            throw "$($file.Name) missing required field: $req"
        }
    }
    Write-Host "[OK] $($file.Name)" -ForegroundColor Green
}

python $ValidateScript events $EventsDir
if ($LASTEXITCODE -ne 0) { throw "JSON validation failed" }

if (-not $SkipPost) {
    try {
        $null = Invoke-RestMethod -Uri "$BaseUrl/health" -Method Get -TimeoutSec 3
        Write-Host "[OK] errorlogy-mas health" -ForegroundColor Green
        foreach ($file in $eventFiles) {
            $body = Get-Content $file.FullName -Raw
            $null = Invoke-RestMethod -Uri "$BaseUrl/api/events/cross-layer" -Method Post -Body $body -ContentType "application/json"
            Write-Host "[POST] $($file.Name)" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Host "[SKIP] errorlogy-mas not reachable at $BaseUrl (local validation only)" -ForegroundColor DarkYellow
    }
}

Write-Host "=== interop-eu-ilp harness complete ===" -ForegroundColor Cyan
