

import os
import platform

def ping_host(ip):
    current_os = platform.system().lower()
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -W 2 {ip} > /dev/null 2>&1"

    return os.system(ping_cmd)

ip_prefix = "192.168.0."

for final_octet in range(1, 255):
    ip = f"{ip_prefix}{final_octet}"
    exit_code = ping_host(ip)

    if exit_code == 0:
        print(f"{ip} is online")
    else:
        print(f"{ip} is offline")
