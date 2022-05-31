from os import remove
from site import removeduppaths #site adındaki modüle değişken ekledim
import time #zaman kütüphanesi zaman değişkeni eklemek için kullanılıyor,
import colorama #renk kütüphanesi 
from colorama import Fore, Back, Style
colorama.init()
print("KULLANICI GİRİŞ EKRANI")

eaa_password = input ("Bir parola belirleyin:")

if not eaa_password:
    print("Parola bölümü boş geçilemez")

elif len(eaa_password) > 8 or len(eaa_password) < 3:
    print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

else:
    print("Yeni parolanız", eaa_password)
eaa_username = "emrealiali"
while True:
    kullanici_adi = input("Kullanıcı Adını Giriniziz ipucu (emrealiali): ")#kullanıcı adı tanımlamak
    sifre = input("Belirlediğiniz Şifre'yi Giriniz: ")#şifre tanımlamak 

    if (kullanici_adi == eaa_username) and (sifre != eaa_password):#kullanıcı adı doğru fakat şifre yanlış
         print("Şifre yanlış..")

    elif (kullanici_adi != eaa_username) and (sifre == eaa_password):#şifre doğru fakat kullanıcı adı yanlış
         print("Kullanıcı adı yanlış..")

    elif(kullanici_adi != eaa_username) and (sifre != eaa_password):#kullanıcı adı ve şifre yanlış
         print("Kullanıcı adı ve şifre yanlış..")

    if(kullanici_adi == eaa_username) and (sifre == eaa_password):#her ikiside doğru ise sayfayı devam ettiriyor
        print(Fore.RED)
        print("3") 
        time.sleep(1) #time kütüphanesini genel olarak kullandığımız yer
        print(Fore.YELLOW)# colorama kütüphanesi ile renk veriyoruz 
        print("2") 
        time.sleep(1) 
        print(Fore.GREEN)
        print("1")
        time.sleep(1)
        print(Style.RESET_ALL)#verdiğimiz renkleri sıfırlıyoruz
        print("Mağazaya Giriş yapıldı!")
        time.sleep(0.5)
        print(Fore.LIGHTWHITE_EX)
        print("HOŞGELDİNİZ!")
        break #komut kendini tekrar etmesin diye komut çizgisini kırıyorum


    
print(Fore.LIGHTCYAN_EX+""" Marka seçiniz
    1.Bajaj
    2.Bmw
    3.Mondial
    4.KTM
    5.Ducati
    6.Falcon
    7.Honda
    8.Kawasaki
    9.Suzuki
    10.Yamaha
    PROGRAMI KAPATMAK İÇİN (kapat) YAZINIZ
    """)
print(Style.RESET_ALL)
# Bu alttaki aşamada motorların her birini değişken olarak tanımlıyorum özelliklerini ona göre giriyorum.
bajaj = 'Model: Pulsar rs 200\nTipi: Super Sport\n Yılı:2021\n Motor Hacmi: 200 cm³/n Motorgücü 176 - 200hp \n Renk: Mavi \n Fiyat: 57.000TL '

bmw = 'Model: R1200RT  \n Tipi:Touring\n Yılı: 2022 \n Motor Hacmi: 1001 - 1200 cm³\n Yılı \n Motorgücü: 101 - 125 hp \n Renk: Kırmızı \n Fiyat:119.000TL  '
 
mondial = 'Model:Nevada 250 \n Tipi:Chopper\n Yılı:2019 \n Motor Hacmi: 248cc \ Motor gücü:17hp \n Renk: Siyah \n Fiyat:73.437TL '

ktm = 'Model:250 EXC \n Tipi:Enduro \n Yılı: 2020 \n Motor Hacmi: 250cc \n Motor Gücü: 96hp \n Renk: Turuncu \n Fiyat:209.500TL  '

ducati = 'Model:Paingale V4\n Tipi:Super Sport \n Yılı: 2020 \n Motor Hacmi: 1100cc \n Motor Gücü: 225hp  \n Renk: Kırmızı \n Fiyat:571.000TL'

falcon = 'Model:Mexico 150 \n Tipi:Touring \n Yılı: 2021 \n Motor Hacmi: 100 - 125 cm3 \n Motor Gücü: 125hp \n Renk: Siyah \n Fiyat:29.000TL  '

honda = 'Model: NSS250(Forza 250) \n Tipi: Scooter \n Yılı:2021 \n Motor Hacmi: 151 - 250 cm3\n Motor Gücü: 225 hp \n Renk Siyah \n Fiyat:133.500TL'

kawasaki = 'Model: Ninja 636 \n Tipi: Super Sport \n Yılı:2005 \n Motor Hacmi: 251 - 650 cm3 \n Motor Gücü:650 hp \n Renk: Yeşil \n Fiyat 122.000TL'

suzuki = 'Model: GSX-R 250 \n Tipi: Super Sport \n Yılı: 2017 \n Motor Hacmi: 151 - 250 cm3\n Motor Gücü: 250 hp \n Renk: Mavi \n Fiyat: 107.000TL'

yamaha = 'Model: MT-09 \n Tipi: Naked / Roadster \n Yılı: 2015 \n Motor Hacmi:651 - 1000 cm3\n Motor Gücü: 125 hp \n Renk: Turuncu \n Fiyat: 187.000Tl'    


#Bu aşamada ise o belirlediğim değişkenleri inputtaki soruya bağlı olarak print ile terminale yazdırıyoruz
while True:
    belirle = input("Seçeceğiniz Markanın Adını Giriniz:")
    if belirle == 'bajaj':
        print(bajaj)
    
    elif belirle == 'bmw':
        print (bmw)

    elif belirle == 'mondial':
        print(mondial)

    elif belirle == 'ktm':
        print(ktm)

    elif belirle == 'ducati':
        print(ducati)

    elif belirle == 'falcon':
        print(falcon)

    elif belirle == 'honda':
        print(honda)

    elif belirle == 'kawasaki':
        print(kawasaki)

    elif belirle == 'suzuki':
        print(suzuki)

    elif belirle == 'yamaha':
        print(yamaha)
    
    elif belirle == 'kapat':
        
        print("PROGRAM KAPANIYOR") 
        print(Fore.RED)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print(Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX)
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz :)")
        time.sleep(2)
        exit(0)
   
    else:
        print(Fore.LIGHTRED_EX)
        print("Lütfen Geçerli Bir İşlem Girin")
        print(Style.RESET_ALL)
     
