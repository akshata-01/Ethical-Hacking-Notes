#!usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #A packet that asks a specific IP 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #This will create a ether object and store an instance in variable boradcast 
    scapy.ls(scapy.Ether)
    #broadcast.dst = ""ff:ff:ff:ff:ff:ff""
    #arp_request.pdst = ip
    #print(arp_request.summary()) #This is a method in ARP class 
    #scapy.ls(scapy.ARP) #ls function by scapy gives names of the variables you can set for ARP class 
    print(broadcast.summary())
scan("192.168.0.1/24") #Range 0-254 