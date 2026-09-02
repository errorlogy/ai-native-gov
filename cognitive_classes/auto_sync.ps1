# Auto-sync script for Cognitive Classes -> Flash D: + Yandex.Disk
# Monitors C:\ai_models\cognitive_classes and copies changes to all available destinations

$source = "C:\ai_models\cognitive_classes"
$flash  = "D:\COGNETIVE_CLASSES"
$yandex = Join-Path $env:USERPROFILE "Yandex.Disk\AI_PROJECTS\COGNITIVE_CLASSES"
$log    = "$source\auto_sync_log.txt"

function Write-Log($msg) {
    $line = "[{0:yyyy-MM-dd HH:mm:ss}] {1}" -f (Get-Date), $msg
    Add-Content -Path $log -Value $line -Encoding UTF8
    Write-Host $line
}

function Sync-Destination($dest, $mode) {
    if (-not (Test-Path $dest)) {
        Write-Log "SKIP: $dest not available"
        return
    }
    Write-Log "SYNC $mode -> $dest"
    try {
        $argsList = @(
            '"' + $source + '"',
            '"' + $dest + '"'
        )
        if ($mode -eq "MIRROR") {
            $argsList += @('/MIR','/Z','/R:3','/W:5')
        } else {
            $argsList += @('/E','/Z','/R:3','/W:5','/XC','/XN','/XO')
        }
        $argsList += @(
            '/XD','.git','node_modules','__pycache__','.venv','venv',
            '/XF','*.tmp','*.log','~$*',
            '/MT:8','/NP','/NDL','/NFL'
        )
        $proc = Start-Process -FilePath "robocopy" -ArgumentList $argsList -Wait -PassThru -NoNewWindow
        Write-Log "SYNC done $mode (robocopy exit: $($proc.ExitCode))"
    } catch {
        Write-Log "SYNC ERROR $mode : $_"
    }
}

function Sync-All {
    Sync-Destination $flash  "MIRROR"
    Sync-Destination $yandex "ARCHIVE"
}

# Initial sync on startup
Write-Log "=== Auto-sync watcher started (Flash + Yandex) ==="
Sync-All

# FileSystemWatcher setup
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $source
$watcher.IncludeSubdirectories = $false
$watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor [System.IO.NotifyFilters]::FileName -bor [System.IO.NotifyFilters]::DirectoryName

$syncPending = $false
$timer = New-Object System.Timers.Timer
$timer.Interval = 8000  # 8 seconds debounce (give Yandex time to settle)
$timer.AutoReset = $false
Register-ObjectEvent -InputObject $timer -EventName Elapsed -Action {
    $global:syncPending = $false
    Sync-All
} | Out-Null

$action = {
    $global:syncPending = $true
    $timer.Stop()
    $timer.Start()
}

Register-ObjectEvent -InputObject $watcher -EventName Changed -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName Created -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventEvent Renamed -Action $action | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName Deleted -Action $action | Out-Null

$watcher.EnableRaisingEvents = $true

Write-Log "Watcher active. Press Ctrl+C to stop."

while ($true) {
    Start-Sleep -Seconds 1
}
