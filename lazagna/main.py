import os
import time
import sys
from termcolor import colored

time.sleep(0.2)
print (f"""

██╗      █████╗ ███████╗ █████╗  ██████╗ ███╗   ██╗ █████╗      ██████╗ ███████╗███╗   ███╗
██║     ██╔══██╗██╔════╝██╔══██╗██╔════╝ ████╗  ██║██╔══██╗    ██╔════╝ ██╔════╝████╗ ████║
██║     ███████║███████╗███████║██║  ███╗██╔██╗ ██║███████║    ██║  ███╗███████╗██╔████╔██║
██║     ██╔══██║╚════██║██╔══██║██║   ██║██║╚██╗██║██╔══██║    ██║   ██║╚════██║██║╚██╔╝██║
███████╗██║  ██║███████║██║  ██║╚██████╔╝██║ ╚████║██║  ██║    ╚██████╔╝███████║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝     ╚═╝
""")
print(colored("Tool for capturing gsm traffic with Gr-Gsm & IMSI-catcher", 'blue'))
time.sleep(0.9)
os.system("lsusb")
usb = input("continue? [y/n]")
if usb == "n":
	sys.exit()
time.sleep(0.2)
print (f"""
.d8888b   .d8888b  8888b.  88888b.  88888b.   .d88b.  888d888 
88K      d88P"        "88b 888 "88b 888 "88b d8P  Y8b 888P"   
"Y8888b. 888      .d888888 888  888 888  888 88888888 888     
     X88 Y88b.    888  888 888  888 888  888 Y8b.     888     
 88888P'  "Y8888P "Y888888 888  888 888  888  "Y8888  888  
""")
os.system ("sudo xterm -hold -T Disclaimer -e python core/dsc.py")
print(colored("SCANNING...", 'red'))
os.system("bash core/scan.sh")
print (f"""
                           .::                                      
                           .::                  .:                  
   .:::   .::    .: .::  .:.: .:.::  .::.: .:::   .:: .::     .::   
 .::    .::  .:: .:  .::   .::  .::  .:: .::   .:: .::  .:: .::  .::
.::    .::   .:: .:   .::  .::  .::  .:: .::   .:: .::  .::.::   .::
 .::   .::   .:: .:: .::   .::  .::  .:: .::   .:: .::  .:: .::  .::
   .:::  .:: .:::.::        .::   .::.::.:::   .::.:::  .::     .:: 
                 .::                                         .:: 
""")
os.system ("sudo xterm -hold -T wiretapping -e python3 core/livemon.py & sudo xterm -hold -T IMSI-catcher -e python3 core/imsi.py")
