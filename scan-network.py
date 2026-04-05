import nmap

scanner = nmap.PortScanner()

target_ip = "192.168.1.0/24"#yo chai idconfig bata ip lenu parxa jaslai WIFI scan garna chinxa 

scanner.scan(hosts=target_ip, arguments='-sn')

for host in scanner.all_hosts():
    print("\n" + "="*40)
    print(f"IP: {host}")
    print(f"State: {scanner[host].state()}")

    
    hostname = scanner[host].hostname()
    print(f"Hostname: {hostname if hostname else 'Unknown'}")

    if 'addresses' in scanner[host] and 'mac' in scanner[host]['addresses']:
        print(f"MAC: {scanner[host]['addresses']['mac']}")