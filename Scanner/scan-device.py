import socket
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Core.risk_engine import calculate_risk
from Core.device_classifier import classify_device
from Core.port_scanner import scan_ports

target_ip = input("Enter target IP: ").strip()


def scan_ports(ip):
    open_ports = []

    for port in [21, 22, 23, 80, 443, 445, 3389, 554]:
        s = socket.socket()
        s.settimeout(0.5)

        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)

        s.close()

    return open_ports


ports = scan_ports(target_ip)

risk_level, issues = calculate_risk(ports)

print("\n===== DEVICE SECURITY REPORT =====")
print(f"Target IP: {target_ip}")
print(f"Open Ports: {ports}")

print(f"\nRisk Level: {risk_level}")

if issues:
    print("Issues Found:")
    for i in issues:
        print(f"- {i}")
else:
    print("No major risks detected")
