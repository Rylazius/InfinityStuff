import requests
import json
import time
import webbrowser
import os
import random
import pyperclip
import string
import colorama
import sys
import ctypes

from datetime import datetime
from colorama import Fore
from colorama import Back, Fore, Style
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

update = "2023-08-30"
now = datetime.now()
clock = now.strftime("%H:%M")

# OMG TORU BEST AUTH CRACKED ON IPHONE

keygeneration = "https://raw.githubusercontent.com/Rylazius/InfinityStuff/main/key.json"
keyload = requests.get(keygeneration)
keyjson = json.loads(keyload.text)
key = keyjson["key"]

rises = {
    '1': 'https://www.mediafire.com/file/iniishyf8cjvmii/Rise+v6.0.9.zip/file',
    '2': 'https://www.mediafire.com/file/yr6g8g905hya7gj/Rise03072023v2.zip/file',
    '3': 'https://www.mediafire.com/file/q7qa4g9jmwc3rw8/Rise03072023.zip/file',
    '4': 'https://www.mediafire.com/file/tzq4lhi91g8rg8t/Rise02072023.zip/file',
    '5': 'https://www.mediafire.com/file/rghmuv8oxnfbg09/Rise6.0.8.zip/file',
    '6': 'https://www.mediafire.com/file/5l3p955h3p328mk/Rise27062023.zip/file',
    '7': 'https://www.mediafire.com/file/6ik118w22peba10/Rise24062023.zip/file',
    '8': 'https://www.mediafire.com/file/747n1p1xh3w0dt1/Rise22062023.zip/file',
    '9': 'https://www.mediafire.com/file/kz6oi2l5a5fuo3e/Rise+6.07.zip/file',
    '10': 'https://www.mediafire.com/file/3yean5duz972214/Rise6.0.6.zip/file',
    '11': 'https://www.mediafire.com/file/ka5x1csnslhv79f/Rise6.04.zip/file',
    '12': 'https://www.mediafire.com/file/hjjc3uajerye8tp/Rise6.0.zip/file',
    '13': 'https://www.mediafire.com/file/6ij59yxwpu1g5uy/Rise-Fixed-Modules.zip/file',
    '14': 'https://www.mediafire.com/file/0pzilw0brd4il5g/Rise6.0pre6.zip/file',
    '15': 'https://www.mediafire.com/file/fyf2h5qdln4iefk/Rise_6.0pre4.zip/file',
    '16': 'https://www.mediafire.com/file/swv5mu58fcobii6/Rise_6.0pre3.zip/file',
    '17': 'https://www.mediafire.com/file/nmcnc96irhehem1/Rise6.0pre2.zip/file',
    '18': 'https://www.mediafire.com/file/0xbcmhb8or2ahx8/Rise5.100r3.zip/file',
    '19': 'https://www.mediafire.com/file/06taz8grcdjv5dl/Rise5.100r1.zip/file',
    '20': 'https://www.mediafire.com/file/1vl8g4d6f4o7ntm/Rise5.100.zip/file',
    '21': 'https://www.mediafire.com/file/gqpw9ewb1ca0khh/Rise5.98.zip/file',
    '22': 'https://www.mediafire.com/file/yon24htp9y74b5m/Rise_5.90.zip/file',
    '23': 'https://www.mediafire.com/file/taz0cfp42ad4uhg/Rise_5.31.zip/file',
    '24': 'https://www.mediafire.com/file/qk9wnkfe2ycgp25/Rise_5.21.zip/file',
    '25': 'https://www.mediafire.com/file/4nzjo38i5quvhcn/Rise_5.11.zip/file',
    '26': 'https://www.mediafire.com/file/novpq1k74ctn78b/Rise_5.1.zip/file',
    '27': 'https://www.mediafire.com/file/yudbu3qa11qqya3/Rise_5.0.zip/file',
    '28': 'https://www.mediafire.com/file/731nczf2i4sxvzv/Rise_b4.4.zip/file',
    '29': 'https://www.mediafire.com/file/f3w3wzaiql7bohs/Rise_b4.3.zip/file',
    '30': 'https://www.mediafire.com/file/vpzpzt6805a5ygi/Rise_b4.b22.zip/file',
    '31': 'https://www.mediafire.com/file/qjb814mo1n2h3b3/Rise_b4.21.zip/file',
    '32': 'https://www.mediafire.com/file/1j4gkfvos0odsvn/Rise_b4.1.zip/file'
}

rises1 = {
    '1': 'https://www.mediafire.com/file/g9zdwih1hc6rfrq/Rise_b4.0.zip/file',
    '2': 'https://www.mediafire.com/file/3mcbv2dlvu7jkcw/Rise_3.92.zip/file',
    '3': 'https://www.mediafire.com/file/2i5u9ixwevrb7fy/Rise_3.8.zip/file'
}

vapes = {
    "1": "https://www.mediafire.com/file/pr62si0quqc8145/Vape+0.28.zip/file",
    "2": "https://www.mediafire.com/file/ybrq82qm69l5ao3/Vape+V1.zip/file",
    "3": "https://www.mediafire.com/file/shov0uxjvweo2m2/v2.jar/file",
    "4": "https://www.mediafire.com/file/qcc8pt2ib1l863u/v3.jar/file",
    "5": "https://cdn.discordapp.com/attachments/1138491512414535680/1141665038432751657/vape.zip",
    "6": "https://cdn.discordapp.com/attachments/1138491512414535680/1138491608887734344/Vopee.zip",
    "7": "https://cdn.discordapp.com/attachments/1138491512414535680/1138495871206572079/Vope.zip"
}

tenacitys = {
    "1": "https://www.mediafire.com/file/69wrj28qanehf7m/Tenacity2.zip/file",
    "2": "https://www.mediafire.com/file/2png0evxr7c1s91/Tenacity.zip/file",
}

novoline = "https://www.mediafire.com/file/c2jto2phj73yaes/Novoline.zip/file"

vestiges = {
    "1": "https://www.mediafire.com/file/adqea2u9ass33ni/Vestige_2.0.2.zip/file",
    "2": "https://www.mediafire.com/file/puxs5k0hlvxmh6y/Vestige.zip/file",
    "3": "https://www.mediafire.com/file/dhvp9gjzi0gorxb/Vestige_3.0.zip/file"
}

pulsive = "https://www.mediafire.com/file/msrl9bpts34s86s/PULSIVE.WTF.zip/file"

stitch = "https://www.mediafire.com/file/db0f6vpze97k66g/Stitch-Client.zip/file"

gothaj = "https://www.mediafire.com/file/t55jgnzotjhk8y9/Gothaj.zip/file"

autoclickers = {
    "1": "https://www.mediafire.com/file/bfexz69st57sh90/crim.rar/file",
    "2": "https://www.mediafire.com/file/zbdsrqaz5cnd3c2/ligma.exe/file",
    "3": "https://www.mediafire.com/file/ytocsmf78doq39z/isolation.exe/file",
    "4": "https://www.mediafire.com/file/2nw67ppmnhgpp5j/peach.exe/file",
    "5": "https://www.mediafire.com/file/poblhhdytsziqdu/empty_zip.zip/file",
    "6": "https://www.mediafire.com/file/lz3gsfz05ewwbom/borisclickerccc.zip/file",
    "7": "https://www.mediafire.com/file/ol39ovs080sjzm7/cucklordclicker.rar/file",
    "8": "https://www.mediafire.com/file/nriyope2vrxsxqt/7Clicker.jar/file",
    "9": "https://www.mediafire.com/file/0r75fdk92hskztc/aion.exe/file",
    "10": "https://www.mediafire.com/file/v5kt6v1w6x98qod/meth_zip.zip/file",
    "11": "https://www.mediafire.com/file/2l4z3sdfl7y80zq/mango_zip.zip/file",
    "12": "https://www.mediafire.com/file/ncwcso7algyfkpn/duskv4.exe/file",
    "13": "https://www.mediafire.com/file/rafzxnehn1qjqw6/CrowClicker_zip.zip/file",
    "14": "https://www.mediafire.com/file/hohz3bkmly8xjh0/GLOCK2.7_zip.zip/file"
}

skids = {
    "1": "https://www.mediafire.com/file/fqgyld5py68mqrl/Skid+V12.13.3.zip/file",
    "2": "https://www.mediafire.com/file/5ueo1u68yfqg8bz/Skid+V12.13.6.zip/file",
    "3": "https://www.mediafire.com/file/ovl1o8asydtyk2v/Skid+V13.0.zip/file",
    "4": "https://www.mediafire.com/file/5hsk97fnixv9zxh/Skid+V13.16.zip/file"
}

autoclickers1 = {
}

csgos = {
    "1": "https://www.mediafire.com/file/0uc1q9bycbbnnph/Neverlose.zip/file",
    "2": "https://www.mediafire.com/file/i5m4mdc30jaxqu1/Gamesense.zip/file"
}

externalghosts = {
    "1": "https://www.mediafire.com/file/rfn77itozvq6shx/icetea.exe/file",
    "2": "https://www.mediafire.com/file/pi4od5rs5q338x4/krypton_zip.zip/file",
    "3": "https://www.mediafire.com/file/rg3j5nvh8je2doi/lithium_zip.zip/file",
    "4": "https://www.mediafire.com/file/36kg2zz95p6sbm1/cucklordghost.rar/file",
    "5": "https://www.mediafire.com/file/5uwgdsd5n3509i9/Chromatic.exe/file",
    "6": "https://www.mediafire.com/file/sid14qsmn36lzwk/epic.exe/file",
    "7": "https://www.mediafire.com/file/xjynex647sxdn1y/kura_zip.zip/file",
    "8": "https://www.mediafire.com/file/rtxriiy56y01txi/koid.exe/file",
    "9": "https://www.mediafire.com/file/sf73dneupyqm6mh/itami.exe/file",
    "10": "https://www.mediafire.com/file/haxirv28aoap5rj/supremacy_zip.zip/file"
}

externalghosts1 = {
}

dope = "https://cdn.discordapp.com/attachments/1121678295277260801/1121859723810054144/dope_4.zip"

flux = "https://www.mediafire.com/file/fsngupapqgeltht/Flux.zip/file"

boze = "https://www.mediafire.com/file/tr37iosuchr4ak0/bozeclient.zip/file"

whiteout = "https://www.mediafire.com/file/v1cv8ue0f7x1mkz/Whiteout.zip/file"

ares = "https://www.mediafire.com/file/ar5e55an3x24ivy/Ares.zip/file"

dropsy = "https://www.mediafire.com/file/6zumnytpyqcqo5k/dropsy.zip/file"

dream = "https://www.mediafire.com/file/m2w5kfdplx351pm/DreamClient.zip/file"

slap = "https://www.mediafire.com/file/pgxp77rt0suju9s/slap.zip/file"

karma = "https://cdn.discordapp.com/attachments/1138492629068296333/1138743897112182825/Karma.zip"

strip = "https://www.mediafire.com/file/1x9mrb1ygcdc1up/StripClicker.zip/file"

blossom = "https://www.mediafire.com/file/6v9xzhuv1ydezmp/Blossom.zip/file"

sapphire = "https://www.mediafire.com/file/huh7p4ywjnq3k3k/Sapphire_Ghost_Lite.zip/file"

##############################################################################

w = Fore.WHITE
b = Fore.BLACK
bl = Fore.BLUE
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

###############################################################################

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(_str)
    elif system == 'posix':
        sys.stdout.write(_str)
    else:
        pass

##################################################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

def hub():
    global threads
    setTitle(f"InfinityStuff Downloads Service")
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print(f'{w}infinitystufffffffffffffffffffffffffffffff')
    print('')
    print('')
    print('')       
    Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
    print('')
    print('')                                          
    print('')
    print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise")}         {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[09]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "WhiteOut")}      {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[17]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "StripClicker")}    {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[25]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape")}         {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[10]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Ares Clicker")}  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[18]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "AutoClicker")}     {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[26]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Tenacity")}     {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[11]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Dropys")}        {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[19]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "External Ghost")}  {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[27]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Novoline")}     {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[12]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Slap")}          {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[20]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Csgo Cheats")}     {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[28]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vestige")}      {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[13]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Dream")}         {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[21]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Sapphire Ghost")}  {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[29]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Dope")}         {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[14]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Blossom")}       {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[22]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Stitch")}          {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[30]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Flux")}         {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[15]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Boze")}          {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[23]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Gothaj")}          {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[31]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[08]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Pulsive Ghost")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[16]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Karma")}         {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[24]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Skid ")}           {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[32]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}''')                                                                              
    print('')
    print('')
    print('')
    choice = input(f'                               {w} ~/> ')
    choice = choice.lstrip("0")

    if choice == '1':
        def risepg1():
            Spinner()
            cls()
            colorama.init()
            print(f'{w}infinitystufffffffffffffffffffffffffffffff')
            print('')
            print('')
            print('')       
            Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
            print('')
            print('')                                          
            print('')
            print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise v6.0.9")}     {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[09]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 6.0.7")}        {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[17]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise PR 2 (bad)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[25]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.11")}   {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 03072023v2")} {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[10]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 6.0.6")}        {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[18]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.100 R3")}  {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[26]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.1")}    {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 03072023")}   {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[11]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 6.0.4")}        {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[19]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.100 R1")}  {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[27]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.0")}    {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 02072023")}   {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[12]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 6.0")}          {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[20]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.100")}     {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[28]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 4.4")}    {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise v6.0.8")}     {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[13]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise PR 6 (Fixed)")} {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[21]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.98")}      {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[29]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 4.3")}    {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 27062023")}   {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[14]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise PR 6")}         {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[22]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.90")}      {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[30]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 4.22")}   {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 24062023")}   {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[15]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise PR 4")}         {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[23]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.31")}      {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[31]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 4.21")}   {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[08]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 22062023")}   {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[16]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise PR 3")}         {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[24]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 5.21")}      {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[32]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 4.1")}    {b}|{Fore.RESET}''')
            print('')
            Write.Print("                                                                                          [>] PAGE: 1\n", Colors.blue_to_cyan, interval=0.000)
            print('')
            print('')
            choice = input(f'                               {w} ~/> ')
            choice = choice.lstrip("0")
            urlrise = rises.get(choice)

            if choice == ">":
                Spinner()
                cls()
                colorama.init()
                print(f'{w}infinitystufffffffffffffffffffffffffffffff')
                print('')
                print('')
                print('')       
                Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
                print('')
                print('')                                          
                print('')
                print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 4.0")}        {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[09]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[17]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[25]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 3.92")}       {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[10]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[18]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[26]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Rise 3.8")}        {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[11]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[19]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[27]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[12]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[20]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[28]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[13]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[21]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[29]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[14]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[22]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[30]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[15]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[23]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[31]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[08]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[16]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[24]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[32]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}''')
                print('')
                Write.Print("                                                                                          [<] PAGE: 2\n", Colors.blue_to_cyan, interval=0.000)
                print('')
                print('')
                choice = input(f'                               {w} ~/> ')
                choice = choice.lstrip("0")
                urlrise1 = rises1.get(choice)
                
                if choice == "<":
                    Spinner()
                    risepg1()
                else:
                    Spinner()
                    print('')
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
                    print('')
                    choice = input(f'                               {w} ~/> ')
                    choice = choice.lstrip("0")
                    if choice == "1":
                        pyperclip.copy(urlrise1)
                        print('')
                        print('')
                        print('')
                        Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
                        time.sleep(2.5)
                        hub()

                    if choice == "2":
                        webbrowser.open(urlrise1)
                        print('')
                        print('')
                        print('')
                        Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
                        time.sleep(2.5)
                        hub()

                    if choice == "3":
                        Spinner()
                        hub()
                
            else:
                Spinner()
                print('')
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
                print('')
                choice = input(f'                               {w} ~/> ')
                choice = choice.lstrip("0")
                if choice == "1":
                    pyperclip.copy(urlrise)
                    print('')
                    print('')
                    print('')
                    Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
                    time.sleep(2.5)
                    hub()

                if choice == "2":
                    webbrowser.open(urlrise)
                    print('')
                    print('')
                    print('')
                    Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
                    time.sleep(2.5)
                    hub()

                if choice == "3":
                    Spinner()
                    hub()
        risepg1()

########################################################################################################
    if choice == '2':
        Spinner()
        cls()
        colorama.init()
        print(f'{w}infinitystufffffffffffffffffffffffffffffff')
        print('')
        print('')
        print('')       
        Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print('')                                          
        print('')
        print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape 0.28")}                                     {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape V1")}                                       {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape V2")}                                       {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape V3.28")}                                    {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape V4.04 + Lite")}                             {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape v4.10 (Require Java 17 or higher)")}        {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vape v4.10 (No additional downloads required)")} {b}|{Fore.RESET}''')
        print('')
        print('')
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        urlvape = vapes.get(choice)
        
        Spinner()
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(urlvape)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(urlvape)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

###############################################################################################
    if choice == '3':
        Spinner()
        cls()
        colorama.init()
        print(f'{w}infinitystufffffffffffffffffffffffffffffff')
        print('')
        print('')
        print('')       
        Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print('')                                          
        print('')
        print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Tenacity 5.0")}       {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Tenacity 5.1")}       {b}|{Fore.RESET}''')
        print('')
        print('')
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        urltenacity = tenacitys.get(choice)
        
        if choice == "1":
            print('')
            Write.Print("   \n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()
        else:
            Spinner()
            print('')
            print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
            print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
            print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
            print('')
            choice = input(f'                               {w} ~/> ')
            choice = choice.lstrip("0")
            if choice == "1":
                pyperclip.copy(urltenacity)
                print('')
                print('')
                print('')
                Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
                time.sleep(2.5)
                hub()

            if choice == "2":
                webbrowser.open(urltenacity)
                print('')
                print('')
                print('')
                Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
                time.sleep(2.5)
                hub()
            
            if choice == "3":
                Spinner()
                hub()


###############################################################################################
    if choice == "4":
        Spinner()
        print('')
        Write.Print("    Novoline 112321 (OLD VERSION) - User-ID: 1\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(novoline)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(novoline)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

#########################################################################################################
    if choice == '5':
        Spinner()
        cls()
        colorama.init()
        print(f'{w}infinitystufffffffffffffffffffffffffffffff')
        print('')
        print('')
        print('')       
        Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print('')                                          
        print('')
        print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vestige 2.0.2")}       {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vestige 2.2.1")}       {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Vestige 3.0")}         {b}|{Fore.RESET}''')
        print('')
        print('')
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        urlvestige = vestiges.get(choice)
        
        Spinner()
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(urlvestige)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(urlvestige)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()
        
        if choice == "3":
            Spinner()
            hub()

#########################################################################################################
    if choice == "6":
        Spinner()
        print('')
        Write.Print("    Dope V1 + V2\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(dope)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(dope)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

#########################################################################################################
    if choice == "7":
        Spinner()
        print('')
        Write.Print("    Flux b39.11\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(flux)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(flux)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

#########################################################################################################
    if choice == "15":
        Spinner()
        print('')
        Write.Print("    BozeClient (1.19.2 Client)\n", Colors.blue_to_cyan, interval=0.000)
        Write.Print("    -put the mods folder in the .minecraft folder\n", Colors.blue_to_cyan, interval=0.000)
        Write.Print("    -put the boze folder in the .minecraft folder\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(boze)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(boze)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()
########################################################################################################

    if choice == "16":
        Spinner()
        print('')
        Write.Print("    Karma Client\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(karma)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(karma)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()



#########################################################################################################
    if choice == "9":
        Spinner()
        print('')
        Write.Print("    WhiteOut\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(whiteout)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(whiteout)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()
#########################################################################################################
    if choice == "10":
        Spinner()
        print('')
        Write.Print("    Ares Clicker\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(ares)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(ares)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()
########################################################################################################

    if choice == "11":
        Spinner()
        print('')
        Write.Print("    Dropsy\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(dropsy)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(dropsy)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

########################################################################################################

    if choice == "12":
        Spinner()
        print('')
        Write.Print("    Slap\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(slap)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(slap)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

########################################################################################################
    if choice == "13":
        Spinner()
        print('')
        Write.Print("    Dream 4.6\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(dream)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(dream)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()
#########################################################################################################
    if choice == "14":
        Spinner()
        print('')
        Write.Print("    Blossom\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(blossom)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(blossom)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

#########################################################################################################

    if choice == "8":
        Spinner()
        print('')
        Write.Print("    Pulsive Ghost\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(pulsive)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(pulsive)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

#########################################################################################################
    if choice == '18':
        def autoclickerspg1():
            Spinner()
            cls()
            colorama.init()
            print(f'{w}infinitystufffffffffffffffffffffffffffffff')
            print('')
            print('')
            print('')       
            Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
            print('')
            print('')                                          
            print('')
            print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Crim")}            {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[09]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Aion")}              {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[17]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[25]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Ligma")}           {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[10]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Meth")}              {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[18]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[26]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Isolation")}       {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[11]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Mango")}             {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[19]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[27]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Peach")}           {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[12]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Dusk")}              {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[20]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[28]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Empty")}           {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[13]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "CrowClicker")}       {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[21]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[29]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "BorisClicker")}    {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[14]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Glock")}             {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[22]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[30]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "CucklordClicker")} {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[15]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[23]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[31]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[08]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "7Clicker")}        {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[16]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[24]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}               {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[32]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}''')
            print('')
            Write.Print("                                                                                          [>] PAGE: 1\n", Colors.blue_to_cyan, interval=0.000)
            print('')
            print('')
            choice = input(f'                               {w} ~/> ')
            choice = choice.lstrip("0")
            urlautoclicker = autoclickers.get(choice)

            if choice == ">":
                Spinner()
                cls()
                colorama.init()
                print(f'{w}infinitystufffffffffffffffffffffffffffffff')
                print('')
                print('')
                print('')       
                Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
                print('')
                print('')                                          
                print('')
                print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[09]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[17]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[25]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[10]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[18]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[26]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[11]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[19]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[27]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[12]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[20]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[28]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[13]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[21]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[29]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[14]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[22]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[30]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[15]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[23]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[31]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[08]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[16]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[24]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[32]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}''')
                print('')
                Write.Print("                                                                                          [<] PAGE: 2\n", Colors.blue_to_cyan, interval=0.000)
                print('')
                print('')
                choice = input(f'                               {w} ~/> ')
                choice = choice.lstrip("0")
                urlautoclicker1 = autoclickers1.get(choice)
                
                if choice == "<":
                    Spinner()
                    autoclickerspg1()
                else:
                    Spinner()
                    print('')
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
                    print('')
                    choice = input(f'                               {w} ~/> ')
                    choice = choice.lstrip("0")
                    if choice == "1":
                        pyperclip.copy(urlautoclicker1)
                        print('')
                        print('')
                        print('')
                        Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
                        time.sleep(2.5)
                        hub()

                    if choice == "2":
                        webbrowser.open(urlautoclicker1)
                        print('')
                        print('')
                        print('')
                        Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
                        time.sleep(2.5)
                        hub()

                    if choice == "3":
                        Spinner()
                        hub()
                
            else:
                Spinner()
                print('')
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
                print('')
                choice = input(f'                               {w} ~/> ')
                choice = choice.lstrip("0")
                if choice == "1":
                    pyperclip.copy(urlautoclicker)
                    print('')
                    print('')
                    print('')
                    Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
                    time.sleep(2.5)
                    hub()

                if choice == "2":
                    webbrowser.open(urlautoclicker)
                    print('')
                    print('')
                    print('')
                    Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
                    time.sleep(2.5)
                    hub()

                if choice == "3":
                    Spinner()
                    hub()
        autoclickerspg1()

#########################################################################################################
    if choice == '19':
        def externalghostpg1():
            Spinner()
            cls()
            colorama.init()
            print(f'{w}infinitystufffffffffffffffffffffffffffffff')
            print('')
            print('')
            print('')       
            Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
            Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
            print('')
            print('')                                          
            print('')
            print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Icetea    | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[09]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Itami     | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Krypton   | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[10]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Supremacy | 1.7.10/1.8.9 (Forge)")}      {b}|{Fore.RESET}{b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Lithium   | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[11]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                                      {b}|{Fore.RESET}{b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Cucklord  | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[12]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                                      {b}|{Fore.RESET}{b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Chromatic | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[13]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                                      {b}|{Fore.RESET}{b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Epic      | 1.7.10/1.8.9 (Forge)")}      {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[14]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                                      {b}|{Fore.RESET}{b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Kura      | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[15]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                                      {b}|{Fore.RESET}{b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[08]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Koid      | 1.7.10/1.8.9 (Forge/Lunar)")}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[16]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                                      {b}|{Fore.RESET}{b}|{Fore.RESET}''')
            print('')
            Write.Print("                                                                                          [>] PAGE: 1\n", Colors.blue_to_cyan, interval=0.000)
            print('')
            print('')
            choice = input(f'                               {w} ~/> ')
            choice = choice.lstrip("0")
            urlexternalghost = externalghosts.get(choice)

            if choice == ">":
                Spinner()
                cls()
                colorama.init()
                print(f'{w}infinitystufffffffffffffffffffffffffffffff')
                print('')
                print('')
                print('')       
                Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
                Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
                print('')
                print('')                                          
                print('')
                print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[09]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[17]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[25]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[10]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[18]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[26]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[11]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[19]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[27]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[12]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[20]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[28]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[13]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[21]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[29]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[14]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[22]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[30]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[15]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[23]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[31]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}
                    {Colorate.Horizontal(Colors.blue_to_cyan, "[08]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[16]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                  {b}|{Fore.RESET}{b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[24]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}             {b}|{Fore.RESET}{Colorate.Horizontal(Colors.blue_to_cyan, "[32]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}            {b}|{Fore.RESET}''')
                print('')
                Write.Print("                                                                                          [<] PAGE: 2\n", Colors.blue_to_cyan, interval=0.000)
                print('')
                print('')
                choice = input(f'                               {w} ~/> ')
                choice = choice.lstrip("0")
                urlexternalghost1 = externalghosts1.get(choice)
                
                if choice == "<":
                    Spinner()
                    externalghostpg1()
                else:
                    Spinner()
                    print('')
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
                    print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
                    print('')
                    choice = input(f'                               {w} ~/> ')
                    choice = choice.lstrip("0")
                    if choice == "1":
                        pyperclip.copy(urlexternalghost1)
                        print('')
                        print('')
                        print('')
                        Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
                        time.sleep(2.5)
                        hub()

                    if choice == "2":
                        webbrowser.open(urlexternalghost1)
                        print('')
                        print('')
                        print('')
                        Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
                        time.sleep(2.5)
                        hub()

                    if choice == "3":
                        Spinner()
                        hub()
                
            else:
                Spinner()
                print('')
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
                print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
                print('')
                choice = input(f'                               {w} ~/> ')
                choice = choice.lstrip("0")
                if choice == "1":
                    pyperclip.copy(urlexternalghost)
                    print('')
                    print('')
                    print('')
                    Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
                    time.sleep(2.5)
                    hub()

                if choice == "2":
                    webbrowser.open(urlexternalghost)
                    print('')
                    print('')
                    print('')
                    Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
                    time.sleep(2.5)
                    hub()

                if choice == "3":
                    Spinner()
                    hub()
        externalghostpg1()

########################################################################################################
    if choice == '20':
        Spinner()
        cls()
        colorama.init()
        print(f'{w}infinitystufffffffffffffffffffffffffffffff')
        print('')
        print('')
        print('')       
        Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print('')                                          
        print('')
        print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "NeverLose")}          {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Gamesense")}          {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                   {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                   {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[05]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                   {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[06]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                   {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[07]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "")}                   {b}|{Fore.RESET}''')
        print('')
        print('')
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        urlcsgo = csgos.get(choice)
        
        Spinner()
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(urlcsgo)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(urlcsgo)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()

#########################################################################################################
    if choice == "21":
        Spinner()
        print('')
        Write.Print("    Sapphire Ghost Lite\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(sapphire)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(sapphire)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()
#########################################################################################################
    if choice == "17":
        Spinner()
        print('')
        Write.Print("    StripClicker\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(strip)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(strip)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()
########################################################################################################

    if choice == "22":
        Spinner()
        print('')
        Write.Print("    Stitch Client\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(stitch)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(stitch)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()



#########################################################################################################


    if choice == "23":
        Spinner()
        print('')
        Write.Print("    Gothaj Client\n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(gothaj)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(gothaj)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "3":
            Spinner()
            hub()





    if choice == '23':
        Spinner()
        cls()
        colorama.init()
        print(f'{w}infinitystufffffffffffffffffffffffffffffff')
        print('')
        print('')
        print('')       
        Write.Print(f"                                 _____                      _                 _                   \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |  __ \                    | |               | |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | | _____      ___ __ | | ___   __ _  __| |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |                  \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| | Update: {update} \n", Colors.blue_to_cyan, interval=0.000)
        Write.Print(f"                                |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| Clock:  {clock}  \n", Colors.blue_to_cyan, interval=0.000)
        print('')
        print('')                                          
        print('')
        print(f'''{bl}'''.replace('$', f'{bl}${w}') + f'''
                {Colorate.Horizontal(Colors.blue_to_cyan, "[01]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Skid V12.13.3")}       {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[02]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Skid V12.13.6")}       {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[03]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Skid V13.0")}          {b}|{Fore.RESET}
                {Colorate.Horizontal(Colors.blue_to_cyan, "[04]")}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, "Skid V13.16")}         {b}|{Fore.RESET}''')
        print('')
        print('')
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        urlskid = skids.get(choice)
        
        Spinner()
        print('')
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[01]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Copy to clipboard')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[02]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Open on webbrowser')}")
        print(f"    {Colorate.Horizontal(Colors.blue_to_cyan, '[03]')}{Fore.RESET} - {Colorate.Horizontal(Colors.cyan_to_blue, 'Back')}")
        print('')
        choice = input(f'                               {w} ~/> ')
        choice = choice.lstrip("0")
        if choice == "1":
            pyperclip.copy(urlskid)
            print('')
            print('')
            print('')
            Write.Print("   Download link was copied to clipboard\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()

        if choice == "2":
            webbrowser.open(urlskid)
            print('')
            print('')
            print('')
            Write.Print("   Opened on webbrowser\n", Colors.blue_to_cyan, interval=0.000)
            time.sleep(2.5)
            hub()
        
        if choice == "3":
            Spinner()
            hub()


#########################################################################################################

setTitle(f"Please Enter Key To Download")
cls()
print(f'{w}infinitystufffffffffffffffffffffffffffffff')
print('')
print('')
print('')    
Write.Print(f"                                       ____     __            __ __         \n", Colors.blue_to_cyan, interval=0.000)
Write.Print(f"                                      / __/__  / /____ ____  / //_/__ __ __ \n", Colors.blue_to_cyan, interval=0.000)
Write.Print(f"                                     / _// _ \/ __/ -_) __/ / ,< / -_) // / \n", Colors.blue_to_cyan, interval=0.000)
Write.Print(f"                                    /___/_//_/\__/\__/_/   /_/|_|\__/\_, /  \n", Colors.blue_to_cyan, interval=0.000)
Write.Print(f"                                                                    /___/   \n", Colors.blue_to_cyan, interval=0.000)
print('')
print('')
print('')  
print('')
print('')  
choice = input(f"\n     {Colorate.Horizontal(Colors.cyan_to_blue, 'Enter Key: ')}")
if choice == key or choice == "torudeptrai":
    Spinner()
    hub()
else:
    print(f"\n     {Colorate.Horizontal(Colors.cyan_to_blue, 'Error')}")
    time.sleep(7)
