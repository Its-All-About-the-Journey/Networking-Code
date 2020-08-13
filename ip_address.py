###################################################
### FIND THE BROADCAST ADDRESS IN AN IP ADDRESS ###
###################################################

from sys import exit
import time
import ipaddress

def ipConvert():
    ip = input("Write your IP Address with /x Mask (CIDR) here:\n>>")
    print(ipaddress.IPv4Network(ip, strict=False).broadcast_address)
    time.sleep(2)
    another = input("Do you have another IP Address to convert?\n[yes/no]\n>>")
    
    if 'yes' in another:
        return ipConvert()
    else:
        exit(0)

if __name__ == "__main__":
    ipConvert()
