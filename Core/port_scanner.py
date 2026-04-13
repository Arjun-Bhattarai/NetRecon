import socket

def scan_ports(ip):
    open_ports = []

    common_ports = [21, 22, 23, 80, 443, 445, 3389, 554, 8000, 8080]

    for port in common_ports:
        s = socket.socket()
        s.settimeout(0.5)

        try:
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
        except:
            pass

        s.close()

    return open_ports
