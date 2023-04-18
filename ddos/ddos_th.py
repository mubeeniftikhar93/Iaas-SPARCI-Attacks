import threading
import os

def print_string():

    while True:
       os.system("sudo nmap -Pn 141.26.68.156")
       os.system("ssh mubeeniftikhar1@141.26.68.156 -p 22")

threads = []
for i in range(200):
    t = threading.Thread(target=print_string)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
