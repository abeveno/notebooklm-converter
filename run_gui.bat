@echo off
echo Starting NotebookLM Converter GUI...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found. Please install Python first.
    pause
    exit /b 1
)

REM Check if tkinter is available
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo Error: tkinter not available. Please install Python with tkinter support.
    pause
    exit /b 1
)

echo Python and tkinter found. Starting GUI...
echo.

REM Change to script directory
cd /d "%~dp0"

REM Run the application
python -c "
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print('Loading NotebookLM Converter...')
try:
    from notebooklm_converter.app import main
    main()
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
    input('Press Enter to exit...')
"

if errorlevel 1 (
    echo.
    echo Application exited with error.
    pause
)
