#!usr/bin/env python3 

import scapy.all as scapy 
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = processed_sniffed_packet) #prn = For each packet we capture it'll call another function for us

def processed_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #Checks if packet has HTTP layer
        if packet.haslayer(scapy.Raw): 
            print(packet[scapy.Raw].load)

sniff("wlan0")