from sys import exit
import ipaddress
import random

def ipConvert():
    octect1 = random.randint(1, 255)
    octect2 = random.randint(1, 255)
    octect3 = random.randint(1, 255)
    octect4 = random.randint(1, 255)
    mask = random.randint(8, 32)

    ip = f'{octect1}.{octect2}.{octect3}.{octect4}/{mask}'
    print(f"What are the network address, broadcast address, and the subnet mask for a host with the IP Address:\n {ip}?\n")
    # --------------------------------------- #
    # Convert Ip Address from the Variable IP #
    # --------------------------------------- #
    net1 = str(ipaddress.IPv4Network(ip, strict=False).network_address)
    broa1 = str(ipaddress.IPv4Network(ip, strict=False).broadcast_address)
    sub1 = str(ipaddress.IPv4Network(ip, strict=False).netmask)
    # ---------------------------------------------------------------- #
    # Find the good Network, Broadcast and Subnet from the variable IP #
    # ---------------------------------------------------------------- #
    net_addr = input("What is the Network Address:\nn for quit this IP Address | q for exit the program\n>>")
    if 'q' in net_addr:
        exit(0)
    elif 'n' in net_addr:
        return ipConvert()

    broad_add = input("What is the Broadcast Address:\nn for quit this IP Address | q for exit the program\n>>")
    if 'q' in broad_add:
        exit(0)
    elif 'n' in broad_add:
        return ipConvert()

    net_mask = input("What is the Subnet Mask:\nn for quit this IP Address | q for exit the program\n>>")
    if 'q' in net_mask:
        exit(0)
    elif 'n' in net_mask:
        return ipConvert()
    # -------------------------------------------------------- #
    # Until wrong, try again, except if "N" or "Q" are pressed #
    # -------------------------------------------------------- #
    while net_addr != net1:
        print("\nWrong Network Address!\nTry again!\n")
        net_addr = input("What is the Network Address:\nn for quit this IP Address | q for exit the program\n>>")
        if 'q' in net_addr:
            exit(0)
        elif 'n' in net_addr:
            return ipConvert()
        
    while broad_add != broa1:
        print("\nWrong Broadcast Address!\nTry again!\n")
        broad_add = input("What is the Broadcast Address:\nn for quit this IP Address | q for exit the program\n>>")
        if 'q' in broad_add:
            exit(0)
        elif 'n' in broad_add:
            return ipConvert()

    while net_mask != sub1:
        print("\nWrong Subnet Mask!\nTry again!\n")
        net_mask = input("What is the Subnet Mask:\nn for quit this IP Address | q for exit the program\n>>")
        if 'q' in net_mask:
            exit(0)
        elif 'n' in net_mask:
            return ipConvert()

    print("Congrats!\n")
    
    # ---------------------- #
    # Try another Ip Address #
    # ---------------------- #
    another = input("Do you want to try again?\n[yes/no]\n>>")
    if 'yes' in another:
        return ipConvert()
    else:
        exit(0)

if __name__ == "__main__":
    ipConvert()
