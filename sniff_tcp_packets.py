#!/usr/bin/python3

from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
   if IP in packet:
      ip_source = packet[IP].src
      ip_dest = packet[IP].src
      print(f"IP Packet: {ip_source} -> {ip_dest}")

if TCP in packet:
   tcp_source_port = packet[TCP].sport
   tcp_dest_port = packet[TCP].dport
   print(f"TCP Packet: {tcp_source_port} -> {tcp_dest_port}")

sniff(prn=packet_callback, count=10)

