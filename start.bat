@echo off
title EV - ENHANCED VIRTUAL INTELLIGENCE
color 0B
cls
echo ========================================================
echo   EV - ENHANCED VIRTUAL INTELLIGENCE (J.A.R.V.I.S.)
echo   Autonomous Personal Desktop AI Assistant
echo ========================================================
echo.
echo [1/3] Checking Python runtime...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your system PATH.
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b
)

echo [2/3] Verifying core modules...
python -c "import PySide6, psutil, pyttsx3, speech_recognition" >nul 2>&1
if %errorlevel% neq 0 (
    echo [NOTICE] Installing missing dependencies from requirements.txt...
    python -m pip install -r requirements.txt
)

echo [3/3] Booting EV Desktop Workstation...
echo.
python main.py
if %errorlevel% neq 0 (
    echo.
    echo [NOTICE] EV session ended with code %errorlevel%.
    pause
)

