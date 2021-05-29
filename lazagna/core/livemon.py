import os
from termcolor import colored

print(colored("ENTER TARGET", 'red'))
t = input ("Enter our target: ")
os.system('grgsm_livemon -f {0}'.format(t))
