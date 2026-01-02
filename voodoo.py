import subprocess
import os
import sys
from time import sleep

def run_command(cmd):
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

class Colors:
    """Colors for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    banner = f"""{Colors.RED}

 ██▒   █▓ ▒█████   ▒█████  ▓█████▄  ▒█████   ▒█████  
▓██░   █▒▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██▒  ██▒▒██▒  ██▒
 ▓██  █▒░▒██░  ██▒▒██░  ██▒░██   █▌▒██░  ██▒▒██░  ██▒
  ▒██ █░░▒██   ██░▒██   ██░░▓█▄   ▌▒██   ██░▒██   ██░
   ▒▀█░  ░ ████▓▒░░ ████▓▒░░▒████▓ ░ ████▓▒░░ ████▓▒░
   ░ ▐░  ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ 
   ░ ░░    ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒   ░ ▒ ▒░   ░ ▒ ▒░ 
     ░░  ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ░ ░ ░ ▒  ░ ░ ░ ▒  
      ░      ░ ░      ░ ░     ░        ░ ░      ░ ░  
     ░                      ░                        
"""
    print(banner)


def show_main_menu():
    print ("""
╭─────────────────╮
│      MAIN       │
│1. airmon-ng     │
│2. airodump-ng   │
│3. areplay-ng    │
│4. exit          │
╰─────────────────╯
""")
    choice = input("Select (1/2/3/4): ")
    return choice

def airmon_ng_menu():
    while True:
        print("""
╭─────────────────╮
│     AIRMON      │
│1. list Ifaces   │
│2. enable mon    │
│3. disable mon   │
│4. exit          │
╰─────────────────╯
""")
        choice = input("Select (1/2/3/4): ")
        if choice == "1":
            subprocess.run(["sudo", "airmon-ng"])
        elif choice == "2":
            iface = input("Enter Interface: ")
            subprocess.run(["sudo", "airmon-ng", "start", iface])
        elif choice == "3":
            iface = input("Enter Interface: ")
            subprocess.run(["sudo", "airmon-ng", "stop", iface])
        elif choice == "4":
            break

def airodump_ng_menu():
    while True:
        print ("""
╭─────────────────╮
│    AIRODUMP     │
│1. scan around   │
│2. scan target   │
│3. exit          │
╰─────────────────╯
""")
        choice = input("Select (1/2/3): ")
        if choice == "1":
            iface = input("Enter Interface: ")
            try:
                subprocess.run(["sudo", "airodump-ng", iface], check=True)
                if KeyboardInterrupt:
                    return main()
            except subprocess.CalledProcessError:
                print("Interrupted by user...")
        elif choice == "2":
            iface = input("Enter Interface: ")
            bssid = input("Enter BSSID: ")
            channel = input("Enter channel: ")
            try:
                subprocess.run(["sudo", "airodump-ng", "--bssid", bssid, "--channel", channel, iface], check=True)
                if KeyboardInterrupt:
                    return main()
            except subprocess.CalledProcessError:
                print("Interrupted by user...")
        elif choice == "3":
            break

def aireplay_ng_menu():
    while True:
        print ("""
╭──────────────────╮
│$   AIREPLAY      │
│1. deauth attack  │
│2. fakeauth attack│
│3. exit           │
╰──────────────────╯
""")
        choice = input("Select (1/2/3): ")
        if choice == "1":
            iface = input("Enter interface: ")
            bssid = input("Enter BSSID: ")
            client = input("Enter client MAC (nothing for skip): ")
            print("PS: '0' in count of packets means u'll send packets until u interrupt the attack")
            sleep(1)
            count = input("Enter your count of packets (default 0): ") or "0"
            cmd = ["sudo", "aireplay-ng", "--deauth", count, "-a", bssid, iface]
            if client:
                cmd.extend(["-c", client])
            run_command(cmd)
        elif choice == "2":
            iface = input("Enter Interface: ")
            bssid = input("Enter BSSID: ")
            subprocess.run(["sudo", "aireplay-ng", "--fakeauth", "0", "-a", bssid, iface])
        elif choice == "3":
            break

def main():
    while True:
        choice = show_main_menu()
        if choice == "1":
            airmon_ng_menu()
        elif choice == "2":
            airodump_ng_menu()
        elif choice == "3":
            aireplay_ng_menu()
        elif choice == "4":
            print("Exit...")
            break
        else:
            print("Wrong pick, try again.")

if __name__ == "__main__":
    banner()
    main()
