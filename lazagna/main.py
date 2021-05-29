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
def helpText():
    print("""
scan - Scanning of cellular stations in a radius of action
help - this menu
capture - start capture gsm signal
exit - exit from this script
----------------------------------------------------------------------------------------
https://github.com/ptrkrysik/gr-gsm
https://github.com/Oros42/IMSI-catcher

my telegram channel: t.me/termuxqew
        """)

print("""Type "help" for the help prompt.
    """)
while True:
        user_input = input("lazagna-gsm'> ").lower()
        if user_input == "help":
            helpText()
        elif user_input == "exit":
            sys.exit()
        elif user_input == "capture":
            print (f"""                           .::                                    
   .:::   .::    .: .::  .:.: .:.::  .::.: .:::   .:: .::     .::   
 .::    .::  .:: .:  .::   .::  .::  .:: .::   .:: .::  .:: .::  .::
.::    .::   .:: .:   .::  .::  .::  .:: .::   .:: .::  .::.::   .::
 .::   .::   .:: .:: .::   .::  .::  .:: .::   .:: .::  .:: .::  .::
   .:::  .:: .:::.::        .::   .::.::.:::   .::.:::  .::     .:: 
                 .::                                         .:: 
""")
            os.system ("sudo xterm -geometry 93x31+100+350 -hold -T wiretapping -e python3 core/livemon.py & sudo xterm -geometry 93x91+900+300 -hold -T IMSI-catcher -e python3 core/imsi.py & xterm -T wireshark_Sms_Capturing -e sudo wireshark -k -f udp -Y gsm_sms -i lo")
        elif user_input == "scan":
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
            os.system("sudo grgsm_scanner -v -b GSM900 --args=rtl")

                        
