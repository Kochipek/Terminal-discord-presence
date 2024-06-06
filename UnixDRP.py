# for Linux terminals!

import os
import time
import psutil
from pypresence import Presence

LaunchCode = "939904925494829086" # paste your client id here
theShell = os.environ['SHELL']
# identify terminal and get terminal data
def getData():
    # identifying terminal
    if "gnome-terminal-server" in (i.name() for i in psutil.process_iter()):
        state = "On GNOME-terminal"
        largeImage = "terminal"
        largeText = "GNOME-terminal"
    elif "konsole" in (i.name() for i in psutil.process_iter()):
        state = "On KDE-Konsole"
        largeImage = "konsole"
        largeText = "KDE-Konsole"
    else:
        state, largeImage, largeText = "On Linux Terminal", None, "Linux Terminal"  # default values

    # identifying shell
    shells = ["ZSH", "Bash", "Tmux", "Fish", "Dash"]

    details, smallImage, smallText = "Using a shell", None, None  # default values
    for shell in shells:
        if theShell.endswith(shell.lower()):
            details = f"Using {shell} shell"
            smallImage = shell.lower()
            smallText = f"{shell} shell"

    return state, largeImage, largeText, details, smallImage, smallText

timeOfStart = time.time()  # shows the elapsed time at the bottom (needs to be started in Slushy.update())

print("Started\n")

# Initialize Presence once
Slushy = Presence(client_id=LaunchCode)
try:
    Slushy.connect()
    print("Connect success!")
except Exception as e:
    print(f"Failed to connect: {e}")
    exit(1)

while True:
    try:
        state, largeImage, largeText, details, smallImage, smallText = getData()
        Slushy.update(
            start=timeOfStart,
            state=state,
            large_image=largeImage,
            large_text=largeText,
            details=details,
            small_image=smallImage,
            small_text=smallText
        )
        time.sleep(30)
    except Exception as e:
        print(f"Update failed: {e}\nWaiting...\n")
        time.sleep(5)
        continue
