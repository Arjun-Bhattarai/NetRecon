from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from Core.port_scanner import scan_ports
from Core.device_classifier import classify_device
from Core.risk_engine import calculate_risk
from Core.network_scanner import scan_network
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse) #yesla 
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/scan") # yesla single device ko endpoint banaunchha ra scan garxa
def scan_device(data: dict):
    ip = data.get("ip")

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

@app.post("/scan-network") # yesla network scan ko endpoint banaunchha ra scan garxa 
def network_scan():
    return {
        "devices": scan_network()
    }