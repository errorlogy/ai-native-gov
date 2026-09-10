# Cognitive Classes Auto-Sync Instructions

## Copy destinations

| Destination | Type | Mode | Path |
|-------------|------|------|------|
| **Flash drive** | Local media | Mirror (`/MIR`) | `D:\COGNETIVE_CLASSES` |
| **Yandex.Disk** | Cloud (desktop) | Archive (`/E /XC /XN /XO`) | `%USERPROFILE%\Yandex.Disk\AI_PROJECTS\COGNITIVE_CLASSES` |

**Mode difference:**
- **Mirror** — full identity: new files are copied, changed files updated, files deleted from source are removed from the flash drive.
- **Archive** — append/update only: nothing is deleted from the cloud (protection against accidental loss).

---

## Quick start

### Manual sync (before ejecting the flash drive)

Double-click: **`sync_all.bat`**

- If the flash drive is connected — it will be updated.
- If Yandex.Disk is running — the cloud folder will be updated.
- Writes a log to `sync_log.txt`.

### Background auto-sync

Double-click: **`run_auto_sync_hidden.vbs`**

- Watches for changes in `C:\ai_models\cognitive_classes`
- On file save/create/delete, waits 8 seconds and syncs **both** destinations (if available)
- Runs hidden (no PowerShell window)

**Stop:** Task Manager → find `powershell.exe` → End task.

### Windows startup

Press `Win+R`, enter:
```
shell:startup
```

Copy a shortcut to **`run_auto_sync_hidden.vbs`** there — the watcher will start on every login.

---

## Exclusions

Robocopy skips:
- `.git`, `node_modules`, `__pycache__`, `.venv`, `venv`
- `*.tmp`, `*.log`, `~$*` (temporary/lock files)

---

## Logs

- `sync_log.txt` — manual runs of `sync_all.bat`
- `auto_sync_log.txt` — background watcher

---

## Troubleshooting

| Symptom | Solution |
|---------|----------|
| Flash drive not copying | Check drive letter (should be `D:`) |
| Yandex.Disk not copying | Ensure `Yandex.Disk` folder is syncing (tray icon) |
| PowerShell policy errors | Run via `.vbs` — it bypasses policies (`-ExecutionPolicy Bypass`) |
| Files not deleted from flash | Normal: cloud uses archive mode without deletion |
