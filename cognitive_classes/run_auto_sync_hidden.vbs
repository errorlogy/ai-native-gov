' Hidden launcher for auto_sync.ps1
' Double-click to start background file watcher without PowerShell window

Dim objShell
Set objShell = CreateObject("WScript.Shell")

Dim scriptPath
scriptPath = "C:\ai_models\cognitive_classes\auto_sync.ps1"

Dim cmd
cmd = "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File """ & scriptPath & """"

objShell.Run cmd, 0, False

Set objShell = Nothing
