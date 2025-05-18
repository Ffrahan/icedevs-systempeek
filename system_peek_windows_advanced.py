import platform
import socket
import shutil
import time
import getpass
import subprocess
from datetime import datetime

def bytes_to_gb(bytes):
    return round(bytes / (1024 ** 3), 2)

def get_cpu_info():
    try:
        output = subprocess.check_output("wmic cpu get Name,NumberOfCores,NumberOfLogicalProcessors", shell=True)
        lines = output.decode().splitlines()
        values = [line.strip() for line in lines if line.strip()][1]  # skip header
        return values
    except:
        return "Unknown"

def get_boot_time():
    try:
        output = subprocess.check_output("wmic os get LastBootUpTime", shell=True)
        lines = output.decode().splitlines()
        boot_time_raw = [line.strip() for line in lines if line.strip()][1]
        boot_time_str = boot_time_raw.split('.')[0]
        boot_time_dt = datetime.strptime(boot_time_str, '%Y%m%d%H%M%S')
        return boot_time_dt
    except:
        return None

def get_system_info():
    print("🧊 Ice Devs - System Peek (Windows - Advanced)\n")

    print(f"👤 User: {getpass.getuser()}")
    print(f"💻 OS: {platform.system()} {platform.release()} (Version: {platform.version()})")
    print(f"🧠 Architecture: {platform.machine()} | Python: {platform.python_version()}")
    
    hostname = socket.gethostname()
    print(f"📛 Hostname: {hostname}")
    try:
        print(f"🌐 Local IP: {socket.gethostbyname(hostname)}")
    except:
        print("🌐 Local IP: Not available")

    print(f"🧮 CPU Info: {get_cpu_info()}")
    
    total, used, free = shutil.disk_usage("C:\\")
    print(f"💾 Disk: Total {bytes_to_gb(total)} GB | Free {bytes_to_gb(free)} GB")

    boot_time = get_boot_time()
    if boot_time:
        now = datetime.now()
        uptime = now - boot_time
        print(f"⏱️ Uptime: {uptime.days}d {uptime.seconds//3600}h {(uptime.seconds//60)%60}m")
        print(f"📅 Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("⏱️ Uptime: Unknown")

    print(f"🕒 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    get_system_info()
