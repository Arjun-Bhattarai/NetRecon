# 🛡️ NetRecon

> A Python-based network reconnaissance and security analysis tool to discover devices, scan ports, classify systems, and identify potential risks on local networks.

---

## 🚀 Overview

**NetRecon** is a lightweight yet powerful network scanning and analysis tool built using **Python + Nmap + FastAPI**.  
It helps users explore their local network by discovering connected devices, identifying open ports, classifying device types, and analyzing potential security risks.

The project is designed for **cybersecurity learning, network auditing, and hackathon-level demonstrations**.

---

## ✨ Features

- 🔍 Scan entire local network (e.g., `192.168.1.0/24`)
- 📡 Detect active devices with IP, MAC address, and vendor details
- 🔌 Identify open ports on individual devices
- 🧠 Smart device classification (Router, PC, IP Camera, IoT, etc.)
- ⚠️ Risk analysis based on exposed services (SSH, SMB, RDP, etc.)
- 🌐 REST API backend using FastAPI
- 🖥️ Simple web-based frontend dashboard

---

## 🏗️ Architecture

- **Core/** → Scanning & security logic  
- **FastAPI backend** → API layer (`/scan`, `/scan-network`)  
- **Frontend (HTML/JS)** → UI dashboard  
- **Nmap + Socket** → Network discovery engine  

---

## 🛠️ Tech Stack

- Python 🐍  
- FastAPI ⚡  
- socket (low-level port scanning)  
- Nmap (network discovery engine)  
- HTML, JavaScript (frontend UI)  

---

## 🎯 Purpose

- Learn real-world networking & cybersecurity concepts  
- Practice port scanning and service detection  
- Understand device fingerprinting  
- Build SOC-style monitoring logic  

---

## ⚠️ Disclaimer

This tool is intended for **educational and authorized network testing only**.  
Do not use it on networks you do not own or have permission to scan.
