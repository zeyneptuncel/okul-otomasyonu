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
        secim=input("1-Yeni Öğrenci Ekle"
        "2-Öğrenci Bilgi Görüntüle"
        "3-Öğrenci Sil"
        "4-Çıkış"
        "seçiminiz: ")
        if secim=="1":
            ogrenci_ekle()


            


