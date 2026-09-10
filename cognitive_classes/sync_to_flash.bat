@echo off
chcp 65001 >nul
set SOURCE=C:\ai_models\cognitive_classes
set DEST=D:\COGNETIVE_CLASSES
set LOG=%SOURCE%\sync_log.txt

echo [%date% %time%] Checking flash drive D:... >> "%LOG%"

if not exist D:\ (
    echo [ERROR] Flash drive D: not found! Connect the drive and retry.
    echo [%date% %time%] ERROR: D: not available >> "%LOG%"
    pause
    exit /b 1
)

echo [%date% %time%] Starting sync %SOURCE% -> %DEST% >> "%LOG%"

robocopy "%SOURCE%" "%DEST%" /MIR /Z /R:3 /W:5 /XD .git node_modules __pycache__ .venv venv /XF *.tmp *.log ~$* /MT:8 /NP /NDL /NFL

if %ERRORLEVEL% LEQ 7 (
    echo [SUCCESS] Sync complete. Files copied to flash drive.
    echo [%date% %time%] SUCCESS: robocopy finished (code %ERRORLEVEL%) >> "%LOG%"
) else (
    echo [WARNING] Robocopy exited with code %ERRORLEVEL%. Check the log.
    echo [%date% %time%] WARNING: robocopy code %ERRORLEVEL% >> "%LOG%"
)

echo.
pause
