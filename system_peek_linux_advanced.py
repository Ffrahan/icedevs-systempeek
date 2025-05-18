import platform
import socket
import shutil
import getpass
import subprocess
from datetime import datetime

def bytes_to_gb(bytes):
    return round(bytes / (1024 ** 3), 2)

def get_distro():
    try:
        with open("/etc/os-release") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("PRETTY_NAME"):
                    return line.strip().split("=")[1].replace('"', '')
        return "Unknown Linux"
    except:
        return "Unknown"

def get_cpu_info():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("model name"):
                    return line.split(":")[1].strip()
        return "Unknown"
    except:
        return "Unknown"

def get_uptime():
    try:
        with open("/proc/uptime") as f:
            seconds = float(f.readline().split()[0])
            days = int(seconds // 86400)
            hours = int((seconds % 86400) // 3600)
            minutes = int((seconds % 3600) // 60)
            return f"{days}d {hours}h {minutes}m"
    except:
        return "Unknown"

def get_boot_time():
    try:
        output = subprocess.check_output("who -b", shell=True)
        line = output.decode().strip()
        return line.split("system boot")[-1].strip()
    except:
        return "Unknown"

def get_system_info():
    print("🧊 Ice Devs - System Peek (Linux - Advanced)\n")

    print(f"👤 User: {getpass.getuser()}")
    print(f"🐧 Distro: {get_distro()}")
    print(f"💻 Kernel: {platform.system()} {platform.release()}")
    print(f"🧠 Architecture: {platform.machine()} | Python: {platform.python_version()}")

    hostname = socket.gethostname()
    print(f"📛 Hostname: {hostname}")
    try:
        print(f"🌐 Local IP: {socket.gethostbyname(hostname)}")
    except:
        print("🌐 Local IP: Not available")

    print(f"🧮 CPU: {get_cpu_info()}")

    total, used, free = shutil.disk_usage("/")
    print(f"💾 Disk: Total {bytes_to_gb(total)} GB | Free {bytes_to_gb(free)} GB")

    print(f"⏱️ Uptime: {get_uptime()}")
    print(f"📅 Boot Time: {get_boot_time()}")
    print(f"🕒 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    get_system_info()
