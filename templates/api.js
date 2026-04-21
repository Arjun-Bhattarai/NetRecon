const API_BASE = "http://127.0.0.1:8000"; // yo localhost ko link bata api banako

export async function scanDevice(ip) {
    let res = await fetch(`${API_BASE}/scan`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ ip })
    }); // yesla scan garna ko lagi ip address pathaune ra response ma scan result aune

    return await res.json();
}

export async function scanNetwork() {
    let res = await fetch(`${API_BASE}/scan-network`, {
        method: "POST"
    }); // yesla network scan garna ko lagi endpoint ma request pathaune ra response ma network scan result aune

    return await res.json();
}