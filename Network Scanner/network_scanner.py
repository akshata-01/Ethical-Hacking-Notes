#!usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #A packet that asks a specific IP 
    arp_request.show() #Shows details of the package 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #This will create a ether object and store an instance in variable boradcast 
    broadcast.show()
    arp_request_boradcast = broadcast/arp_request #appending our 2 packtes using / 
    arp_request_boradcast.show()
    #scapy.ls(scapy.Ether)
    #scapy.ls(scapy.ARP) #ls function by scapy gives names of the variables you can set for ARP class 
    #arp_request.pdst = ip
    #broadcast.dst = ""ff:ff:ff:ff:ff:ff""
    #arp_request.pdst = ip
    #print(arp_request.summary()) #This is a method in ARP class 
    #print(broadcast.summary())
    print(arp_request_boradcast.summary()) 

scan("192.168.0.1/24") #Range 0-254 