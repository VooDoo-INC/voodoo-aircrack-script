![preview](https://github.com/user-attachments/assets/375f08a9-cd46-47e0-acce-205dba44dc9d)


Python script for semi-automating work with the aircrack-ng suite of utilities via a convenient text-based menu. The script features a CLI interface, enabling seamless interaction with the almost all aircrack-ng functionality for both advanced users and beginners.

Attention: This script is intended exclusively for testing the security of one's own networks or networks for which official authorization has been obtained. Use for any other purposes may be illegal in your jurisdiction.

Attacks via aireplay are conducted only during active scanning of the selected access point. To perform this, execute the attack in a second terminal window while maintaining active scanning in the first window.

Requirements:
1. Linux (the script was developed and tested on Arch Linux; functionality on other distributions is not guaranteed)
2. Superuser privileges (run with sudo)
3. Wireless adapter supporting monitor mode

Required packages:
1. Python3
2. Aircrack-ng

Installation:
```
git clone https://github.com/VooDoo-INC/voodoo-aircrack-script.git
```
Launch:
```
cd voodoo-aircrack-script
sudo python3 voodoo.py
```
