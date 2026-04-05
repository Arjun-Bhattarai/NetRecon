import nmap

scanner = nmap.PortScanner()

target_ip = "192.168.1.0/24"# find this by running "ipconfig" in cmd and looking for the IPv4 address, then replacing the last number with 0 and adding /24 at the end

scanner.scan(hosts=target_ip, arguments='-sn')

for host in scanner.all_hosts():
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}")