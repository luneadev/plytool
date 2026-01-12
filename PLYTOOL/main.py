import subprocess
import os
import sys
import webbrowser
from colorama import Fore, Style, init

SCRIPT_PATH = os.path.abspath(__file__)

def launch_holmes():
    path = r"C:\Users\\" + usernameWindows + "\\Mr.Holmes"
    script = "MrHolmes.py"
    subprocess.Popen(f'start cmd /k "cd /d {path} && {sys.executable} {script}"', shell=True)



    

def launch_wireshark():
    subprocess.Popen([
    "C:\\Program Files\\Wireshark\\Wireshark.exe"
    
])
    
def relaunch_launcher():
    # relance le launcher dans une NOUVELLE fenêtre et ferme celle-ci
    subprocess.Popen(f'start cmd /c "{sys.executable} {SCRIPT_PATH}"', shell=True)
    sys.exit()



init()

usernameWindows = os.getlogin()



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

print("1: Launch App Wireshark")
print("2: Launch Cmd Mr Holmes")
print("3: Launch Web Discord Channels Symbols")
print("4: Launch Web OSINTMAP")
print("5: Launch Web Emojis Panel")
print("6: Launch Web Secure Bigs Files Transfer")
choice = input("Select an option: ")

if choice == "1":
    launch_wireshark()
    print(Fore.GREEN + "Wireshark launched successfully!")
    relaunch_launcher()
elif choice == "2":
    launch_holmes()
    print(Fore.GREEN + "Mr Holmes launched successfully!")
    relaunch_launcher()
elif choice == "3":
    webbrowser.open("https://discordgate.com/tools/symbols")
    print(Fore.GREEN + "DiscordSymbols launched in your web browser!")
    relaunch_launcher()
elif choice == "4":
    webbrowser.open("https://nikoko107.github.io/OSINTMap/")
    print(Fore.GREEN + "OSINTMAP launched in your web browser!")
    relaunch_launcher()
elif choice == "5":
    webbrowser.open("https://emojikeyboard.top/")
    print(Fore.GREEN + "Emojis Panel launched in your web browser!")
    relaunch_launcher()
elif choice == "6":
    webbrowser.open("https://sharealuxz.fr/")
    print(Fore.GREEN + "Secure Bigs Files Transfer launched in your web browser!")
    relaunch_launcher()
