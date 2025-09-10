#!/usr/bin/env python3
"""
Build script for creating Windows executable of the System Information Dashboard.
This script can be run locally to build the executable without GitHub Actions.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_requirements():
    """Check if all required packages are installed."""
    try:
        import streamlit
        import psutil
        import PyInstaller
        print("✅ All required packages are installed.")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def create_build_script():
    """Create the build script that will be packaged with PyInstaller."""
    build_script_content = '''import streamlit.web.cli as stcli
import sys
import os

def main():
    """Main entry point for the executable."""
    # Set Streamlit configuration for headless mode
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_PORT'] = '8501'
    os.environ['STREAMLIT_SERVER_ADDRESS'] = 'localhost'
    
    # Get the directory where the exe is located
    if getattr(sys, 'frozen', False):
        # Running as compiled exe
        app_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        app_dir = os.path.dirname(os.path.abspath(__file__))
    
    app_path = os.path.join(app_dir, 'app.py')
    
    # Check if app.py exists
    if not os.path.exists(app_path):
        print(f"Error: app.py not found at {app_path}")
        input("Press Enter to exit...")
        return
    
    # Run Streamlit
    sys.argv = ['streamlit', 'run', app_path]
    try:
        stcli.main()
    except KeyboardInterrupt:
        print("\\nApplication stopped by user.")
    except Exception as e:
        print(f"Error running application: {e}")
        input("Press Enter to exit...")

if __name__ == '__main__':
    main()
'''
    
    with open('build_script.py', 'w') as f:
        f.write(build_script_content)
    print("✅ Created build_script.py")

def build_executable():
    """Build the executable using PyInstaller."""
    print("🔨 Building executable with PyInstaller...")
    
    # PyInstaller command with comprehensive imports
    cmd = [
        'pyinstaller',
        '--onefile',                    # Create a single executable file
        '--windowed',                   # Don't show console window
        '--name', 'SystemInfoDashboard', # Name of the executable
        '--add-data', 'app.py;.',       # Include app.py in the bundle
        '--hidden-import', 'streamlit', # Ensure Streamlit is included
        '--hidden-import', 'streamlit.web',
        '--hidden-import', 'streamlit.web.cli',
        '--hidden-import', 'streamlit.runtime',
        '--hidden-import', 'streamlit.runtime.scriptrunner',
        '--hidden-import', 'streamlit.runtime.state',
        '--hidden-import', 'streamlit.components',
        '--hidden-import', 'streamlit.components.v1',
        '--hidden-import', 'altair',
        '--hidden-import', 'pandas',
        '--hidden-import', 'numpy',
        '--hidden-import', 'psutil',
        '--hidden-import', 'platform',
        '--hidden-import', 'datetime',
        '--hidden-import', 'time',
        '--collect-all', 'streamlit',   # Collect all Streamlit modules
        '--collect-all', 'altair',      # Collect all Altair modules
        '--collect-all', 'pandas',      # Collect all Pandas modules
        '--collect-all', 'numpy',       # Collect all NumPy modules
        '--collect-all', 'psutil',      # Collect all psutil modules
        'build_script.py'
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Executable built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building executable: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False

def create_distribution_files():
    """Create additional files for distribution."""
    dist_dir = Path('dist')
    
    # Create batch file to run the application
    batch_content = '''@echo off
title System Information Dashboard
echo.
echo ========================================
echo   System Information Dashboard
echo ========================================
echo.
echo Starting application...
echo Please wait while the application loads...
echo.
echo The application will open in your default web browser.
echo If it doesn't open automatically, go to: http://localhost:8501
echo.
echo To stop the application, close this window or press Ctrl+C
echo.
SystemInfoDashboard.exe
echo.
echo Application has been closed.
pause
'''
    
    with open(dist_dir / 'run_system_info.bat', 'w') as f:
        f.write(batch_content)
    
    # Create README for the executable
    readme_content = '''# System Information Dashboard - Windows Executable

## How to Run:
1. **Easy way**: Double-click 'run_system_info.bat' to start the application
2. **Direct way**: Double-click 'SystemInfoDashboard.exe' directly
3. The application will open in your default web browser at http://localhost:8501

## System Requirements:
- Windows 10 or later
- No additional software installation required
- Internet connection not required (runs locally)

## Features:
- Real-time system information display
- CPU, Memory, and Disk usage monitoring
- Operating system detection (Windows, Linux, macOS)
- Network information and connection details
- Interactive charts and live updates
- Beautiful web-based interface

## Troubleshooting:
If the application doesn't start:
1. Make sure Windows Defender or antivirus isn't blocking it
2. Try running as administrator
3. Check that port 8501 is not in use by another application
4. Ensure you have sufficient disk space and memory

## Technical Details:
- Built with Python and Streamlit
- Packaged with PyInstaller
- Self-contained executable (no Python installation required)
- Runs a local web server on port 8501

## Support:
For issues or questions, please check the source code repository.
'''
    
    with open(dist_dir / 'README.txt', 'w') as f:
        f.write(readme_content)
    
    print("✅ Created distribution files (run_system_info.bat, README.txt)")

def cleanup():
    """Clean up temporary files."""
    files_to_remove = ['build_script.py', 'build_script.spec']
    dirs_to_remove = ['build', '__pycache__']
    
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"🧹 Removed {file}")
    
    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🧹 Removed {dir_name}")

def main():
    """Main build process."""
    print("🚀 Starting System Information Dashboard executable build process...")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        return False
    
    # Create build script
    create_build_script()
    
    # Build executable
    if not build_executable():
        return False
    
    # Create distribution files
    create_distribution_files()
    
    # Cleanup
    cleanup()
    
    print("=" * 60)
    print("🎉 Build completed successfully!")
    print("📁 Executable location: dist/SystemInfoDashboard.exe")
    print("📁 Run script: dist/run_system_info.bat")
    print("📁 Documentation: dist/README.txt")
    print("=" * 60)
    
    return True

if __name__ == '__main__':
    success = main()
    if not success:
        print("❌ Build failed!")
        sys.exit(1)
    else:
        print("✅ Build successful!")
