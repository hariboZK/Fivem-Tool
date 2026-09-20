<div align="center">

# 🎮 HARIBO MULTI TOOL v1.0

**An all-in-one FiveM intelligence, network diagnostic, and server stress testing utility with a dark-themed Tkinter GUI.**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-ff2222?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![Author](https://img.shields.io/badge/author-Haribo-ff2222.svg?style=for-the-badge)](https://github.com/)
[![Version](https://img.shields.io/badge/version-1.0-brightgreen.svg?style=for-the-badge)](https://github.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

[Modules](#-modules--features) • [Installation](#-installation) • [Usage](#-usage) • [Interface Preview](#-interface-preview) • [Disclaimer](#-disclaimer)

</div>

---

## ✨ Modules & Features

### 🌐 1. IP & Network Management (IP DEG)
- **External IP Query:** Fetches your current public IP via redundant API endpoints.
- **Proxy Rotation:** SOCKS5 and HTTP proxy support with random rotation from a user-supplied proxy list.
- **Adapter LAN IP Switch:** Configure local network adapter IPs directly.
- **MAC Spoof & DHCP Renew:** Network interface MAC address configuration and automated DHCP renewal.

### 🎯 2. FiveM Server Intelligence (FIVEM)
- **Server Lookup:** Query FiveM servers by IP/Port or CFX.re join codes (`cfx.re/join/xxxxxx`).
- **Player & Resource Extraction:** Fetches active player lists, server variables, and installed server resources/scripts (`/players.json` and `/info.json`).
- **Port 30120 Scanner:** Scans IP ranges to discover live FiveM servers on the default game port.
- **System & HWID Inspector:** Inspects local machine GUID, MAC addresses, and environment details.
- **Export Data:** Saves queried server data to timestamped text files.

### ⚡ 3. Network Stress Testing & Benchmark (DDOS/FLOOD)
*Designed for server administrators to benchmark firewall resilience and server capacity.*
- **Multiple Protocols:**
  - **UDP Flood:** High-throughput UDP datagram transmission with configurable packet sizes.
  - **TCP Flood:** Multi-threaded TCP connection stress test.
  - **HTTP GET / POST Flood:** Web service load testing with randomized query strings and payloads.
  - **Slowloris:** Low-bandwidth connection exhaustion test.
  - **ICMP Flood:** Raw socket ICMP ping stress testing.
- **Live Metrics:** Real-time packet counter, packet rate (`pkt/s`), and thread monitoring.

### 🔍 4. Network Diagnostics (NETWORK)
- **GeoIP Lookup:** Detailed IP intelligence (Country, City, ISP, ASN, Latitude/Longitude, Proxy/Hosting detection).
- **Multi-Threaded Port Scanner:** Fast port range scanning (`1-1024` or custom ranges) with open port detection.
- **Ping & Traceroute:** ICMP latency check and hop-by-hop route tracing.
- **DNS & RDAP/Whois:** Resolves domain records and IP registration details via ARIN/RDAP.
- **Subnet Ping Sweep:** Discovers active live hosts across `/24` subnets (`.1-254`).
- **Banner Grabbing:** Connects and reads server HTTP service headers.
- **Local Diagnostics:** Quick access to `ipconfig`, `arp -a`, and `netstat -ano`.

### 💥 5. FiveM Client Testing (CRASH TOOL)
- **Client Disconnect Simulator:** Triggers controlled client disconnects with custom quit/crash messages (e.g., `"Disconnected by admin"`).
- **Delayed & Loop Mode:** Schedule timed disconnects or recurring test loops for debugging FiveM reconnect handlers.

---

## 📸 Interface Preview

```text
+-----------------------------------------------------------------------------------+
| === HARIBO MULTI TOOL v1.0                                         Made By Haribo |
+-----------------------------------------------------------------------------------+
| [ IP DEG ] [ FIVEM ] [ DDOS/FLOOD ] [ NETWORK ] [ INTEL ] [ MONITOR ] [ CRASH ]  |
+-----------------------------------------------------------------------------------+
|  FIVEM SERVER INTELLIGENCE                                                        |
|  Server IP / CFX Code: [ cfx.re/join/abc123  ] [ Query Server ] [ Scan Range ]    |
|                                                                                   |
|  Server Name: [TR] Haribo Roleplay | Whitelist | discord.gg/...                   |
|  Players: 64 / 128   |  Game Build: 3095   |  OneSync: Enabled                   |
|                                                                                   |
|  Installed Resources:                                                             |
|  - es_extended        - qb-core             - ox_lib                              |
|  - ox_inventory       - vMenu               - pma-voice                           |
|                                                                                   |
|  Console Output:                                                                  |
|  [16:20:05] [INFO] Connected to CFX router: cfx.re/join/abc123                    |
|  [16:20:06] [OK] Server online: 64 players connected                              |
+-----------------------------------------------------------------------------------+
```

---

## 🚀 Installation

### 1. Prerequisites
- **Windows 10 / 11**
- **Python 3.8+** installed on your system.

### 2. Setup
Navigate to the directory:
```powershell
cd "C:\Users\Haribooo\Desktop\tool\fivem tool"
```

Install the required dependencies:
```powershell
pip install -r requirements.txt
```

---

## 💻 Usage

### Quick Start (Windows)
Double-click [`run.bat`](file:///C:/Users/Haribooo/Desktop/tool/fivem%20tool/run.bat) or run via terminal:
```powershell
python haribo_tool.py
```

### Module Guide:
1. **IP DEG:** Choose your method (Proxy, Adapter, or MAC+DHCP) and click **IP DEGISTIR**.
2. **FIVEM:** Paste a FiveM server IP:Port or CFX join URL to extract player lists and resources.
3. **DDOS/FLOOD:** Set target host, port, thread count, and method for network load testing.
4. **NETWORK:** Run GeoIP, Port scans, Subnet sweeps, or DNS lookups.
5. **CRASH TOOL:** Test FiveM client quit/disconnect behaviors with custom messages.

---

## 📂 Project Structure

```text
fivem tool/
│
├── haribo_tool.py        # Main GUI application & network engine
├── patcher.py            # Utility / patcher module
├── run.bat               # Windows batch launcher
├── requirements.txt      # Dependencies (requests)
└── README.md             # Documentation
```

---

## ⚖️ Disclaimer

This tool is developed for **educational purposes, network diagnostics, and authorized server load testing only**.
Performing stress tests or unauthorized scans against networks or servers without explicit permission from the owner is illegal and violates computer misuse laws. The author assumes no liability for any misuse or damages caused by this program.
