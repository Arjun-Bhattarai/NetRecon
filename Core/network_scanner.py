import nmap
import requests

scanner = nmap.PortScanner()
network_range = "192.168.1.0/24"

def get_vendor(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        res = requests.get(url, timeout=3)
        return res.text if res.status_code == 200 else "Unknown"
    except:
        return "Unknown"

def scan_network():
    scanner.scan(hosts=network_range, arguments="-sn -PR")

    devices = []

    for host in scanner.all_hosts():
        mac = "Unknown"
        vendor = "Unknown"

        if "addresses" in scanner[host]:
            mac = scanner[host]["addresses"].get("mac", "Unknown")
            vendor = get_vendor(mac) if mac != "Unknown" else "Unknown"

        devices.append({
            "ip": host,
            "state": scanner[host].state(),
            "mac": mac,
            "vendor": vendor
        })

    return devices