def calculate_risk(ports):
    ports = set(ports)

    score = 0
    issues = []
 # risk level calculate garna ko lagi, hamile common vulnerable ports check garxaun ra tyo port khula cha bhane score badhaune ra issue list ma add garne.
    
    if 23 in ports:
        score += 6
        issues.append("Telnet exposed (insecure)")

    if 21 in ports:
        score += 5
        issues.append("FTP exposed (possibly insecure)")

    if 3389 in ports:
        score += 5
        issues.append("RDP exposed")

    if 554 in ports:
        score += 5
        issues.append("Camera stream exposed")

    if 445 in ports:
        score += 4
        issues.append("SMB exposed (possible vulnerability)")

    if 22 in ports:
        score += 2
        issues.append("SSH exposed")

    if 80 in ports:
        score += 1
        issues.append("HTTP exposed (unencrypted)")

    if 443 in ports:
        issues.append("HTTPS detected (secure communication)")

    # 🎯 Risk Level Classification
    if score <= 2:
        level = "LOW 🟢"
    elif score <= 6:
        level = "MEDIUM 🟡"
    else:
        level = "HIGH 🔴"

    return level, issues