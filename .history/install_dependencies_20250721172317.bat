@echo off
title Installing EPUB Converter Dependencies
echo Installing required Python packages...
echo.
"C:/Users/abeve/AppData/Local/Programs/Python/Python313/python.exe" -m pip install -r requirements.txt
echo.
echo Installation completed!
echo.
echo Note: If you want to convert to MOBI/AZW3 format, please install Calibre from:
echo https://calibre-ebook.com/download
echo.
pause
