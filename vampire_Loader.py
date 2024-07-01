import discord
from discord.ext import commands
from pystyle import Colors, Colorate
import os
import time
import colorama
from colorama import Fore, Back, Style
## @Vampire 2024 - 204
Key = "Trial_app"

vampire = commands.Bot(command_prefix=";", intents=discord.Intents.all())

## Load UserName



def main():
    os.system("cls & title - Vampire - Trial - v1.0 -") 
    print(Colorate.Horizontal(Colors.red_to_purple, """
                     $$\    $$\                                  $$\                     
                     $$ |   $$ |                                 \__|                    
                     $$ |   $$ |$$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$\  $$$$$$\   $$$$$$\  
                     \$$\  $$  |\____$$\ $$  _$$  _$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ 
                      \$$\$$  / $$$$$$$ |$$ / $$ / $$ |$$ /  $$ |$$ |$$ |  \__|$$$$$$$$ |
                       \$$$  / $$  __$$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$ |      $$   ____|
                        \$  /  \$$$$$$$ |$$ | $$ | $$ |$$$$$$$  |$$ |$$ |      \$$$$$$$\ 
                         \_/    \_______|\__| \__| \__|$$  ____/ \__|\__|       \_______|
                                                       $$ |                              
                                                       $$ |                              
                                                       \__|            
------------------------------------------------------------------------------------------------------------------------
                              Make By Rain                 ┃v1┃         https://github.com/Rain436/Vampire                        
------------------------------------------------------------------------------------------------------------------------                    
""", 1))
    
    print(Colorate.Horizontal(Colors.red_to_purple, f"                      1 › Delete Channels                                      2 › Create Channels", 1))
    print(Colorate.Horizontal(Colors.red_to_purple, f"                      3 › Mass Kick                                            4 › Mass Ban", 1))
    print(Colorate.Horizontal(Colors.red_to_purple, f"                      5 › Server User DM Spammer                               6 › Rename Guild", 1))
    print(Colorate.Horizontal(Colors.red_to_purple, f"                      7 › Webhook Create Spammer                               8 › Channel Spammer", 1))
    print(Colorate.Horizontal(Colors.red_to_purple, f"                      9 › Console Logger Spammer                               10 › Leave Vampire Robot", 1))
    pass
    vmpir = input(f"{Fore.RED}Vampire@menu/: ")

    if vmpir == "1":
        os.system("python tool_data\channeldeleter.py")
        os.system("pause")

with open('account_data\config.json') as f:
    username = f.read().strip()
## Loaded Message
print(Colorate.Horizontal(Colors.red_to_purple, f"Loaded Username", 1))
print(Colorate.Horizontal(Colors.red_to_purple, f"Welcome Back! {username}", 1))

## Load Premium
print(Colorate.Horizontal(Colors.red_to_purple, f"Loading Premium Checking...", 1))
time.sleep(2)
## Loaded Message


print(Colorate.Horizontal(Colors.red_to_purple, f"Loading Key.....", 1))
## Key sample - Key038fadfukc910 - nekokkka93KEt - Minenenekoa947fedeaf
time.sleep(3)
print(Colorate.Horizontal(Colors.red_to_purple, f"Found Key! {Key}", 1))
main()