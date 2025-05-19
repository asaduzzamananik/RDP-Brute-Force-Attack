# 🛡️ RDP Brute-Force Attack Tool

This is a Python-based brute-force script designed for **ethical hacking** and **cybersecurity learning** in a **controlled lab environment**. It targets a Windows VM with Remote Desktop Protocol (RDP) enabled and tests a list of passwords to identify weak credentials.

> ⚠️ **Disclaimer:** This tool is for educational and authorized penetration testing purposes **only**. Misuse is illegal.

---

## 🧰 Features

- Python script using `xfreerdp`
- Tests 10 common passwords from a built-in wordlist
- Simple, beginner-friendly code
- Intended for virtual lab environments only

---

## 🖥️ Lab Setup Instructions

### Step 1: Setup Network in VirtualBox

- Use **Host-Only Adapter** (or Internal Network) for both VMs:
  - Go to: *VirtualBox → Settings → Network*
  - Set `Adapter 1` → `Enable Network Adapter`
  - Attached to: **Host-Only Adapter**
  - Adapter Type: `Intel PRO/1000 MT Desktop`

Repeat the same for **Windows VM**.

### Step 2: Get IP Addresses

- **Kali Linux:**  
  Run `ip a` or `ifconfig`  
  Look for something like: `192.168.56.103`

- **Windows VM:**  
  Run `cmd` → `ipconfig`  
  Find: `IPv4 Address: 192.168.56.102`

---

## ⚙️ Windows RDP Configuration

### Step 3: Enable RDP

- Run: `SystemPropertiesRemote`
- Check: ✅ Allow remote connections
- Uncheck: ❌ “Allow connections only from computers with NLA”

### Step 4: Allow RDP Through Firewall

Run the following command as **Administrator** in CMD:

```bash
netsh advfirewall firewall add rule name="Allow RDP" dir=in action=allow protocol=TCP localport=3389
