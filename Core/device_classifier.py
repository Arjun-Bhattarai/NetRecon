def classify_device(ports):
    ports = set(ports) # Set ma convert garna le fast lookup garna help garcha
    if 554 in ports:
        return "📷 IP Camera"

    if 445 in ports and 3389 in ports:
        return "🪟 Windows PC / Server"

    if 80 in ports and 443 in ports and 22 in ports:
        return "🌐 Router / Gateway"

    if 8080 in ports or 8000 in ports:
        return "⚙️ IoT / Smart Device"

    if 80 in ports or 443 in ports:
        return "🌍 Web Server"

    if 22 in ports:
        return "🐧 Linux Device (SSH enabled)" 

    return "❓ Unknown Device"