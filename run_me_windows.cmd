@echo off
:: Check if Python is installed
python --version >nul 2>&1
IF NOT ERRORLEVEL 0 (
    echo Python is not installed or not added to PATH.
    pause
    exit /b
)

:: Run the Python script
python CareersLauncher.py
pause
