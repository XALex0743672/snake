import PyInstaller.__main__
import os
import sys

def build_executable():
    """
    Build the executable using PyInstaller
    """
    print("Starting Snake Game build process...")
    
    # Define PyInstaller options
    options = [
        'snake_game.py',                  # Script to bundle
        '--name=SnakeGame',               # Name of the output exe
        '--onefile',                      # Create a single executable file
        '--windowed',                     # Do not show console window
        '--icon=snake_icon.png',          # Use our custom icon
        '--clean',                        # Clean PyInstaller cache
        '--add-data', 'snake_game.py:.',  # Include the main script
        '--noupx',                        # Do not use UPX for compression
    ]
    
    # Run PyInstaller with our options
    try:
        PyInstaller.__main__.run(options)
        print("\nBuild completed successfully!")
        print("\nYou can find the executable in the 'dist' folder.")
    except Exception as e:
        print(f"\nError building executable: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = build_executable()
    sys.exit(0 if success else 1)
