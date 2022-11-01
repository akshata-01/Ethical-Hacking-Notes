#!/usr/bin/env python3

import subprocess #Importing subprocess module 

network_interface = input("What's your network interface?")
print(network_interface)
mac_address = input("What MAC address would you like to set?")

#SYNTAX: subprocess.call("exit 1", shell=True) #

subprocess.call("ifconfig", shell=True) #Using this module and call function with 1st argument = command & 2nd as shell variable to True.
subprocess.call(f"sudo ifconfig {network_interface} down", shell=True) #Disabling interface 
subprocess.call(f"sudo ifconfig {network_interface} hw ether {mac_address}", shell=True) #Modify option of ether  | Make sure it's 12 characters & separated with : 
subprocess.call(f"sudo ifconfig {network_interface} up", shell=True) #enabling the interface 
subprocess.call("sudo ifconfig", shell=True) #To check 

#SYNTAX: subprocess.call(["ls", "-l"]) #
subprocess.call(["sudo", "ifconfig", network_interface, "down"])
subprocess.call(["sudo","ifconfig", network_interface, "hw", "ether", mac_address])
subprocess.call(["sudo","ifconfig", network_interface, "up"])




