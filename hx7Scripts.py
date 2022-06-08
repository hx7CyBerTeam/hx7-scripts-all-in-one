import os, sys, time
from colorama import Fore, Back, Style
from tkinter import messagebox

# ==== system ==== #

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
def typingPrint2(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
def typingPrint3(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.06)
def typingPrint4(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
def typingPrint5(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()
  return value


# ===== starting hx7 system ===== #

class ap():
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.write("\x1b]2;EvilToken Bruteforcerz\x07")
    typingPrint(f"""{Fore.YELLOW}{Style.BRIGHT}
 _              _____                  _
| |__   __  __ |___  |   ___   _   _  | |__     ___   _ __
| '_ \  \ \/ /    / /   / __| | | | | | '_ \   / _ \ | '__|
| | | |  >  <    / /   | (__  | |_| | | |_) | |  __/ | |
|_| |_| /_/\_\  /_/     \___|  \__, | |_.__/   \___| |_|
                               |___/

[>] Tool improvised by : @hx7 | hadixd7.
[>] Original Author : hx7 team owner | hadixd7.{Fore.RESET}
""")


def mainMenu():
    # scripts #
    time.sleep(0.9)
    typingPrint5("""
┍──━──━──┙◆┕──━──━──┑┍──━──━──┙◆┕──━──━──┑
                  CREDITS

Author   : *hx7 | hadixd*
Team    : hx7 team
Instagram : @h_a_c_k_7_7
Version   : 1.0

┕──━──━──┑◆┍──━──━──┙┕──━──━──┑◆┍──━──━──┙
""")

    print ('Tools :\n')

    typingPrint4("""
 --=> [1] hx7 Port Grabber
 --=> [2] hx7 Port Grabber [By: Port Name]
 --=> [3] hx7 email generator [V.1]
 --=> [0] Exit the Program .
    """)

    anwser =  typingInput("""
hx7@scripts -->>> """)

    def hx7_Port_Grabber():
        import socket
        import time
        import pyfiglet
        import sys
        import os


        class app():
            # ==== system ==== #

            def typingPrint(text):
                for character in text:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.01)


            print("[+] ====== hx7 Script ====== [+]")
            time.sleep(0.7)
            print("[+] ====== Port Grabber ====== [+]")
            time.sleep(0.7)
            print("[+] ====== Made By: hx7 | hadixd ====== [+]")
            time.sleep(1)
            print("> 3")
            time.sleep(1)
            print("> 2")
            time.sleep(1)
            print("> 1")
            time.sleep(0.7) 
            print("> ------ | 10%")
            time.sleep(0.7)
            print("> ----------- | 20%")
            time.sleep(0.1)
            print("> ------------- | 23%")
            time.sleep(0.6)
            print("> ---------------- | 28%")
            print("> ------------------ | 30%")
            time.sleep(0.7)
            print("> ------------------------ | 50%")
            print("> ----------------------------- | 62%")
            print("> --------------------------------- | 69%")
            time.sleep(0.5)
            print("> ----------------------------------- | 70%")
            time.sleep(0.6)
            print("> ------------------------------------------ | 76%")
            print("> ---------------------------------------------- | 80%")
            time.sleep(0.7)
            print("> ------------------------------------------------------ | 90%")
            print("> ------------------------------------------------------------ | 100%")
            time.sleep(1)
            print("> Welcome 👋")
            time.sleep(0.7)
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(0.7)
            logo = '''
             _              _____                  _
            | |__   __  __ |___  |   ___   _   _  | |__     ___   _ __
            | '_ \  \ \/ /    / /   / __| | | | | | '_ \   / _ \ | '__|
            | | | |  >  <    / /   | (__  | |_| | | |_) | |  __/ | |
            |_| |_| /_/\_\  /_/     \___|  \__, | |_.__/   \___| |_|
                                           |___/

            '''
            typingPrint(logo)
            time.sleep(0.5)
            port = int(input("Enter Port : "))
            ts = socket.getservbyport(port)
            if port:
                print(ts)
            else:
                print("[!] This Port Not Found, Try Again !!")

        app()
        time.sleep(1.2)
        print("""
  [01] Return To Main Menu
        """)
        choose3 = input("""
hx7@scripts -->>> """)
        if choose3 == '1' or '02':
            os.system('cls' if os.name == 'nt' else 'clear')
            mainMenu()
        # end this app


    def hx7_Port_Grabber_by_name():
        import socket
        import time
        import sys

        def typingPrint_custom_1(text):
            for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.01)

        class app2():
        
            print("[+] ====== hx7 Script ====== [+]")
            time.sleep(0.7)
            print("[+] ====== Port Grabber By: [Port Name] ====== [+]")
            time.sleep(0.7)
            print("[+] ====== Made By: hx7 | hadixd ====== [+]")
            time.sleep(1)
            print("> 3")
            time.sleep(2)
            print("> 2")
            time.sleep(1)
            print("> 1")
            time.sleep(0.7)
            print("> ------ | 10%")
            time.sleep(0.7)
            print("> ----------- | 50%")
            time.sleep(1)
            print("> ---------------- | 100%")
            time.sleep(1)
            print("> Welcome 👋")
            time.sleep(0.7)
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(0.7)
            tkoplogo = '''
         _              _____                  _
        | |__   __  __ |___  |   ___   _   _  | |__     ___   _ __
        | '_ \  \ \/ /    / /   / __| | | | | | '_ \   / _ \ | '__|
        | | | |  >  <    / /   | (__  | |_| | | |_) | |  __/ | |
        |_| |_| /_/\_\  /_/     \___|  \__, | |_.__/   \___| |_|
                                       |___/

            '''
            typingPrint_custom_1(tkoplogo)
            print(' ')
            portname = input("> Enter Port Name : ")
            ftls = socket.getservbyname(portname)
            print(ftls)

        app2()
        time.sleep(1.2)
        print("""
  [01] Return To Main Menu
        """)
        choose2 = input("""
hx7@scripts -->>> """)
        if choose2 == '1' or '02':
            os.system('cls' if os.name == 'nt' else 'clear')
            mainMenu()
        # end this app

    def hx7_email_generator():
        import random
        import string

        def random_char(char_num):
           return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

        print("email: "+random_char(7)+"@gmail.com")

        print ("password: "+random_char(7) )
        time.sleep(1.2)
        print("""
  [01] Return To Main Menu
        """)
        choose = input("""
hx7@scripts -->>> """)
        if choose == '1' or '02':
            os.system('cls' if os.name == 'nt' else 'clear')
            mainMenu()
        # end this app

    if anwser == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        hx7_Port_Grabber()
    elif anwser == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        hx7_Port_Grabber_by_name()
    elif anwser == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        hx7_email_generator()
    elif anwser == '0':
        exit


ap()
mainMenu()