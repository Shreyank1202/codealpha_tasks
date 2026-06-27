# 🔍 Basic Network Packet Sniffer

A Python-based network packet sniffer built using **Scapy** that captures live network traffic and displays useful information including Source/Destination IPs, Protocols, Ports, and Payloads.

> Developed as Task 1 of the CodeAlpha Cyber Security Internship to demonstrate live packet capture and analysis using Python and Scapy.

---

## 📸 Demo

```
============================================================
         BASIC NETWORK SNIFFER
============================================================
[*] Interface : Auto-detect
[*] Filter    : None (all packets)
[*] Count     : Unlimited
[*] Press Ctrl+C to stop
------------------------------------------------------------

[Packet #1]  16:38:47  |  82 bytes
  Protocol : TCP
  Source   : 192.168.1.12:63942
  Dest     : 20.195.65.193:443
  Payload  : No payload
------------------------------------------------------------

[Packet #2]  16:38:47  |  123 bytes
  Protocol : UDP
  Source   : 142.250.70.42:443
  Dest     : 192.168.1.12:54540
  Payload  : No payload
------------------------------------------------------------
```

---

## 📋 Features

- 📡 **Live packet capture** on any network interface
- 🌐 **Source & Destination IP** extraction with ports
- 🔎 **Protocol detection** — TCP, UDP, ICMP
- 📦 **Payload extraction** with UTF-8 decoding
- 🗂️ **BPF Filtering** — filter by protocol, port, or IP
- 💾 **Automatic logging** to `logs/packets.log`
- 🔢 **Live packet counter** with timestamps

---

## 🗂️ Project Structure

```
Task-1-Network-Packet-Sniffer/
│
├── display.py
├── filters.py
├── packet_handler.py
├── sniffer.py
├── requirements.txt
├── README.md
└── logs/
    └── packets.log
```

---

## ⚙️ Requirements

- Python 3.10 or later
- [Npcap](https://npcap.com) (Windows only — required for raw packet access)
- Scapy (installed using `pip install -r requirements.txt`)

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shreyank1202/codealpha_tasks.git
cd codealpha_tasks/Task-1-Network-Packet-Sniffer
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Npcap (Windows only)

Download and install from [https://npcap.com](https://npcap.com)

> ✅ During installation, check **"Install Npcap in WinPcap API-compatible Mode"**

---

## ▶️ Running the Sniffer

> ⚠️ **Must be run as Administrator (Windows) or with sudo (Linux/Mac)**

```bash
python sniffer.py

```

## The program will begin capturing live packets immediately. Press Ctrl+C to stop packet capture.

## 🔧 Configuration

Open `sniffer.py` and edit these three variables at the bottom:

```python
INTERFACE = None       # None = auto-detect
                       # Or specify: "Wi-Fi" / "Ethernet"

FILTER    = None       # None = capture everything
                       # Or use BPF: "tcp" / "udp" / "icmp" / "port 443"

COUNT     = 0          # 0 = capture forever
                       # Or set a number: 50
```

### BPF Filter Examples

| Filter String    | What it captures           |
| ---------------- | -------------------------- |
| `"tcp"`          | Only TCP packets           |
| `"udp"`          | Only UDP packets           |
| `"icmp"`         | Only ping packets          |
| `"port 80"`      | Only HTTP traffic          |
| `"port 443"`     | Only HTTPS traffic         |
| `"host 8.8.8.8"` | Traffic to/from Google DNS |

---

## 🔩 Custom Filtering (`filters.py`)

You can also filter inside `filters.py` without using BPF:

```python
ALLOWED_PROTOCOLS = ["TCP", "UDP"]   # only TCP and UDP
BLOCKED_IPS       = ["192.168.1.1"]  # ignore router traffic
ALLOWED_PORTS     = [80, 443]        # only HTTP and HTTPS
```

Leave any list empty `[]` to disable that filter.

---

## 📝 Logging

All captured packets are automatically saved to `logs/packets.log`.

The log file is created automatically on first run. Each entry includes:

- Packet number
- Timestamp
- Packet size
- Protocol
- Source and Destination (IP + Port)
- Payload (if any)

---

## 🧠 How It Works

```
Network Traffic
      │
      ▼
  Scapy sniff()            ← Captures raw packets from the wire
      │
      ▼
 packet_handler.py         ← Extracts IP, Protocol, Ports, Payload
      │
      ▼
   filters.py              ← Decides whether to display this packet
      │
      ▼
   display.py              ← Prints to terminal + logs to file
```

---

## ⚖️ Ethical & Legal Notice

This tool is intended for **educational purposes only**.

- ✅ Only use on networks you **own** or have **explicit permission** to monitor
- ✅ Safe to use on your own machine and home network
- ❌ Do NOT use on public WiFi or any network without authorization
- ❌ Do NOT use to capture credentials or private data

Unauthorized network sniffing is illegal under India's **IT Act 2000 (Sections 43 & 66)** and equivalent laws in other countries.

---

## 🛠️ Built With

- [Python 3](https://python.org)
- [Scapy](https://scapy.net) — Packet manipulation and capture library
- [Npcap](https://npcap.com) — Windows packet capture driver

---

## 📚 Concepts Demonstrated

- OSI Model (Layers 2–7)
- Ethernet Frames, IP Packets, TCP/UDP Segments
- Packet Encapsulation and De-encapsulation
- BPF (Berkeley Packet Filter) syntax
- Protocol identification (TCP / UDP / ICMP)
- Raw payload extraction and UTF-8 decoding

---

## 👤 Author

Shreyank Yadav
B.Tech CSE(Ai)
GitHub:
https://github.com/Shreyank1202
