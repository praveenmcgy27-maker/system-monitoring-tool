import os
import socket
import platform
from datetime import datetime

def system_info():
    print("---- SYSTEM INFO ----")

    # Date & Time
    now = datetime.now()
    print("Date & Time:", now.strftime("%Y-%m-%d %H:%M"))

    # Hostname
    hostname = socket.gethostname()
    print("Hostname:", hostname)

    # Python Version
    print("Python Version:", platform.python_version())

    # Current User
    try:
        user = os.getlogin()
    except:
        user = os.environ.get('USER', 'Unknown')
    print("Current User:", user)

    # Files in Directory
    files = os.listdir(".")
    print("Files in Directory:")
    for f in files:
        print("-", f)

    # Count files
    print("Total Files:", len(files))

    print("----------------------")

def user_input_section():
    print("\n---- USER INPUT ----")
    name = input("Enter your name: ")
    print("Hello,", name, "! Welcome to DevOps Project 🚀")

if __name__ == "__main__":
    system_info()
    user_input_section()