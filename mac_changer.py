import subprocess # sistem komutlarını çalıştırmak için kullanılır.
import optparse  # komut satırı argümanlarını almak için kullanılır.
import random   # rastgele sayı ve karakter üretmek için kullanılır.
import sys      # sistemle ilgili işlemleri gerçekleştirmek için kullanılır.
import re       # düzenli ifadeler (regex) ile metin işleme işlemleri için kullanılır.

## -i interface belirtmek için (eth0 , wlan0 vs)
## -m mac değerini manual girmek için
## -r mac değerini random girmek için 



##  örnek kullanımlar ##
## python3 mac_changer.py -r -i wlan0
## python3 mac_changer.py -m  11:AA:BB:44:55:66 -i wlan0

def ifconfig_commands(interface_parameter,newmac_parameter): ## değişim için ilgili console komularını yazar.

    interface= interface_parameter
    newmac=  newmac_parameter

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",newmac])
    subprocess.call(["ifconfig",interface,"up"])

def inputs_arguments(): ## -i -m  -r gibi parametrelerin girişi
    parse_obj = optparse.OptionParser()

    parse_obj.add_option("-i","--interface",dest="interface",help="interface to change!")                                          
    parse_obj.add_option("-m","--mac",dest="newmac",help="mac address to change!")
    parse_obj.add_option("-r", "--random", action="store_const", const=1, dest="choice") # -r parametresi girilirse mod seçimi 1 olucak (choice = 1 )

    return parse_obj.parse_args()

def mac_change_random(): ## mac addressini  random secer.
   

    newmac_blocks=[]

    i = 6 ## 6 adet 2 li mac blockları için.

    while i > 0:
        number1 = random.randint(0, 9)  # 0-9 arası rastgele sayı seçer..
        number2 = random.randint(0, 9)

        harf1 = random.choice(["A", "B", "C", "D", "E", "F"])  # A-F arasında harf seçer..
        harf2 = random.choice(["A", "B", "C", "D", "E", "F"])

        macblock = "00"  # Varsayılan değer

        choice = random.randint(1, 4)  # 1-4 arasında seçim yapar

        if choice == 1:
            macblock = str(number1) + str(number2)
        elif choice == 2:
            macblock = harf1 + str(number1)
        elif choice == 3:
            macblock = str(number2) + harf2
        else:
            macblock = harf2 + harf1

        newmac_blocks.append(macblock)
        i = i - 1  

    random.shuffle(newmac_blocks)
    random.shuffle(newmac_blocks)
    random.shuffle(newmac_blocks)

    if newmac_blocks[0][1] == "1" or  newmac_blocks[0][1] == "3" or newmac_blocks[0][1] == "5" or newmac_blocks[0][1] == "7" or newmac_blocks[0][1] == "9" or newmac_blocks[0][1] == "B" or newmac_blocks[0][1] == "D" or newmac_blocks[0][1] == "F": 
        ## eğerki mac adresinin soldan ilk baytının LSB değeri 1 ise , *multicast olur ve çoğu sistem kabul etmez.
        ## bu olayı korumak için  o biti 1 olmayacak şekilde rastgele seçiyoruz, alt kısımda..

        safe_mac_block= random.choice(["0", "2", "A", "C", "4", "E","6","8"])
        newmac_blocks[0]=newmac_blocks[0][0]+safe_mac_block


    newmac= newmac_blocks[0]+":"+newmac_blocks[1]+":"+newmac_blocks[2]+":"+newmac_blocks[3]+":"+newmac_blocks[4]+":"+newmac_blocks[5]

    return newmac

def mac_is_changed(interface_argument,newmac_argument): ## adresin değişip değişmediğini kontrol eder.

    ifconfig = subprocess.check_output(["ifconfig",interface_argument])
    ifconfig= ifconfig.decode()
    new_mac= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    upper_group= new_mac.group(0).upper()

                                                                     
    if oldmac == newmac_argument:
        return 1
    elif upper_group== newmac_argument :
        return 2    
    else:
        return 3

def mac_is_valid(newmac): ## uyumluluk kontrolu yapar
    valid_sembols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F",":"]
    
    
    if newmac.count(":")!=5 or len(newmac)!=17 or newmac[2]!=":"or newmac[5]!=":"or newmac[8]!=":"or newmac[11]!=":"or newmac[14]!=":":
        print("MAC format hatasi...") 
        sys.exit()  # programı sonlandırır


    if  any(char not in valid_sembols for char in newmac):
        print("Girilen mac adresi uyumsuz karakterlerden oluşmakta..")
        sys.exit()  # programı sonlandırır


    if newmac[1] == "1" or  newmac[1] == "3" or newmac[1] == "5" or newmac[1] == "7" or newmac[1] == "9" or newmac[1] == "B" or newmac[1] == "D" or newmac[1] == "F":
        print("Uyari!!:manual mac girişinde ilk baytin LSB si 1 olmamalidir. örn(X1:XX:XX:XX:XX:XX veya XB:XX:XX:XX:XX:XX olmamalı)")
        print("Bu durum mac adresinin multicast olmasini sağlar. Çoğu sistem kabul etmez.")
        print("Lutfen tekrardan farklı bir mac adresi giriniz..")
        
        sys.exit()  # programı sonlandırır

def old_mac(interface_argument):
    ifconfig = subprocess.check_output(["ifconfig",interface_argument])
    ifconfig= ifconfig.decode()
    old= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig).group(0).upper() ## reger formatında ilgili mac değerine erişmek için..

    return old

(inputs,arguments) = inputs_arguments() ## tuple ataması..
interface= inputs.interface

oldmac=old_mac(interface)

print("##M4C CH4NG3R##")

## mod Seçimi
if inputs.choice == 1: ## random mod seçilmiş ise..
    
    newmac=mac_change_random()
    
else:   ## kullanıcı manual mac girmek isterse.

    newmac=inputs.newmac.upper()
    mac_is_valid(newmac) ## uyumluluk kontrolu



ifconfig_commands(interface,newmac)  ## komutların gerçeklenmesi


if mac_is_changed(interface,newmac) == 2:
    print("mac changed done!")
    print(f"old mac address:{oldmac}")
    print(f"new mac address:{newmac}")
    print(f"interface: {interface}")
    
elif mac_is_changed(interface,newmac) == 1:
    print("same mac adress entered")
    print(f"old mac address:{oldmac}")
    print(f"new mac address:{newmac}")
    print(f"interface: {interface}")

else :
    print("mac not changed!")




