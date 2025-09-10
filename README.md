# System Information Dashboard

A simple Streamlit application that displays real-time system information including time, date, and system details.

## Features

- 🕐 **Real-time Clock**: Live updating time display
- 📅 **Current Date**: Today's date in a readable format
- 💻 **System Information**: Operating system details (Windows, Linux, macOS)
- 📊 **System Resources**: CPU, Memory, and Disk usage monitoring
- 🔍 **Additional Details**: Python version, network information, and more
- 📈 **CPU Usage Chart**: Visual representation of CPU usage trends

## Requirements

- Python 3.7 or higher
- Streamlit
- psutil

## Installation

### Option 1: Run from Source Code

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser, typically at `http://localhost:8501`.

### Option 2: Download Windows Executable

1. Go to the [Releases](https://github.com/yourusername/testpythonbuild/releases) page
2. Download the latest `system-info-dashboard-windows.zip`
3. Extract the files
4. Double-click `run_system_info.bat` to start the application

**No Python installation required!** The executable is self-contained.

## Building Windows Executable

### Automatic Build (GitHub Actions)

The Windows executable is automatically built using GitHub Actions when you:
- Push to the main/master branch
- Create a release/tag
- Manually trigger the workflow

The built executable will be available as a downloadable artifact.

### Manual Build (Local)

To build the executable locally on Windows:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the build script:
```bash
python build_exe.py
```

3. The executable will be created in the `dist/` folder:
   - `SystemInfoDashboard.exe` - The main executable
   - `run_system_info.bat` - Easy-to-use batch file
   - `README.txt` - Instructions for end users

### Build Requirements

- Windows 10 or later
- Python 3.7 or higher
- All dependencies from `requirements.txt`

## What You'll See

### Main Dashboard
- **Time & Date Section**: Current time and date with an optional live clock
- **System Information**: OS details, architecture, and processor information
- **System Resources**: Real-time monitoring of CPU, memory, and disk usage

### Additional Features
- **Python Information**: Version and implementation details
- **Network Information**: Hostname and connection details
- **Sidebar Options**: Quick refresh and CPU usage trend chart

## Supported Operating Systems

This application works on:
- ✅ Windows
- ✅ macOS
- ✅ Linux

## Dependencies

- `streamlit`: Web application framework
- `psutil`: System and process utilities
- `pyinstaller`: For building Windows executable (build-time only)
- `platform`: Built-in Python module for system information
- `datetime`: Built-in Python module for date and time

## Customization

You can easily modify the application by:
- Adding more system metrics
- Changing the layout and styling
- Adding new charts and visualizations
- Implementing data logging features

## Troubleshooting

If you encounter any issues:

1. Make sure all dependencies are installed correctly
2. Check that you're using Python 3.7 or higher
3. Ensure you have the necessary permissions to access system information

## License

This project is open source and available under the MIT License.
