
<img width="550" height="467" alt="Вставленное изображение" src="https://github.com/user-attachments/assets/90e970d2-8eac-4e87-91da-bcc8761740d2" />

<img width="521" height="468" alt="изображение" src="https://github.com/user-attachments/assets/52dfcd12-5449-43df-9e59-448690a48bb4" />


<img width="503" height="431" alt="Вставленное изображение (3)" src="https://github.com/user-attachments/assets/38d7f72d-bebf-43e5-92bc-3c417e9158ec" />


Python script for semi-automating work with the aircrack-ng suite of utilities via a convenient text-based menu. The script features a CLI interface, enabling seamless interaction with the almost all aircrack-ng functionality for both advanced users and beginners.

## Attention
This script is intended exclusively for testing the security of one's own networks or networks for which official authorization has been obtained. Use for any other purposes may be illegal in your jurisdiction.

Attacks via aireplay are conducted only during active scanning of the selected access point. To perform this, execute the attack in a second terminal window while maintaining active scanning in the first window.

## Last global update: 
* Added automatical power on monitor mode after launch of the script
* Added channel-scan mode
* Airmon-ng had been delated
* Code has been restructured. Now it is prettier than last code

Requirements:
1. Linux
2. Superuser privileges (run with sudo)
3. Wireless adapter supporting monitor mode

## Required packages:
1. Python3
2. Aircrack-ng

## Installation
```
git clone https://github.com/VooDoo-INC/voodoo-aircrack-script.git
```
## Launch
```
cd voodoo-aircrack-script
sudo python3 voodoo.py
```
