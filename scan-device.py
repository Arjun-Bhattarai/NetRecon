import nmap

target_ip = "192.168.1.68"

print(f"[*] Scanning {target_ip}...")

scanner = nmap.PortScanner()

try:
    # Use TCP connect scan (no admin needed)
    scanner.scan(hosts=target_ip, arguments='-sT -p 1-100')
except Exception as e:
    print(f"[!] Error: {e}")
    input("Press Enter to exit...")
    exit()

if not scanner.all_hosts():
    print("[!] No hosts found.")
    input("Press Enter to exit...")
    exit()

for host in scanner.all_hosts():
    print("\n" + "="*40)
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}")
    print("="*40)

    for proto in scanner[host].all_protocols():
        print(f"\nProtocol: {proto}")
        ports = scanner[host][proto]

        for port in sorted(ports):
            state = ports[port]['state']
            service = ports[port]['name']
            print(f"Port {port}: {state} ({service})")

print("\n[*] Done")