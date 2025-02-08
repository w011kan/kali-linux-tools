import sys
import scapy.all as scapy
from rich import print
import optparse

## kullanım:
## python3 network_scan.py -i İP_range
## python3 network_scan.py -i 192.168.1.1/24

def inputs_argument(): ## -i parametresi için..
    parse_obje = optparse.OptionParser()

    parse_obje.add_option("-i","--ipaddr",dest="IP",help="set value of ip range")                                          

    
    return parse_obje.parse_args()



def scan(input_ip): ## tarama işlemleri...
    arp_packet=scapy.ARP(pdst=input_ip) ## arp isteği 

    broadcast_packet = scapy.Ether(dst="FF:FF:FF:FF:FF:FF") ## arp yayını için adres.

    #paketleri birleştirip  tek paket halinde toplama işlemi
    sum_packet= broadcast_packet/arp_packet

    show = scapy.srp(sum_packet,timeout=1,verbose=False)

    (alive, notalive) = show 

    # renkler 
    colors = ["green", "red", "blue", "yellow", "magenta", "cyan"]

    print("[bold]** MAC - IP Eşleşmeleri **[/bold]")


    for index, (sent, recived) in enumerate(alive):
        color = colors[index % len(colors)] 
        print(f"[{color}]MAC: {recived.hwsrc}  →  IP: {recived.psrc}[/{color}]")


(input,argumentss) =inputs_argument() ##tuple işlemi
ip= input.IP

scan(ip) ## scan işleminin başlatılması

