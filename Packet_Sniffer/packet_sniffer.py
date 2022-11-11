#!usr/bin/env python3 

import scapy.all as scapy 

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = processed_sniffed_packet) #prn = For each packet we capture it'll call another function for us

def processed_sniffed_packet(packet):
    print (packet)

sniff("wlan0")