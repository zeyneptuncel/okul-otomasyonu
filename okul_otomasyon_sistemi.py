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

print("-----HOŞ GELDİNİZ-----")
kullanici_adi=input("Kullanıcı Adınızı Giriniz: ")
sifre=input("Şifrenizi Giriniz: ")
