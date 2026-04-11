import socket

target_ip = input("Enter target IP: ")

def scan_ports(ip):
    open_ports = []

    for port in [21, 22, 23, 80, 443]:
        s = socket.socket()
        s.settimeout(0.5)

        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)

        s.close()


    return open_ports

ports = scan_ports(target_ip)

print("\n===== Port Scan Result =====")
print(f"Target: {target_ip}")

if ports:
    print(f"Open Ports: {ports}")
else:
    print("No open ports found")