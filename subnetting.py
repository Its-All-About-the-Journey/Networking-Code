from sys import exit
import time
import ipaddress
import random

def ipConvert():
    octect1 = 10
    octect2 = random.randint(1, 255)
    octect3 = random.randint(1, 255)
    octect4 = random.randint(1, 255)
    mask = random.randint(1, 32)

    ip = f'{octect1}.{octect2}.{octect3}.{octect4}/{mask}'
    print(f"What are the network address, broadcast address, and the subnet mask for a host with the IP Address:\n {ip}?\n")

    net1 = str(ipaddress.IPv4Network(ip, strict=False).network_address)
    broa1 = str(ipaddress.IPv4Network(ip, strict=False).broadcast_address)
    sub1 = str(ipaddress.IPv4Network(ip, strict=False).netmask)

    net_addr = input("What is the Network Address:\n")
    broad_add = input("What is the Broadcast Address:\n")
    net_mask = input("What is the Subnet Mask:\n")

    while net_addr != net1:
        print("\nWrong Network Address!\nTry again!\n")
        net_addr = input("What is the Network Address: ")
    while broad_add != broa1:
        print("\nWrong Broadcast Address!\nTry again!\n")
        broad_add = input("What is the Broadcast Address: ")
    while net_mask != sub1:
        print("\nWrong Subnet Mask!\nTry again!\n")
        net_mask = input("What is the Subnet Mask: ")

    print("Congrats!\n")
    
    another = input("Do you want to try again?\n[yes/no]\n>>")
    if 'yes' in another:
        return ipConvert()
    else:
        exit(0)

if __name__ == "__main__":
    ipConvert()

