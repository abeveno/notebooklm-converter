@echo off
title Installing NotebookLM Converter Dependencies
echo Installing required Python packages for NotebookLM Converter...
echo.
"C:/Users/abeve/AppData/Local/Programs/Python/Python313/python.exe" -m pip install -r requirements.txt
echo.
echo Installation completed!
echo.
echo Note: For MOBI/AZW/KFX formats, please install Calibre from:
echo https://calibre-ebook.com/download
echo.
echo For KFX format, you also need the KFX Input Plugin for Calibre.
echo.
pause
