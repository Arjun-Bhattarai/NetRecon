import nmap
import requests

scanner = nmap.PortScanner()
network = "192.168.1.0/24"

def get_vendor(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url, timeout=3)
        return response.text if response.status_code == 200 else "Unknown"
    except:
        return "Unknown"

# Only ping scan (no ports)
scanner.scan(hosts=network, arguments="-sn -PR")

print("\n===== Devices on Network =====")

for host in scanner.all_hosts():
    print("\n" + "=" * 40)
    print(f"IP: {host}")
    print(f"State: {scanner[host].state()}")

    hostname = scanner[host].hostname()
    print(f"Hostname: {hostname if hostname else 'Unknown'}")

    mac = "Unknown"
    vendor = "Unknown"

    if "addresses" in scanner[host] and "mac" in scanner[host]["addresses"]:
        mac = scanner[host]["addresses"]["mac"]
        vendor = get_vendor(mac)

    print(f"MAC: {mac}")
    print(f"Vendor: {vendor}")