from scapy.all import *
from scapy.utils import hexdump
import json

def packet_callback(packet):
    if packet.haslayer(TCP):
        print("here")
        if packet[TCP].payload:
            payload = bytes(packet[TCP].payload).decode("utf-8", "ignore")

            
            print("HTTP Packet captured:")
            packet.show()
            print(" ") 

            hexdump(packet)
            print(" ")
        
            print(payload)
            

try:
    sniff(prn=packet_callback, filter="tcp and port 80")
except KeyboardInterrupt:
    print("\nExiting...")
