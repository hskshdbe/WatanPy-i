import requests,os
#BOBO = requests.get('https://t.me/test_watan/2').text
#if "TT" in BOBO:
#    os.system('clear')
#else:
#    exit('\x1b[1;33m Dev : Watan├──➤ Stoped Tool ')
#— — — — — — — — — — — — —
import webbrowser as WK
url = "https://t.me/sx_sk"
import sys
from threading import Thread as WTN
try: 
    from instagramtolle import GMAIL,instagram
except ImportError:
    os.system("pip install instagramtolle==0.3")
try:
    import requests
except ImportError:
    os.system("pip install requests")
#— — — — — — — — — — — — —
idf = input("ID > : ")
tokf = input("Token > : ")
#— — — — — — — — — — — — —
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
W = "\033[1;37m"  # White
ge, be, gi, bi = 0, 0, 0, 0
#— — — — — — — — — — — — —
def info(email):
    global idf,tokf
    user=email.split("@")[0]
    if "@"not in email:email=email+"@gmail.com"
    try:
        a=instagram.info(user)
        data=a.get("data")
        id_t=data.get("id")
        nm=data.get("full_name")
        prv=data.get("is_private")
        pos=data.get("post")
        fol=data.get("followers")
        folg=data.get("following")
        prpg='@WatanPy'
        tlg=str(f''' 
• Hi Available Instagram ✅
— — — — — — — — — — — — —
• Gmail : {email}
• Reset : {instagram.Reset(user).get("data").get("reset")}
• Name : {nm}
• UserName : {user}
• Following : {folg}
• Followers : {fol}
• Id  : {id_t}
• Private : {prv}
• PoSt : {pos}
• DaTe : {instagram.GetData(id_t).get("message").get("data")}
• ProgRmaer : {prpg} • @Sx_Sk
— — — — — — — — — — — — —
        ''')
    except:
        tlg=str(f''' 
• Hi Available Instagram ✅
— — — — — — — — — — — — —
• Gmail : {email}
• Reset : {instagram.Reset(user).get("data").get("reset")}
• UserName : {user}
• ProgRmaer : {prpg} • @Sx_Sk
— — — — — — — — — — — — —
''')

    requests.post(f"https://api.telegram.org/bot{tokf}/sendMessage?chat_id={idf}&text=" + str(tlg))
#— — — — — — — — — — — — —
def ch(email):
    global ge, be, gi, bi
    try:
        b = instagram.CheckEmail(email).get("data", {}).get("status", False)
        if b:
            gi += 1
            c = GMAIL.CheckEmail(email).get("data", {}).get("status", False)
            if c:
                ge += 1
                info(email)
            else:
                be += 1
        else:
            bi += 1                    
        os.system('clear')
        sys.stdout.write(f'\r < {G}Hits: {W}{ge}{R} | Bad IN: {W}{bi}{Y} | Bad EM: {W}{be}{Bl} | Good IN: {W}{gi} >  ')
        sys.stdout.flush()    
    except:
        print("\n⚠️ تأكد من تشغيل VPN وحاول مجددًا.")
#— — — — — — — — — — — — —
def T1():
    while True:
        try:
            a = instagram.generateUsername2011()
            user = a["data"]["username"]
            if user and "None" not in user:
                ch(user + "@gmail.com")
        except:
            continue
#— — — — — — — — — — — — —
def T2():
    while True:
        try:
            a = instagram.generateUsername2012()
            user = a["data"]["username"]
            if user and "None" not in user:
                ch(user + "@gmail.com")
        except:
            continue
#— — — — — — — — — — — — —
def T3():
    while True:
        try:
            a = instagram.generateUsername2013()
            user = a["data"]["username"]
            if user and "None" not in user:
                ch(user + "@gmail.com")
        except:
            continue
#— — — — — — — — — — — — —
def T4():
    while True:
        try:
            a = instagram.generateUsername2013()
            user = a["data"]["username"]
            followers = a.get("data", {}).get("follower_count", 0)
            if user and "None" not in user and followers > 25:
                ch(user + "@gmail.com")
        except:
            continue
#— — — — — — — — — — — — —
def Res():
	from instagramtolle import instagram
	user = input(' - Enter User Or Email : ')
	a = instagram.Reset(user)
	reset_status = a.get('data', {}).get('reset', False)
	banned_status = a.get('data', {}).get('banned', False)
	if banned_status:
	    print(" - Account is banned (مبند)")
	elif reset_status:
	    print(" - Good Reset ")
	else:
	    print(" - Bad Reset ")    
#— — — — — — — — — — — — —
from concurrent.futures import ThreadPoolExecutor
import os

def admin_gmail(name):
    try:
        with open(name, 'r') as file:
            lines = file.read().splitlines()
    except:
        os.system('clear')
        print('File Not Found')
        return

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(ch, user + "@gmail.com") for user in lines]
        for future in futures:
            future.result()
#— — — — — — — — — — — — —
def Get1():
    while True:
        try:
            a = instagram.generateUsername2013()
            if a and 'data' in a:
                us = a['data'].get('username')
                u = a['data'].get('follower_count', 0)
                if us and u > 99:
                    print(f' - User • {us} ¦ Follower • {u} - ')
                    with open('WATAN.txt', 'a') as ff:
                    	ff.write(f'{us}\n')
        except Exception as e:
            print(f' - Error: {e}')
#— — — — — — — — — — — — —
def Get2():
    while True:
        try:
            a = instagram.generateUsername2013()
            if a and 'data' in a:
                us = a['data'].get('username')
                u = a['data'].get('follower_count', 0)           
                print(f' - User • {us} ¦ Follower • {u} - ')
                with open('WATAN.txt', 'a') as ff:
                 ff.write(f'{us}\n')
        except Exception as e:
            print(f' - Error: {e}')
#— — — — — — — — — — — — —            
def del_list():	
	D = input(' Name File Delete : ')
	os.system(f'rm -rf {D}')
	print(' Done Delete Files ✓ ')	        
#— — — — — — — — — — — — —
def choice_menu():
    os.system("clear")
    print(f"""
{Y}- - - - - - - - - - - - - - - - - - - - 
{G}|< Choose Check {Y}
- - - - - - - - - - - - - - - - - - - - 
| {R}1 {W}- Check 2011 {Y}
| {R}2 {W}- Check 2012 {Y}
| {R}3 {W}- Check 2013 {Y}
| {R}4 {W}- Random < عالي > {Y}
| {R}5 {W}- Check List {Y}
| {R}6 {W}- Get List < عالي > {Y}
| {R}7 {W}- Get List < ناصي > {Y}
| {R}8 {W}- Delete List {Y}
| {R}9 {W}- Reset Email {Y}
- - - - - - - - - - - - - - - - - - - - 
""")    
    choice = input(f"{W} - Choose : ").strip()
    WK.open(url)
    if choice == "1":
        for i in range(25):
        	WTN(target=T1).start()   
    elif choice == "2":
        for i in range(25):
        	WTN(target=T2).start()   
    elif choice == "3":
        for i in range(25):
        	WTN(target=T3).start()  
    elif choice == "4":
        for i in range(25):
        	WTN(target=T4).start()  
    elif choice == "5":
               os.system('clear')
               name=input(f" - Enter File Name : ")
               admin_gmail(name)
    elif choice == "6":
        os.system('clear')   
        for i in range(25):
        	WTN(target=Get2).start()      
    elif choice == "7":
        os.system('clear')   
        for i in range(25):
        	WTN(target=Get1).start()          
    elif choice == "8":
    	os.system('clear')
    	del_list()
    elif choice == "9":
    	os.system('clear')
    	Res()    
    else:
        print(f"{R}⚠️ خيار غير صحيح، حاول مرة أخرى!{W}")
        choice_menu()
choice_menu()
#— — — — — — — — — — — — —