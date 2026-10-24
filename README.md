<div align="center">

# 🌐 NET-LAG

**A Stylish Network Bandwidth Stress Tester for Educational Purposes**

[![Python 3](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-brightgreen?style=for-the-badge&logo=linux&logoColor=white)](https://termux.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Educational-red?style=for-the-badge)]()

</div>

---

## 📖 About

**NET-LAG** is a Python-based **UDP bandwidth stress tester** designed for learning network behavior on **your own local network**. It sends a high volume of random UDP packets to your router's gateway IP, simulating a bandwidth exhaustion scenario.

> **⚠️ Disclaimer:** This tool is strictly for **educational purposes** and **testing your own network security**. Using it against any network you do not own or have explicit permission to test is **illegal** and punishable under cyber crime laws. The author is not responsible for any misuse.

---

## ✨ Features

- 🎨 **Stylish Terminal UI** – Colored ASCII banner and live packet counter.
- 🚀 **High-Throughput UDP Flood** – Configurable threads and packet size.
- ⏱️ **Auto-Stop Timer** – Automatically stops after a set duration (default: 60 seconds).
- 🎯 **Target Lock** – Works against your router's gateway IP (e.g., `192.168.1.1`).
- 📱 **Termux & Linux Compatible** – Runs on Android (Termux) and desktop Linux.

---

## 🛠️ Prerequisites

| Requirement | Details |
|-------------|---------|
| **Python** | Python 3.x |
| **Terminal** | Termux (Android) or any Linux Terminal |
| **Network** | Connected to your **own** Wi-Fi network |

---

## 📥 Installation

### 🔹 Option 1: Termux (Android)

```bash
# 1. Update packages
pkg update -y && pkg upgrade -y

# 2. Install Python
pkg install python -y

# 3. Clone the repository
git clone https://github.com/tuhin118/Net-Lag.git

# 4. Navigate into the directory
cd Net-Lag
# 5. Run Termux
python3 net-lag.py 
```

🔹 Option 2: Linux (Ubuntu / Debian / Kali)

```bash
# 1. Update system packages
sudo apt update && sudo apt upgrade -y

# 2. Install Python and Git
sudo apt install python3 git -y

# 3. Clone the repository
git clone https://github.com/tuhin118/Net-Lag.git

# 4. Navigate into the directory
cd Net-Lag
# 5. Run Linux
python3 net-lag.py
```

---

🚀 Usage

1. Find your Router's Gateway IP
   · On Android: Settings → Wi-Fi → Your Network → Gateway / Router
   · On Linux: ip route | grep default
2. Edit the target IP in net-lag.py
      Open the file and locate:
   ```python
   TARGET_IP = "192.168.1.1"   # Replace with your router's IP
   ```
3. Run the script:
   ```bash
   python3 net-lag.py
   ```
4. To stop early: Press CTRL + C in the terminal.
5. 
