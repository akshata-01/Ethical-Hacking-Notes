#!/usr/bin/env python3

import subprocess #Importing subprocess module 
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser() #variable = module.Class()

    parser.add_option( "-i" , "--interface", dest="network_interface", help="Interface to change it's MAC Adress") #Options a user will give 
    parser.add_option( "-m" , "--mac", dest="mac_address", help= "New MAC Adress") #Options a user will give 
    
    (options, arguments) = parser.parse_args() #Allows the obj to understand what the user has given 

    if not options.network_interface:
        #code to handle error 
        parser.error("Please put a valid value of an interface or use --help for more info")

    elif not options.mac_address:
        #code to handle error 
        parser.error("Please put a valid value of a mac address or use --help for more info")
    return options #Variable that holds new_interface and mac address 

def change_mac_address(network_interface, mac_address):
    print("[+] Changing MAC address for " + network_interface + " to " + mac_address)
    subprocess.call(["sudo", "ifconfig", network_interface, "down"])
    subprocess.call(["sudo","ifconfig", network_interface, "hw", "ether", mac_address])
    subprocess.call(["sudo","ifconfig", network_interface, "up"])

#SYNTAX subprocess.check_output(["echo", "Hello World!"])
def get_current_mac(network_interface):
    ifconfig_result = subprocess.check_output(["ifconfig", network_interface], encoding="utf-8") #Execute ifconfig followed by options.interface
    #print(ifconfig_result) 

    #Regular Expression- Search for specific pattern 
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) #Search the given rules in ifconfig_result
    if mac_result:
        return mac_result.group(0) #If there's more than 1 match they're put into groups so specifying group 1 will give us the 1st matched result
    else: 
        print("Could not read MAC Address")
        #return ("Invalid value")

options = get_arguments()
current_mac = get_current_mac(options.network_interface)
print("Current mac is " + str(current_mac))

change_mac_address(options.network_interface, options.mac_address)
current_mac = get_current_mac(options.network_interface)
if current_mac == options.mac_address:
    print("MAC Address got changed to " + current_mac)