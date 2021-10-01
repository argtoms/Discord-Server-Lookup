"""

"""

import colorama
from colored import fg, attr
from colorama import Fore, Back, Style, init
import requests
from time import sleep
import os
import os.path
from requests.api import options
import sys
import webbrowser
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Discord Server Lookup | v1.0 | Developer: cutieQue")

def menu():
    print(f"""{Fore.LIGHTRED_EX}

░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░    ██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗    ██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝    ██║░░░░░██║░░██║██║░░██║█████═╝░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗    ██║░░░░░██║░░██║██║░░██║██╔═██╗░██║░░░██║██╔═══╝░
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║    ███████╗╚█████╔╝╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝    ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░
                                                                    {Fore.LIGHTCYAN_EX}Developed by - cutieQue
                                                                    https://discord.gg/xysmj9mHxV{Fore.RESET}{Fore.LIGHTYELLOW_EX}
    -------------------------------------------------------------------------
   | [1] - Start Server Lookup       [2] - Join Discord          [98] - Exit |    
    -------------------------------------------------------------------------
""")
menu()

option = int(input(f"{Fore.CYAN} [>] {Fore.RESET}"))


def fetch_data():
        menu()
if option == 1:
        sleep(1)
        ctypes.windll.kernel32.SetConsoleTitleW("Discord Server Lookup | v1.0 | Running Server Lookup! | Developer: cutieQue")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{Fore.LIGHTRED_EX}

░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░    ██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗██████╗░
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗    ██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝    ██║░░░░░██║░░██║██║░░██║█████═╝░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗    ██║░░░░░██║░░██║██║░░██║██╔═██╗░██║░░░██║██╔═══╝░
██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║    ███████╗╚█████╔╝╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝    ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░
                                                                    {Fore.LIGHTCYAN_EX}Developed by - cutieQue
                                                                    https://discord.gg/xysmj9mHxV{Fore.RESET}{Fore.LIGHTYELLOW_EX}
""")

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : input(f"\n{Fore.LIGHTYELLOW_EX} Enter Your Token. [>] ")
        }

        guildId = input(f"\n{Fore.LIGHTRED_EX} Enter Guild ID. [>] ")

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        print(f"""{Fore.LIGHTBLUE_EX}
 Guild/Server | Name > {response['name']} 
 Guild/Server | ID > {response['id']}
 Guild/Server | Icon URL > https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
 Guild/Server | Approxomate Amount of Members > {response['approximate_member_count']}
 Guild/Server | Owner > {owner['user']['username']}#{owner['user']['discriminator']} 
 Guild/Server | Owner ID > {response['owner_id']}
 Guild/Server | Region > {response['region']}
""")
        sleep(10)
        exit()

elif option == 2:
    print(f"{Fore.LIGHTGREEN_EX}Redirecting in 3 Seconds...")
    sleep(3)
    webbrowser.open_new('https://discord.gg/xysmj9mHxV')
    sleep(2)
    print(f"{Fore.RED}Bye!!")
    sleep(2)
    exit()
elif option == 98:
    sleep(1)
    print(f"{Fore.LIGHTGREEN_EX}Bye!")
    sleep(0.5)
    exit()
if __name__ == '__main__':
        fetch_data()