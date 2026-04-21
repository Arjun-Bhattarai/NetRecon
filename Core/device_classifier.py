def classify_device(ports):
    if 554 in ports:
        return "📷 IP Camera"

    if 22 in ports and (80 in ports or 443 in ports):
        return "🌐 Router / Gateway"

    if 22 in ports:
        return "🐧 Linux Device (SSH enabled)"

    if 445 in ports and 3389 in ports:
        return "🪟 Windows PC / Server"

    if 80 in ports or 443 in ports:
        return "🌍 Web Server"

    if 8080 in ports or 8000 in ports:
        return "⚙️ IoT / Smart Device"

    return "❓ Unknown Device"