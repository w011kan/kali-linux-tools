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



## 📌 Sonuç  

- Bu araç, Kali Linux kullanıcıları için ağ arayüzlerinin MAC adresini değiştirmeyi kolaylaştırmak amacıyla geliştirilmiştir. 
- Güvenlik testleri, anonimlik veya ağ erişimi ile ilgili ihtiyaçlar için kullanılabilir.  

