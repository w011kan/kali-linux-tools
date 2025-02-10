# kali-linux-tools

- Bu depo, çeşitli güvenlik, ağ yönetimi ve sistem analizine yönelik araçları içermektedir. 
- Her araç, belirli bir ihtiyaca yönelik olarak geliştirilmiş olup, ağ güvenliği, penetrasyon testleri ve sistem yapılandırması gibi konularda kullanıcıya yardımcı olmayı amaçlamaktadır.
- Her aracın detaylı açıklamalarına ve kullanım talimatlarına alt kısımdan bulabilirsiniz..

## mac_changer.py 
- Bu araç, Kali Linux üzerinde ağ arayüzlerinin MAC adresini değiştirmek için geliştirilmiştir. 
- Rastgele veya manuel olarak MAC adresi atama seçenekleri sunar. 
- MAC adresi değişikliği, ağ güvenliği testleri, gizlilik önlemleri ve belirli ağ erişim kısıtlamalarını aşmak için kullanılabilir.

#### Özellikler
  
 - Rastgele MAC oluşturma: Geçerli MAC adresi formatına uygun rastgele adres üretir.
 - Manuel MAC atama: Kullanıcının belirlediği özel bir MAC adresini ağ arayüzüne uygular.
 - Doğrulama Mekanizması: Değişikliğin başarılı olup olmadığını kontrol eder.
 - CLI Desteği: Komut satırından kolay kullanım için optimize edilmiştir.

#### Kullanım
  * Random için: `python3 mac_changer.py -r -i interface`
  * Manual için: `python3 mac_changer.py -m mac -i interface`
  * Kullanım için root yetkisi gerekebilir.


Ilk başta random olarak değiştirelim => ` python3 mac_changer.py -r -i interface`

![image](https://github.com/user-attachments/assets/cc097f7a-e489-40f1-a3b2-47be6956952a)



Tekrar random olarak mac değiştirirsek...

![image](https://github.com/user-attachments/assets/d686f637-32ee-4ee1-8adf-b2a072997301)


Ardından manual şekilde değiştirelim... => `python3 mac_changer.py -m mac -i interface`

![image](https://github.com/user-attachments/assets/dd8ba6e4-4cfc-405d-88da-0152080419bf)


- Kullanıcı hatasını da önlemek için " mac_is_valid " fonksiyonu görev almaktadır.
- Yanlış formatta bir mac adresi girilebilir ve bunu kontrol edip eğerki şartları sağlarsa mac adresi değiştirilir..

![image](https://github.com/user-attachments/assets/499d5548-ce25-4b0d-8a3b-3c95fc4b48d4)

Başka bir hatalı giriş..

![image](https://github.com/user-attachments/assets/d4797add-c932-4ecf-8496-c3c8023921b6)



##### 📌 Sonuç  

- Bu araç, Kali Linux kullanıcıları için ağ arayüzlerinin MAC adresini değiştirmeyi kolaylaştırmak amacıyla geliştirilmiştir. 
- Güvenlik testleri, anonimlik veya ağ erişimi ile ilgili ihtiyaçlar için kullanılabilir.  




## network_scan.py 
- Bu araç, Kali Linux ve diğer Linux sistemlerinde ağ üzerindeki cihazları tespit etmek için geliştirilmiştir.
- ARP (Address Resolution Protocol) taraması yaparak, ağdaki cihazların MAC ve IP adreslerini listeler.
- Ağ güvenliği testleri, bağlı cihazları görüntüleme ve ağ analizi yapmak için kullanılabilir.

#### Özellikler
  
- Ağ Taraması: Belirtilen IP aralığında ARP isteği göndererek bağlı cihazları tespit eder.
- MAC - IP Eşlemesi: Ağdaki cihazların MAC adreslerini ve IP adreslerini gösterir.
- Renkli Çıktı: Sonuçlar renkli olarak ekrana yazdırılır, böylece veriler kolay okunabilir.
- CLI Desteği: Komut satırından esnek kullanım sağlar.
- Kolay Kullanım: Hedef IP aralığını belirterek hızlı tarama yapabilirsiniz.


#### Kullanım
  * Tüm ağı taramak için: `python3 network_scan.py -i 192.168.1.1/24`
  * Özel bir IP bloğu taramak için: `python3 network_scan.py -i 10.0.0.1/16`

  ![image](https://github.com/user-attachments/assets/736ceedb-836b-4ebf-ac94-bc0d4c7ce183)



##### 📌 Sonuç  

- Bu araç, Kali Linux kullanıcıları için ağdaki cihazları hızlı ve kolay bir şekilde tespit etmek amacıyla geliştirilmiştir.
- Ağ güvenliği testleri, izinsiz cihazları belirleme ve ağ yönetimi gibi amaçlar için kullanılabilir.
- Kullanıcı dostu CLI arayüzü sayesinde, ağ analizi yapmak isteyen herkes için pratik ve etkili bir çözümdür.





## man_in_the_middle.py 
- Bu araç, Kali Linux ve diğer Linux sistemlerinde Man-in-the-Middle (MitM) saldırılarını simüle etmek için geliştirilmiştir
- ARP Spoofing yöntemiyle ağ trafiğini yönlendirerek, iki cihaz arasındaki iletişimi dinleyebilir veya değiştirebilirsiniz.
- Kısaca; Bir gateway ve ona bağlı bir cihaz arasında, istekleri yönlendirerek ve mac spoofing yaparak MITM atak gerçekleştirilir. 

#### Özellikler
  
- ARP Spoofing: Hedef cihazları yanıltarak trafiği yönlendirir.
- Renkli Çıktı: Trafik bilgilerini renkli olarak görüntüler.
- CLI Desteği: Komut satırından esnek kullanım sağlar.
- Kolay Kullanım: Hedef IP ve ağ geçidini belirterek hızlıca çalıştırabilirsiniz.


#### Kullanım
  * MITM gerçekleştirmek için: `python3 man_in_the_middle.py --target1 10.0.2.5 --target2 10.0.2.1` gibi.
  * Burada --target1 ve --target2 nin sırası yada değerlerinin sırası önemsizdir.
  * İşlemi herhangi bir an durdurmak için `x + enter`
  * Herhangi bir değer gateway ip değeri veya hedef PC ip değeri olarak girilebilir.
    
    ![image](https://github.com/user-attachments/assets/4c9b65d5-9027-47aa-904b-60c203fe0374)

  * Burada 10.0.2.1 adresi gateway iken, 10.0.2.5 ağa bağlı Windows bir cihazdır.
  * İşleme başlamadan önce Windows cihaz için arp tablosuna bakalım.. (arp -a)
    ![image](https://github.com/user-attachments/assets/41a51d9f-3fd2-40a1-bd7f-134a27105e94)
  * Görüleceği üzere gateway mac ve kaynak cihazımız olan kali için 10.0.2.7 için mac adresleri görünüdeki gibidir.

  * MITM başlatacak olursak. Gateway için mac adresi kali cihazımızın mac adresi değeri olacaktır.
    ![image](https://github.com/user-attachments/assets/180fd87d-a2a9-465e-b7ca-7944710a26ce)

  Herhangi bir anda saldırıyı durdurmak için x+enter yapılır.
    ![image](https://github.com/user-attachments/assets/7d70ed2c-e637-4b86-b746-d4b1b699e2af)

    


##### 📌 Sonuç  

- man_in_the_middle.py, ağ güvenliği testleri yapmak ve MitM saldırılarının etkilerini analiz etmek için geliştirilmiştir.







 
