def classify_device(ports):
    # IP CAMERA
    if 554 in ports:
        return "📷 IP Camera"

    # ROUTER / NETWORK DEVICE
    if 22 in ports and (80 in ports or 443 in ports):
        return "🌐 Router / Gateway"

    # LINUX MACHINE
    if 22 in ports:
        return "🐧 Linux Device (SSH enabled)"

    # WINDOWS MACHINE
    if 445 in ports and 3389 in ports:
        return "🪟 Windows PC / Server"

    # WEB SERVER
    if 80 in ports or 443 in ports:
        return "🌍 Web Server"

    # IOT DEVICE
    if 8080 in ports or 8000 in ports:
        return "⚙️ IoT / Smart Device"

    return "❓ Unknown Device"