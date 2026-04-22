import socket

def scan_ports(ip):
    open_ports = []

    common_ports = [21, 22, 23, 80, 443, 445, 3389, 554, 8000, 8080]

    for port in common_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # yesla socket create garxa for IPv4 and TCP
                s.settimeout(0.5)

                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)

        except Exception:
            pass

    return open_ports