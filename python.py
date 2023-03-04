from scapy.all import *
import random

# Prompt the user to enter an IP address and port number
ip = input("Enter the IP address to send packets to: ")
port = int(input("Enter the port number to send packets to: "))

# Generate random data to send in each packet
packet_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1024))

# Send 100000 UDP packets to the destination IP and port
for i in range(100000):
    packet = IP(dst=ip) / UDP(dport=port) / packet_data
    send(packet)
