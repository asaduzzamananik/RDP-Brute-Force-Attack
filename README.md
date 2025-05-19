# RDP Brute-Force Lab

This project demonstrates a basic RDP brute-force attack in a VirtualBox environment using Kali Linux and a Windows VM.

## Files
- `rdp_try10.py`: Python brute-force script using xfreerdp
- `notes.txt`: Step-by-step notes and configuration
- `screenshots/`: Images from the lab setup and execution

 STEP 1: Network Setup in VirtualBox
1.1 Configure Host-Only Adapter for both VMs
      • Shutdown both VMs.
      • Go to VirtualBox → Select Kali VM → Settings → Network:
  - Adapter 1 → Enable Network Adapter
  -Set Attached to: Host-Only Adapter
  (OR Internal Network, but both VMs must use the same mode)
  Click Advanced → Set Adapter Type to: Intel PRO/1000 MT Desktop 
    • Repeat the same for Windows VM.
1.2 Boot both machines
  • Start Kali Linux and Windows in VirtualBox.

 STEP 2: Get IP Addresses
On Kali Linux, run:
    ip a / ifconfig
Look for something like:
  	inet 192.168.56.103 (under eth0 )

On Windows, press Win + R, type: cmd and run:
    ipconfig
Look for:
    IPv4 Address. . . . . . . . . . . : 192.168.56.102


STEP 3: Enable RDP on Windows VM
    - Enable RDP
    Press Win + R, run:
    SystemPropertiesRemote
    • Check:  Allow remote connections to this computer
    • Uncheck:  “Allow connections only from computers running Remote Desktop with NLA”

STEP 4: Allow RDP in Windows Firewall
Open Command Prompt (as admin) and run:
netsh advfirewall firewall add rule name="Allow RDP" dir=in action=allow protocol=TCP localport=3389

 STEP 5: Test RDP Connection from Kali
5.1 Install xfreerdp
    sudo apt update
    sudo apt install freerdp2-x11

 STEP 6: Create Python Brute-Force Script
6.1 Open Terminal → Create Script
    nano rdp_brute.py
6.2 Paste the Script:

6.3 Save and Exit
	6.3 Save and Exit
      • Press Ctrl + O, then Enter to save.
      • Press Ctrl + X to exit nano.
 STEP 7: Run the Brute-Force Script
Run the script in kali linux using:
    python3 rdp_brute.py

 STEP 7: Run the Brute-Force Script
Run the script in kali linux using:
python3 rdp_brute.py


