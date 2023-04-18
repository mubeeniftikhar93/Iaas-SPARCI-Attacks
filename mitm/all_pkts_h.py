from scapy.all import *
from scapy.utils import hexdump
import time
def packet_callback(packet):
    if packet.haslayer(TCP):
        if packet[TCP].dport == 21 or packet[TCP].sport == 21:
            print("FTP Packet captured:")
            hexdump(packet)
        elif packet[TCP].dport == 25 or packet[TCP].sport == 25:
            print("SMTP Packet captured:")
            hexdump(packet)
        elif packet[TCP].dport == 22 or packet[TCP].sport == 22:
            print("SSH Packet captured:")
            hexdump(packet)
        elif packet[TCP].payload:
            payload = bytes(packet[TCP].payload).decode("utf-8", "ignore")
            print(payload)
            if "GET" in payload or "POST" in payload:
                print("HTTP Packet captured:")
                hexdump(packet)
    elif packet.haslayer(UDP):
        print("UDP Packet captured:")
        hexdump(packet)
    elif packet.haslayer(ICMP):
        print("ICMP Packet captured:")
        hexdump(packet)
    elif packet.haslayer(ARP):
        print("ARP Packet captured:")
        hexdump(packet)
    elif packet.haslayer(DNS):
        print("DNS Packet captured:")
        hexdump(packet)
    elif packet.haslayer(DHCP):
        print("DHCP Packet captured:")
        hexdump(packet)
    else:
        print("Other Packet captured:")
        hexdump(packet)
try:
    while True:
        sniff(prn=packet_callback, count=1)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nExiting...")



