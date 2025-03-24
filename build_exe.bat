@echo off
echo Starting build process for Snake Game...
echo Installing required packages...
pip install --quiet pygame
pip install --quiet pyinstaller

echo.
echo Building executable...
python build_exe.py

echo.
if exist "dist\SnakeGame.exe" (
    echo Build completed successfully!
    echo The executable is located at: dist\SnakeGame.exe
) else (
    echo Build failed. Check the error messages above.
)

echo.
echo Press any key to exit...
pause > nul
