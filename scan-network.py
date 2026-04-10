import nmap, requests

scanner = nmap.PortScanner()

target_ip = "192.168.1.0/24"  # yo chai idconfig bata ip lenu parxa jaslai WIFI scan garna chinxa


def get_vendor(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"# yo chai mac address ko vendor information linxa
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except:
        return "Unknown"


scanner.scan(hosts=target_ip, arguments="-sn -PR")# -sn le ping scan garxa, -PR le ARP request pathaunxa local network ma

for host in scanner.all_hosts():
    print("\n" + "=" * 40)
    print(f"IP: {host}")
    print(f"State: {scanner[host].state()}")

    hostname = scanner[host].hostname()
    print(f"Hostname: {hostname if hostname else 'Unknown'}")

    if "addresses" in scanner[host]:
        if "mac" in scanner[host]["addresses"]:
            mac = scanner[host]["addresses"]["mac"]
            print(f"MAC: {mac}")
            vendor = get_vendor(mac)
            print(f"Vendor: {vendor}")
