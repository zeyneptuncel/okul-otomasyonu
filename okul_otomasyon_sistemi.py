class Okul:
    def __init__(self,isim, soyisim, tc):
        self.isim=isim
        self.soyisim=soyisim
        self.tc=tc

class Ogrenci(Okul):
    def __init__(self, isim , soyisim, tc,  sinif, bolum,not1=None, not2=None):
        super().__init__(isim, soyisim, tc)

        self.sinif=sinif
        self.bolum=bolum
        self.not1=not1
        self.not2=not2

class Calisan(Okul):
    def __init__(self, isim , soyisim, tc, meslek, maas):
        super().__init__(isim, soyisim, tc)

        self.meslek=meslek
        self.maas=maas

def ogrenci_ekle():
    isim=input("Öğrenci ismi giriniz: ").lower()
    soyisim=input("Öğrenci soyismini giriniz: ").lower()
    tc = input("Öğrenci tc kimlik numarasını giriniz: ")
    sinif= input("Öğrenci sınıfını giriniz: ")
    bolum= input("Öğrenci bölümünü giriniz: ")

    with open ("ogrenci_bilgileri.txt","a",encoding="utf-8") as dosya:
        dosya.write(f"{isim},{soyisim},{tc},{sinif},{bolum}\n")
    print(f"Öğrenci kaydedildi. İsim: {isim} Soyisim: {soyisim} Tc: {tc} Sınıf: {sinif} Bölüm: {bolum}")
    ogrenci=Ogrenci(isim,soyisim,tc,sinif,bolum)

    
def ogrenci_goruntule():
    goruntulenecek_tc=input("Bilgileirni görüntülemek istediğiniz öğrencinin tcsinin giriniz: ")
    with open("ogrenci_bilgileri.txt","r",encoding="utf-8") as dosya:
        satirlar= dosya.readlines()
    bulundu_mu=False
    for satir in satirlar:
        bilgiler=satir.strip().split(",")
        if not(len(bilgiler)>=5):
            if goruntulenecek_tc in satir:
                bulundu_mu=True
                print("Öğrenci bulunamadı\nVeri dosyasında hata var kontrol edin.")
                break
            else:
                continue
        else:
            tc=bilgiler[2]
            if goruntulenecek_tc==tc:
                if len(bilgiler)==7:
                    print(f"\nİsim: {bilgiler[0]} Soyisim: {bilgiler[1]}\nTc: {bilgiler[2]}\nSınıf: {bilgiler[3]}\nBölüm: {bilgiler[4]}\nNot1: {bilgiler[5]} Not2: {bilgiler[6]}")
                else:
                    print(f"\nİsim: {bilgiler[0]} Soyisim: {bilgiler[1]}\nTc: {bilgiler[2]}\nSınıf: {bilgiler[3]}\nBölüm: {bilgiler[4]}")
                bulundu_mu=True
                break
    if bulundu_mu==False:
        print("Bu tcye ait öğrenci bulunamadı.")
        
def ogrenci_sil():
    silinecek_tc=input("Silmek istediğiniz öğrenci tcsini giriniz: ")
    with open("ogrenci_bilgileri.txt","r", encoding="utf-8") as dosya:
        satirlar=dosya.readlines()
    with open("ogrenci_bilgileri.txt","w", encoding="utf-8") as dosya:
        silindi_mi=False
        hata=False
        for satir in satirlar:
            bilgiler=satir.strip().split(",")
            if not(len(bilgiler)>=5):
                if silinecek_tc in satir:
                    hata=True
                else:
                    dosya.write(satir)
            else:
                tc=bilgiler[2]
                if tc!=silinecek_tc:
                    dosya.write(satir)
                else:
                    silinen_ad=bilgiler[0]
                    silinen_soyad=bilgiler[1]
                    silindi_mi=True
 
        if hata==True:
            print("Veri hatası olan satır başarıyla silindi")
        if silindi_mi==True:
            print(f"{silinen_ad} {silinen_soyad} isimli öğrencinin kaydı başarıyla silindi")
        else:
            print("Öğrenci bulunamadı")
    
def calisan_ekle():
    isim=input("Çalışan ismi giriniz: ").lower()
    soyisim=input("Çalışan soyismini giriniz: ").lower()
    tc = input("Çalışan tc kimlik numarasını giriniz: ")
    meslek = input("Çalışan mesleğini giriniz: ").lower()
    maas = input("Çalışan maas bilgisini giriniz: ")
    with open("calisan_bilgileri.txt","a",encoding="utf-8") as dosya:
        dosya.write(f"{isim},{soyisim},{tc},{meslek},{maas}\n")
    calisan=Calisan(isim,soyisim,tc,meslek,maas)
    print(f"Çalışan kaydedildi. İsim: {isim} Soyisim: {soyisim} Tc: {tc} Meslek: {meslek} Maaş: {maas}")

def calisan_goruntule():
    goruntulencek_tc=input("Görüntülemek istediginiz çalışanın tcsini giriniz: ")
    with open("calisan_bilgileri.txt","r",encoding="utf-8") as dosya:
        satirlar=dosya.readlines()
        bulundu_mu=False
        for satir in satirlar:
            bilgiler=satir.strip().split(",")
            if not(len(bilgiler)==5):
                if goruntulencek_tc in satir:
                    print(len(bilgiler))
                    bulundu_mu=True
                    print("Çalışan bulunamadı\nVeri dosyasında hata var kontrol edin.")
                    break
            else:
                tc=bilgiler[2]
                if tc==goruntulencek_tc:
                    bulundu_mu=True
                    print(f"\nİsim: {bilgiler[0]} Soyisim: {bilgiler[1]}\nTc: {bilgiler[2]}\nMeslek: {bilgiler[3]}\nMaaş: {bilgiler[4]}")
                    break
    if bulundu_mu==False:
        print("Bu tc ile çalışan bulunamamıştır")

def calisan_sil():
    silinecek_tc=input("Silmek istediğiniz çalışan tcsini giriniz: ")
    with open("calisan_bilgileri.txt","r",encoding="utf-8") as dosya:
        satirlar=dosya.readlines()
    silindi_mi=False
    hata_var_mi=False
    with open("calisan_bilgileri.txt","w",encoding="utf-8") as dosya:
        for satir in satirlar:
            bilgiler=satir.strip().split(",")
            if len(bilgiler)!=5:
                if silinecek_tc in satir:
                    silindi_mi=True
                    hata_var_mi=True
                else:
                    dosya.write(satir)
            else:
                tc=bilgiler[2]
                if silinecek_tc==tc:
                    silindi_mi=True
                    silinen_isim = bilgiler[0]
                    silinen_soyisim=bilgiler[1]
                         
                else:
                    dosya.write(satir)
        if silindi_mi==True:
            if hata_var_mi==True:
                print("Veri hatası olan dosya silindi")
            else:
                print(f"{silinen_isim} {silinen_soyisim} adlı çalışanın kaydı silindi.")

def not_gir():
    not_tc=input("Notunu girmek istediğiniz öğrencinin tcsini giriniz: ")
    with open("ogrenci_bilgileri.txt","r",encoding="utf-8") as dosya:
        satirlar=dosya.readlines()
    ogrenci_bulundu=False
    hata_var=False
    for satir in satirlar:
        bilgiler=satir.strip().split(",")
        if len(bilgiler)>=5:
            karsilastirilacak_tc=bilgiler[2]
            if karsilastirilacak_tc==not_tc:
                 ogrenci_bulundu=True
                 break
        else:
            if not_tc in satir:
                hata_var=True
                break
    if hata_var==True:
        print("HATA\nYöneticiye bildirin")
    if ogrenci_bulundu==True:
        not1=input(f"{bilgiler[0]} {bilgiler[1]} isimli öğrencinin vize notunu giriniz: ")
        not2=input(f"{bilgiler[0]} {bilgiler[1]} isimli öğrencinin final notunu giriniz: ")
        with open("ogrenci_bilgileri.txt","w",encoding="utf-8") as dosya:
            for satir in satirlar:
                if not_tc in satir:
                    dosya.write(f"{bilgiler[0]},{bilgiler[1]},{bilgiler[2]},{bilgiler[3]},{bilgiler[4]},{not1},{not2}\n")
                    print(f"{bilgiler[0]} {bilgiler[1]} isimli öğrencinin notları kaydedildi\nVize:{not1} Final:{not2}")
                else:
                    dosya.write(satir)

print("-----HOŞ GELDİNİZ-----")
kullanici_adi=input("Kullanıcı Adınızı Giriniz: ").lower()
sifre=input("Şifrenizi Giriniz: ")
giris_yapildi=False

#ADMİN YÖNETİM PANELİ
if kullanici_adi=="admin" and sifre=="12345":
    giris_yapildi=True
    secim=input("1-Öğrenci İşlemleri\n" \
    "2-Çalışan İşlemleri\n" \
    "Seçiminiz: ")

    if secim=="1":  
        print("---Öğrenci İşlem Menüsü---")
        while True:
            secim=input("\n1-Yeni Öğrenci Ekle\n"
            "2-Öğrenci Bilgi Görüntüle\n"
            "3-Öğrenci Sil\n"
            "4-Çıkış\n"
            "seçiminiz: ")
            if secim=="1":
                ogrenci_ekle()
            if secim=="2":
                ogrenci_goruntule()
            if secim=="3":
                ogrenci_sil()
            if secim== "4":
                break


    if secim=="2":
        print("---Çalışan İşlem Menüsü---")
        while True:
            secim=input("\n1-Yeni Çalışan Ekle\n"
            "2-Çalışan Bilgi Görüntüle\n"
            "3-Çalışan Sil\n"
            "4-Çıkış\n"
            "seçiminiz: ")
            if secim=="1":
                calisan_ekle()
            if secim=="2":
                calisan_goruntule()
            if secim=="3":
                calisan_sil()
            if secim=="4":
                break

if not(giris_yapildi):
    #OGRETMEN / OGRENCİ KONTROLU
    ogretmen_giris=False
    ogrenci_giris=False
    ogretmen_hata=False
    ogrenci_hata=False
    
    with open("calisan_bilgileri.txt","r",encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
    for satir in satirlar:
        bilgiler=satir.strip().split(",")
        if len(bilgiler)==5:
            if "öğretmen" in satir or "ogretmen" in satir:
                isim=bilgiler[0]
                soyisim=bilgiler[1]
                tc=bilgiler[2]
                ogretmen_sifre= (f"{bilgiler[0]}_{bilgiler[1]}")
                if kullanici_adi==tc and sifre==ogretmen_sifre:
                    ogretmen_giris=True
                    break       
        else:
            if kullanici_adi in satir:
                ogretmen_hata=True


    with open("ogrenci_bilgileri.txt","r",encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
    for satir in satirlar:
        bilgiler=satir.strip().split(",")
        if len(bilgiler)>=5:
            ogrenci_isim=bilgiler[0]
            ogrenci_soyisim=bilgiler[1]
            ogrenci_tc=bilgiler[2]
            ogrenci_sifre=(f"{ogrenci_isim}_{ogrenci_soyisim}")
            if kullanici_adi==ogrenci_tc and sifre==ogrenci_sifre:
                ogrenci_giris=True
                break
        else:
            if kullanici_adi in satir:
                ogrenci_hata=True

    #OGRETMEN / OGRENCİ PANELİ
    if ogretmen_giris==True:
        print(f"Hoş geldiniz, {isim} {soyisim}")
        ogretmen_secim=input("1-Öğrenci Görüntüle\n2-Öğrenci Not Gir\nSeçiminiz.: ")
        if ogretmen_secim=="1":
            ogrenci_goruntule()
        if ogretmen_secim=="2":
            not_gir()
    
    
    elif ogrenci_giris==True:
        with open("ogrenci_bilgileri.txt","r", encoding="utf-8") as dosya:
            satirlar=dosya.readlines()
            for satir in satirlar:
                bilgiler=satir.strip().split(",")
                if len(bilgiler)>5 and bilgiler[2]==ogrenci_tc:
                    #GİRİŞ BASARILI
                    print(f"Öğrenci adı soyadı: {bilgiler[0]} {bilgiler[1]}\nVize notu: {bilgiler[5]} Final Notu: {bilgiler[6]}")
                elif len(bilgiler)==5 and bilgiler[2]==ogrenci_tc:
                    print(f"\nİsim: {bilgiler[0]} Soyisim: {bilgiler[1]}\nTc: {bilgiler[2]}\nSınıf: {bilgiler[3]}\nBölüm: {bilgiler[4]}")

            
    elif ogretmen_hata==True or ogrenci_hata==True:
        print("HATA\nYöneticiye ulaşın")
if not(giris_yapildi) and (ogrenci_giris==False) and (ogretmen_giris==False):
    print("Kullanıcı adı veya şifre hatalı")