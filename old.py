import subprocess
import os
import sys
from colorama import Fore, Style, init

def launch_holmes():
    os.chdir(r"C:\Users\valen\Mr.Holmes")
    subprocess.Popen([sys.executable, "MrHolmes.py"])

def launch_wireshark():
    subprocess.Popen([
    "C:\\Program Files\\Wireshark\\Wireshark.exe"
])

init()




print(Fore.RED + """

 ██▓███   ██▓   ▓██   ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██░  ██▒▓██▒    ▒██  ██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██░ ██▓▒▒██░     ▒██ ██░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██▄█▓▒ ▒▒██░     ░ ▐██▓░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒ ░  ░░██████▒ ░ ██▒▓░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒▓▒░ ░  ░░ ▒░▓  ░  ██▒▒▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░▒ ░     ░ ░ ▒  ░▓██ ░▒░     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░░         ░ ░   ▒ ▒ ░░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
             ░  ░░ ░                  ░ ░      ░ ░      ░  ░
                 ░ ░                                        
""")

print("1: Launch Wireshark")
print("2: Launch Mr Holmes")
choice = input("Select an option (1 or 2): ")

if choice == "1":
    launch_wireshark()
    print(Fore.GREEN + "Wireshark launched successfully!")
elif choice == "2":
    launch_holmes()
    print(Fore.GREEN + "Mr Holmes launched successfully!")