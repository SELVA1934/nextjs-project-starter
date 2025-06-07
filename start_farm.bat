@echo off
title Discord Account Farm Tool
color 0a

:check_python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

:check_script
if not exist discord_farm.py (
    echo discord_farm.py not found
    echo Please ensure the script is in the same directory
    pause
    exit /b 1
)

:run_script
cls
echo Starting Discord Account Farm Tool...
echo.
python discord_farm.py

pause
exit /b 0
