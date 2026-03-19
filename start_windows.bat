@echo off
title MindVault — Personal Knowledge AI
echo.
echo  =============================================
echo    MindVault — Personal Knowledge Base AI
echo    by Aarnav Kejriwal ^<aarnkej@gmail.com^>
echo  =============================================
echo.

:: Check if .env exists and load key from it
if exist .env (
    for /f "tokens=1,2 delims==" %%a in (.env) do (
        if "%%a"=="ANTHROPIC_API_KEY" set ANTHROPIC_API_KEY=%%b
    )
)

:: Prompt if still not set
if "%ANTHROPIC_API_KEY%"=="" (
    echo  [!] ANTHROPIC_API_KEY is not set.
    echo      Get your key at: https://console.anthropic.com
    echo.
    set /p ANTHROPIC_API_KEY="  Paste your key (sk-ant-...): "
    echo.
)

echo  [*] Installing / verifying dependencies...
pip install -r requirements.txt -q
echo  [*] Dependencies OK.
echo.
echo  [*] Starting MindVault server...
echo.
echo  -----------------------------------------------
echo   Open in your browser: http://localhost:5000
echo  -----------------------------------------------
echo.
python app.py
pause
