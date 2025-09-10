import streamlit as st
import datetime
import platform
import psutil
import time

# Set page config
st.set_page_config(
    page_title="System Information Dashboard",
    page_icon="🖥️",
    layout="wide"
)

# Main title
st.title("🖥️ System Information Dashboard")
st.markdown("---")

# Create columns for better layout
col1, col2, col3 = st.columns(3)

# Current Time and Date
with col1:
    st.header("📅 Time & Date")
    
    # Real-time clock
    clock_placeholder = st.empty()
    
    # Current date
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    st.subheader(f"📆 {current_date}")
    
    # Auto-refresh the clock every second
    if st.button("🔄 Start Live Clock"):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            clock_placeholder.metric("Current Time", current_time)
            time.sleep(1)

# System Information
with col2:
    st.header("💻 System Information")
    
    # Operating System
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    
    st.subheader("Operating System")
    st.write(f"**System:** {os_name}")
    st.write(f"**Version:** {os_version}")
    st.write(f"**Release:** {os_release}")
    
    # Architecture
    architecture = platform.machine()
    processor = platform.processor()
    
    st.subheader("Hardware")
    st.write(f"**Architecture:** {architecture}")
    st.write(f"**Processor:** {processor}")

# System Resources
with col3:
    st.header("📊 System Resources")
    
    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)
    st.metric("CPU Usage", f"{cpu_percent}%")
    
    # Memory Usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_used = round(memory.used / (1024**3), 2)  # Convert to GB
    memory_total = round(memory.total / (1024**3), 2)  # Convert to GB
    
    st.metric("Memory Usage", f"{memory_percent}%", f"{memory_used}GB / {memory_total}GB")
    
    # Disk Usage
    disk = psutil.disk_usage('/')
    disk_percent = round((disk.used / disk.total) * 100, 1)
    disk_used = round(disk.used / (1024**3), 2)  # Convert to GB
    disk_total = round(disk.total / (1024**3), 2)  # Convert to GB
    
    st.metric("Disk Usage", f"{disk_percent}%", f"{disk_used}GB / {disk_total}GB")

# Additional Information Section
st.markdown("---")
st.header("🔍 Additional System Details")

# Create two columns for additional info
col4, col5 = st.columns(2)

with col4:
    st.subheader("Python Information")
    st.write(f"**Python Version:** {platform.python_version()}")
    st.write(f"**Python Implementation:** {platform.python_implementation()}")
    st.write(f"**Python Compiler:** {platform.python_compiler()}")

with col5:
    st.subheader("Network Information")
    try:
        # Get hostname
        hostname = platform.node()
        st.write(f"**Hostname:** {hostname}")
        
        # Get network interfaces
        network_interfaces = psutil.net_if_addrs()
        st.write(f"**Network Interfaces:** {len(network_interfaces)}")
        
        # Show active connections
        connections = len(psutil.net_connections())
        st.write(f"**Active Connections:** {connections}")
        
    except Exception as e:
        st.write(f"Network info unavailable: {str(e)}")

# Footer
st.markdown("---")
st.markdown("🔄 **Auto-refresh:** The system resources are updated in real-time. Refresh the page to see the latest information.")
st.markdown("💡 **Tip:** Click the 'Start Live Clock' button to see a real-time updating clock!")

# Sidebar with additional options
st.sidebar.header("⚙️ Options")
if st.sidebar.button("🔄 Refresh All Data"):
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Quick Info")
st.sidebar.write(f"**Current OS:** {platform.system()}")
st.sidebar.write(f"**Python:** {platform.python_version()}")
st.sidebar.write(f"**Streamlit:** {st.__version__}")

# Add a simple chart for CPU usage over time
st.sidebar.markdown("---")
st.sidebar.subheader("📈 CPU Usage Trend")
cpu_data = []
for i in range(10):
    cpu_data.append(psutil.cpu_percent(interval=0.1))

st.sidebar.line_chart(cpu_data)
