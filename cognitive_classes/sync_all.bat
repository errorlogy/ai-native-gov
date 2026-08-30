@echo off
chcp 65001 >nul
set SOURCE=C:\ai_models\cognitive_classes
set LOG=%SOURCE%\sync_log.txt

echo [%date% %time%] ===== SYNC ALL STARTED ===== >> "%LOG%"

:: --- 1. FLASH D: (mirror) ---
echo [%date% %time%] [1/2] Flash D:... >> "%LOG%"
if exist D:\ (
    robocopy "%SOURCE%" "D:\COGNETIVE_CLASSES" /MIR /Z /R:3 /W:5 /XD .git node_modules __pycache__ .venv venv /XF *.tmp *.log ~$* /MT:8 /NP /NDL /NFL
    echo [%date% %time%] [1/2] Flash D: done (code %ERRORLEVEL%) >> "%LOG%"
    echo [OK] Флешка D: синхронизирована.
) else (
    echo [SKIP] Флешка D: не подключена.
    echo [%date% %time%] [1/2] Flash D: SKIP (not mounted) >> "%LOG%"
)

:: --- 2. YANDEX.DISK (append/update, no delete) ---
echo [%date% %time%] [2/2] Yandex.Disk... >> "%LOG%"
set YANDEST=C:\Users\lawye\Yandex.Disk\AI_PROJECTS\COGNITIVE_CLASSES
if exist "%YANDEST%\" (
    robocopy "%SOURCE%" "%YANDEST%" /E /Z /R:3 /W:5 /XC /XN /XO /XD .git node_modules __pycache__ .venv venv /XF *.tmp *.log ~$* /MT:8 /NP /NDL /NFL
    echo [%date% %time%] [2/2] Yandex.Disk done (code %ERRORLEVEL%) >> "%LOG%"
    echo [OK] Yandex.Disk архив обновлён.
) else (
    echo [SKIP] Папка Yandex.Disk\AI_PROJECTS не найдена.
    echo [%date% %time%] [2/2] Yandex.Disk SKIP (path missing) >> "%LOG%"
)

echo [%date% %time%] ===== SYNC ALL FINISHED ===== >> "%LOG%"
echo.
pause
