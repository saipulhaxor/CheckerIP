import os
import json
import requests
import time
from datetime import datetime

os.system(f"cls")
open('clientUP.txt', 'w')
print(f"	CHECKER CLIENT\n   PT. SIMTEL Sc. NOC Syaiful\n================================")
class date:
	clock = datetime.now()
	day = str(clock.day)
	month = str(clock.month)
	year = str(clock.year)
	hour = str(clock.hour)
	minute = str(clock.minute)
	second = str(clock.second)
	today = str(clock.today)
def timer(start_minute, start_second):
	total_second = start_minute* 10 + start_second
	while total_second:
		mins, secs = divmod(total_second, 10)
		print(f' {mins:02d}:{secs:02d} ', end='\r')
		time.sleep(1)
		total_second -= 1
		pass
	print(" Done! ")
	pass

username = list()
ip = list()
with open('client.txt', 'r') as userlist:
    for line in userlist:
        user, ips = line.strip().split('|')
        username.append(user)
        ip.append(ips)
total_length = len(username)
while True:
	for i in range(total_length):
		response = os.popen(f"ping {ip[i]} -w 50").read()
		if "Received = 4" in response:
			print(f"[ UP ] {username[i]} <> {ip[i]}")
			text = open('clientUP.txt', 'a+')
			read = open('clientUP.txt', 'r', encoding="utf-8")
			if username[i] not in read.read():
				requests.get(f"https://api.telegram.org/bot6438030553:AAEZYYxoThr_RsAp5dXdaAYkLmeXb37U5b4/sendMessage?chat_id=1393055245&text=UP {username[i]} <> {ip[i]}")
				text.write(f"{username[i]}|{ip[i]}\n")
		else:
			print(f"[ DOWN ] {username[i]} <> {ip[i]}")
	if __name__ == '__main__':
		timer(00,10)
print(f'\n==========================\nPT. SOLUSI MEDIA TELEKOMUNIKASI \nSC. NOC. Syaiful Hadi')