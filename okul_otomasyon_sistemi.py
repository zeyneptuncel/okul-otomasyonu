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
        bilgiler=satir.split(",")
        if not(len(bilgiler)>=4):
            if goruntulenecek_tc in satir:
                bulundu_mu=True
                print("Öğrenci bulunamadı\nVeri dosyasında hata var kontrol edin.")
                break
            else:
                continue
        else:
            tc=bilgiler[2]
            if goruntulenecek_tc==tc:
                print(f"İsim: {bilgiler[0]} Soyisim: {bilgiler[1]}\nTc: {bilgiler[2]}\nSınıf: {bilgiler[3]}\nBölüm: {bilgiler[4]}")
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
            bilgiler=satir.split(",")
            if not(len(bilgiler)>=4):
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

    if secim=="1":  #Ogrenci İslem Menüsü
        print("---Öğrenci İşlem Menüsü---")
        while True:
            secim=input("1-Yeni Öğrenci Ekle"
            "2-Öğrenci Bilgi Görüntüle"
            "3-Öğrenci Sil"
            "4-Çıkış"
            "seçiminiz: ")
            if secim=="1":
                ogrenci_ekle()
            elif secim=="2":
                ogrenci_goruntule()
            elif secim=="3":
                ogrenci_sil()
    if secim=="2":
        print("---Çalışan İşlem Menüsü---")
        secim=input("1-Yeni Çalışan Ekle"
            "2-Çalışan Bilgi Görüntüle"
            "3-Çalışan Sil"
            "4-Çıkış"
            "seçiminiz: ")
        





            


