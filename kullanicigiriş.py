from site import removeduppaths #site adındaki modüle değişken ekledim
import time #zaman kütüphanesi zaman değişkeni eklemek için kullanılıyor,
import colorama#iyi bir görünüş için renk kütüphanesi
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
