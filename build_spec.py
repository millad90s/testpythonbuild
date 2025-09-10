#!/usr/bin/env python3
"""
Alternative build approach using PyInstaller spec file for better Streamlit compatibility.
"""

import os
import sys
import subprocess
from pathlib import Path

def create_spec_file():
    """Create a PyInstaller spec file for better Streamlit handling."""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['build_script.py'],
    pathex=[],
    binaries=[],
    datas=[('app.py', '.')],
    hiddenimports=[
        'streamlit',
        'streamlit.web',
        'streamlit.web.cli',
        'streamlit.runtime',
        'streamlit.runtime.scriptrunner',
        'streamlit.runtime.state',
        'streamlit.components',
        'streamlit.components.v1',
        'altair',
        'pandas',
        'numpy',
        'psutil',
        'platform',
        'datetime',
        'time',
        'importlib.metadata',
        'pkg_resources',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SystemInfoDashboard',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    with open('SystemInfoDashboard.spec', 'w') as f:
        f.write(spec_content)
    print("✅ Created SystemInfoDashboard.spec file")

def build_with_spec():
    """Build using the spec file."""
    print("🔨 Building executable using spec file...")
    
    try:
        result = subprocess.run(['pyinstaller', 'SystemInfoDashboard.spec'], 
                              check=True, capture_output=True, text=True)
        print("✅ Executable built successfully with spec file!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building with spec file: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False

def main():
    """Main build process using spec file."""
    print("🚀 Building with PyInstaller spec file approach...")
    print("=" * 60)
    
    # Create spec file
    create_spec_file()
    
    # Build with spec file
    if build_with_spec():
        print("=" * 60)
        print("🎉 Build completed successfully!")
        print("📁 Executable location: dist/SystemInfoDashboard.exe")
        print("=" * 60)
        return True
    else:
        print("❌ Build failed!")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
