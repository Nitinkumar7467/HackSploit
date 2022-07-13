#!/use/bin/python3
import banner

import os
import argparse
from colorama import Fore
from socket import *

# import modules

banner.banner()
#functions calls

show_options = '''
Name                Required  Description
----                --------  -----------
TARGET_EMAIL           yes      This is email for your target.

PASSWORD_FILE          yes      This is password list file.
'''
help = """
HackSploit-Framework help:-

"""
while True:
      user_input = input(Fore.WHITE + "HSF"+Fore.RED +Fore.WHITE + "> ")
#cmd handle start
      if user_input == 'exit':
         print(Fore.RED+"["+Fore.BLUE+"+"+Fore.RED+"]"+Fore.WHITE+" THANKS FOR USE ")
         exit()
      elif user_input == 'ls':
         os.system("ls")
      elif user_input == 'whoami':
         print("HackSploit")
      elif user_input == 'pwd':
         print(os.getcwd())
      elif user_input == 'ip':
         os.system("ifconfig")
      elif user_input == 'clear':
         os.system("clear")
      elif user_input == 'banner':
         banner.banner()
      elif user_input == 'help':
         print(help)
#cmd handle stop
 

      else:
         print(Fore.RED+"["+Fore.BLUE+"+"+Fore.RED+"]"+Fore.WHITE+"Command Not Found! ")
