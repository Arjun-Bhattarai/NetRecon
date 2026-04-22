import nmap
import requests
from datetime import datetime

scanner = nmap.PortScanner()
network_range = "192.168.1.0/24"


def get_vendor(mac):
    """Get vendor info from MAC address"""
    try:
        url = f"https://api.macvendors.com/{mac}"
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.text.strip()
        return "Unknown"
    except requests.RequestException:
        return "Unknown"


def scan_network():
    """Scan the network and return device list"""
    print(f"\n[+] Scanning network: {network_range} ...\n")

    try:
        scanner.scan(hosts=network_range, arguments="-sn -PR")
    except Exception as e:
        print(f"[!] Scan failed: {e}")
        return []

    devices = []

    for host in scanner.all_hosts():
        mac = "Unknown"
        vendor = "Unknown"

        if "addresses" in scanner[host]:
            mac = scanner[host]["addresses"].get("mac", "Unknown")
            if mac != "Unknown":
                vendor = get_vendor(mac)

        devices.append({
            "ip": host,
            "state": scanner[host].state(),
            "mac": mac,
            "vendor": vendor
        })

    return devices


def display_results(devices):
    if not devices:
        print("[!] No devices found.")
        return

    print("=" * 60)
    print(f"{'IP Address':<18}{'State':<10}{'MAC Address':<20}{'Vendor'}")
    print("=" * 60)

    for d in devices:
        print(f"{d['ip']:<18}{d['state']:<10}{d['mac']:<20}{d['vendor']}")

    print("=" * 60)
    print(f"[+] Total Devices Found: {len(devices)}\n")


if __name__ == "__main__":
    print("=" * 60)
    print("        NetInspector - Network Scanner")
    print(f"        Started at: {datetime.now()}")
    print("=" * 60)

    devices = scan_network()
    display_results(devices)