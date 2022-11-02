#!/usr/bin/env python3

import subprocess #Importing subprocess module 
import optparse

parser = optparse.OptionParser() #variable = module.Class()

#Handle User Input using arguments

parser.add_option( "-i" , "--interface", dest="network_interface", help="Interface to change it's MAC Adress") #Options a user will give 
parser.add_option( "-m" , "--mac", dest="mac_address", help= " New MAC Adress") #Options a user will give 

(options, arguments) = parser.parse_args() #Allows the obj to understand what the user has given 

network_interface = options.network_interface #parser.parse_args() returns the values if given a variable 
mac_address = options.mac_address

print("[+] Changing MAC address for " + network_interface + " to " + mac_address)