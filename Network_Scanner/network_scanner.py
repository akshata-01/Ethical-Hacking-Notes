#!usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t" , "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #A packet that asks a specific IP 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #This will create a ether object and store an instance in variable boradcast 
    arp_request_boradcast = broadcast/arp_request #appending our 2 packtes using / 
    answered_list = scapy.srp(arp_request_boradcast, timeout=1, verbose = False)[0] #sr is function of sending & receiving while srp actually allows custom ether
    
    clients_list = [] 
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc +"\t\t\t"+ element[1].hwsrc) #IP of the client + MAC Address #Each layer has ethernet and arp layer | MAC Address 
    return clients_list

def print_result(results_list):
    print("IP\t\t\t\tMAC Address\n-------------------------------------------------")
    for element_client in results_list:
        print(element_client["ip"] + "\t\t\t" + element_client["mac"])

options = get_arguments()
scan_result = scan(options.target) #Range 0-254 
print_result(scan_result)