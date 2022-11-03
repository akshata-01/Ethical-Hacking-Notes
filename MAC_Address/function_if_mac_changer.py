#!/usr/bin/env python3

import subprocess #Importing subprocess module 
import optparse

def get_arguments():
    parser = optparse.OptionParser() #variable = module.Class()

    parser.add_option( "-i" , "--interface", dest="network_interface", help="Interface to change it's MAC Adress") #Options a user will give 
    parser.add_option( "-m" , "--mac", dest="mac_address", help= "New MAC Adress") #Options a user will give 
    (options, arguments) = parser.parse_args() #Allows the obj to understand what the user has given 

    if not options.network_interface:
        #code to handle error 
        parser.error("Please put a valid value of an interface or use --help for more info")

    elif not options.mac_address:
        parser.error("Please put a valid value of a mac address or use --help for more info")
    return options #Variable that holds new_interface and mac address 

def change_mac_address(network_interface, mac_address):
    print("[+] Changing MAC address for " + network_interface + " to " + mac_address)
    subprocess.call(["sudo", "ifconfig", network_interface, "down"])
    subprocess.call(["sudo","ifconfig", network_interface, "hw", "ether", mac_address])
    subprocess.call(["sudo","ifconfig", network_interface, "up"])

options = get_arguments()
change_mac_address(options.network_interface, options.mac_address)

