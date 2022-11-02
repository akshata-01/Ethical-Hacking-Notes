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

# #SYNTAX: subprocess.call("exit 1", shell=True) #

# subprocess.call("ifconfig", shell=True) #Using this module and call function with 1st argument = command & 2nd as shell variable to True.
# subprocess.call(f"sudo ifconfig {network_interface} down", shell=True) #Disabling interface 
# subprocess.call(f"sudo ifconfig {network_interface} hw ether {mac_address}", shell=True) #Modify option of ether  | Make sure it's 12 characters & separated with : 
# subprocess.call(f"sudo ifconfig {network_interface} up", shell=True) #enabling the interface 
# subprocess.call("sudo ifconfig", shell=True) #To check 

# #SYNTAX: subprocess.call(["ls", "-l"]) #
# subprocess.call(["sudo", "ifconfig", network_interface, "down"])
# subprocess.call(["sudo","ifconfig", network_interface, "hw", "ether", mac_address])
# subprocess.call(["sudo","ifconfig", network_interface, "up"])




