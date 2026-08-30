@echo off
chcp 65001 >nul
set SOURCE=C:\ai_models\cognitive_classes
set DEST=D:\COGNETIVE_CLASSES
set LOG=%SOURCE%\sync_log.txt

echo [%date% %time%] Проверка флешки D:... >> "%LOG%"

if not exist D:\ (
    echo [ОШИБКА] Флешка D: не найдена! Подключите флешку и повторите.
    echo [%date% %time%] ОШИБКА: D: не доступен >> "%LOG%"
    pause
    exit /b 1
)

echo [%date% %time%] Начало синхронизации %SOURCE% -> %DEST% >> "%LOG%"

robocopy "%SOURCE%" "%DEST%" /MIR /Z /R:3 /W:5 /XD .git node_modules __pycache__ .venv venv /XF *.tmp *.log ~$* /MT:8 /NP /NDL /NFL

if %ERRORLEVEL% LEQ 7 (
    echo [УСПЕХ] Синхронизация завершена. Файлы скопированы на флешку.
    echo [%date% %time%] УСПЕХ: robocopy завершен (code %ERRORLEVEL%) >> "%LOG%"
) else (
    echo [ПРЕДУПРЕЖДЕНИЕ] Robocopy завершился с кодом %ERRORLEVEL%. Проверьте лог.
    echo [%date% %time%] WARNING: robocopy code %ERRORLEVEL% >> "%LOG%"
)

echo.
pause
