import time
import psutil
import subprocess
import ctypes
import platform

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def is_vgc_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] and 'vgc' in process.info['name'].lower():
            return True
    return False

def start_vgc_service():
    try:
        print("[!] vgc is not running. Trying to start it...")
        subprocess.run(["sc", "start", "vgc"], check=True, shell=True)
        print("[+] vgc start command sent.")
    except subprocess.CalledProcessError as e:
        print("[x] Failed to start vgc service:", e)

def main():
    if platform.system() != "Windows":
        print("[x] This script only works on Windows.")
        return

    if not is_admin():
        print("[x] Run this script as Administrator.")
        return

    print("[*] vgc watcher started. Monitoring every 1 second...")

    while True:
        if is_vgc_running():
            print("[✓] vgc is running.")
        else:
            start_vgc_service()
        time.sleep(1)

if __name__ == "__main__":
    main()
