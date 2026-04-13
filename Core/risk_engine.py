def calculate_risk(ports):
    score = 0
    issues = []

    if 22 in ports:
        score += 2
        issues.append("SSH exposed")

    if 80 in ports:
        score += 1
        issues.append("HTTP exposed")

    if 443 in ports:
        score += 1
        issues.append("HTTPS exposed")

    if 445 in ports:
        score += 4
        issues.append("SMB exposed")

    if 3389 in ports:
        score += 5
        issues.append("RDP exposed")

    if 554 in ports:
        score += 5
        issues.append("Camera stream exposed")

    if score <= 2:
        level = "LOW 🟢"
    elif score <= 5:
        level = "MEDIUM 🟡"
    else:
        level = "HIGH 🔴"

    return level, issues