import nmap

scanner = nmap.PortScanner()

target_ip = "192.168.1.84"

scanner.scan(hosts=target_ip, arguments='-sS -sV -O -p 1-1000')

for host in scanner.all_hosts():
    print(f"\nHost: {host}")
    print(f"State: {scanner[host].state()}")

    if 'osmatch' in scanner[host]:
        for os in scanner[host]['osmatch']:
            print(f"OS: {os['name']} (Accuracy: {os['accuracy']}%)")

    for proto in scanner[host].all_protocols():
        print(f"\nProtocol: {proto}")
        ports = scanner[host][proto].keys()

        for port in sorted(ports):
            state = scanner[host][proto][port]['state']
            service = scanner[host][proto][port]['name']
            product = scanner[host][proto][port].get('product', '')

            print(f"Port: {port} | State: {state} | Service: {service} {product}")