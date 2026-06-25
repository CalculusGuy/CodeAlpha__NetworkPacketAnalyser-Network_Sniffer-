# 🔍 Network Packet Analyzer

A real-time network packet analyzer built with **Python** and **Scapy** for network security monitoring, traffic analysis, and protocol inspection.

---

## 📌 Overview

Network Packet Analyzer is a lightweight yet powerful tool that captures live network traffic and extracts meaningful information such as source/destination IP addresses, transport protocols, and application-layer payloads. It is designed for cybersecurity enthusiasts, network administrators, and penetration testers to understand how data flows across networks.

---

## ✨ Features

- ✅ **Live Packet Capture** – Sniffs network traffic in real-time
- ✅ **IP & Protocol Extraction** – Identifies TCP, UDP, and ICMP traffic
- ✅ **HTTP Traffic Detection** – Parses HTTP requests and responses (plaintext)
- ✅ **Payload Inspection** – Displays raw packet payloads for deep analysis
- ✅ **Cross-Platform** – Works on Linux, Windows, and macOS
- ✅ **Lightweight & Fast** – Minimal dependencies, optimized for performance

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Scapy** | Packet manipulation and sniffing |
| **Npcap / WinPcap** | Windows packet capture driver |
| **libpcap** | Linux/macOS packet capture |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/CalculusGuy/NetworkPacketAnalyzer.git
cd NetworkPacketAnalyzer
```

2. Install Dependencies
bash
pip install scapy
3. Install Packet Capture Driver (if required)
Windows: Install Npcap (with WinPcap compatibility mode)

Linux: libpcap is pre-installed on most distributions

macOS: Install libpcap via Homebrew (brew install libpcap)

🚀 Usage
Linux / macOS
bash
sudo python3 sniffer.py
Windows (Admin)
bash
python sniffer.py
Note: Administrative/root privileges are required to capture raw network packets.

📊 Sample Output

[*] Starting Network Sniffer...
[*] Press Ctrl+C to stop

[+] Source: 192.168.x.xxx -> Destination: 23.11.xx.xxx
[+] Protocol: TCP
[+] HTTP Traffic Detected!
[+] Payload: GET /DigiCertTrustedG4CodeSigningRSA4096SHA3842021CA1.crl HTTP/1.1
--------------------------------------------------

[+] Source: 23.11.xx.xxx -> Destination: 192.168.x.xxx
[+] Protocol: TCP
[+] HTTP Traffic Detected!
[+] Payload: HTTP/1.1 304 Not Modified
--------------------------------------------------
