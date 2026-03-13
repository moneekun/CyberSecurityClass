import os
import platform


def ping_host(ip):
    current_os = platform.system().lower()
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -W 2 {ip} > /dev/null"

    exit_code = os.system(ping_cmd)
    return exit_code


ip_prefix = "192.168.0."

for final_octet in range(254):
    ip = ip_prefix + str(final_octet+1)
    exit_code = ping_host(ip)

if exit_code == 0:
    print("{0} is online".format(ip))


