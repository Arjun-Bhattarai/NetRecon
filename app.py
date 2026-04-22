from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from Core.port_scanner import scan_ports
from Core.device_classifier import classify_device
from Core.risk_engine import calculate_risk
from Core.network_scanner import scan_network

app = FastAPI(title="NetInspector API", version="1.0")

app.add_middleware(
    CORSMiddleware,  # CORS vaneko Cross-Origin Resource Sharing ho.

    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)#Yo euta security feature ho web browsers ma, jasle control garxa ki kun website le API lai access garna pauncha.

templates = Jinja2Templates(directory="templates") # yesla templates folder ko path specify garxa


class ScanRequest(BaseModel):
    ip: str


@app.get("/", response_class=HTMLResponse)  # yesla
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/scan")  # yesla single device ko endpoint banaunchha ra scan garxa
def scan_device(data: ScanRequest):
    ip = data.ip

    if not ip:
        raise HTTPException(status_code=400, detail="IP address is required")

    try:
        ports = scan_ports(ip)
        device = classify_device(ports)
        risk, issues = calculate_risk(ports)

        return {
            "ip": ip,
            "ports": ports,
            "device": device,
            "risk": risk,
            "issues": issues
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/scan-network")  # yesla network scan ko endpoint banaunchha ra scan garxa
def network_scan():
    try:
        devices = scan_network()

        return {
            "total_devices": len(devices),
            "devices": devices
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))