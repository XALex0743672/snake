# Snake Game - Executable Builder

This project converts a Python Snake game to a standalone Windows executable (.exe) file.

## Contents

- `snake_game.py` - The main Python game script
- `build_exe.py` - Python script to build the executable using PyInstaller
- `build_exe.bat` - Batch file to automate the build process
- `README.md` - This file

## Requirements

Before building the executable, you need:

1. Python 3.6 or higher installed
2. pip (Python package installer)

## How to Build the Executable

### Easy Method (Windows)

1. Simply double-click the `build_exe.bat` file
2. Wait for the process to complete
3. Find the executable in the `dist` folder (SnakeGame.exe)

### Manual Method

If the batch file doesn't work, you can build manually:

1. Open a command prompt
2. Install the required packages:
   ```
   pip install pygame pyinstaller
   ```
3. Run the build script:
   ```
   python build_exe.py
   ```
4. Find the executable in the `dist` folder

## Game Instructions

- Use arrow keys to control the snake
- Collect green food to grow and gain points
- Avoid the flashing red/blue bombs
- Yellow bonus items appear periodically for extra points
- Choose a difficulty level at the start of each game

## Troubleshooting

If you encounter issues:

1. Make sure Python is installed and in your PATH
2. Try running the original Python script to verify it works:
   ```
   python snake_game.py
   ```
3. Check that you have Administrator privileges
4. Make sure you have internet access to download the required packages

## Playing Without Building

If you just want to play the game without building an executable:

1. Install Python and pygame:
   ```
   pip install pygame
   ```
2. Run the script:
   ```
   python snake_game.py
   ```
