from Otobus import Otobus

otobus1 =  Otobus("06T9876","Ankara","Osmaniye",10)
otobus2 =  Otobus("80TT458","Osmaniye","Ankara",5)
otobus3 =  Otobus("06RE876","İstanbul","Osmaniye",12)
otobus4 =  Otobus("34UY887","Osmaniye","İstanbul",8)

otobusler = [otobus1,otobus2,otobus3,otobus4]


def cikti_test(satislar,iadeler):
    for i in range(len(otobusler)):
        for _ in range(1,satislar[i]+1):
            otobusler[i].bilet_sat()
        for _ in range(1,iadeler[i]+1):
            otobusler[i].bilet_iade()
        otobusler[i].durum_yaz()



cikti_test(satislar = [8,6,4,10], iadeler = [1,1,2,3])
cikti_test(satislar = [11,5,13,7], iadeler = [2,2,2,2])

"""
Programin ekrana basmasi gereken çıktılar:

cikti_test(satislar = [8,6,4,10],iadeler = [1,1,2,3]) çağrısı için 
Ankara->Osmaniye güzergahında 06T9876 plakalı otobüste 3 boş 7 dolu koltuk bulunmaktadır.
Osmaniye->Ankara güzergahında 80TT458 plakalı otobüste 1 boş 4 dolu koltuk bulunmaktadır.
İstanbul->Osmaniye güzergahında 06RE876 plakalı otobüste 10 boş 2 dolu koltuk bulunmaktadır.
Osmaniye->İstanbul güzergahında 34UY887 plakalı otobüste 3 boş 5 dolu koltuk bulunmaktadır.


cikti_test(satislar = [11,5,13,7],iadeler = [2,2,2,2]) çağrısı için
Ankara->Osmaniye güzergahında 06T9876 plakalı otobüste 2 boş 8 dolu koltuk bulunmaktadır.
Osmaniye->Ankara güzergahında 80TT458 plakalı otobüste 2 boş 3 dolu koltuk bulunmaktadır.
İstanbul->Osmaniye güzergahında 06RE876 plakalı otobüste 2 boş 10 dolu koltuk bulunmaktadır.
Osmaniye->İstanbul güzergahında 34UY887 plakalı otobüste 3 boş 5 dolu koltuk bulunmaktadır.

"""