#!/usr/bin/env python3

import subprocess #Importing subprocess module 

network_interface = input("What network_interface would you like to enter? ")
mac_address = input("What MAC address would you like to set? ")

#SYNTAX: subprocess.call(["ls", "-l"]) #

subprocess.call(["sudo", "ifconfig", network_interface, "down"])
subprocess.call(["sudo","ifconfig", network_interface, "hw", "ether", mac_address])
subprocess.call(["sudo","ifconfig", network_interface, "up"])




