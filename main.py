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



#cikti_test(satislar = [8,6,4,10], iadeler = [1,1,2,3])
cikti_test(satislar = [11,5,13,7], iadeler = [4,3,2,1])

"""
Programin ekrana basmasi gereken çıktılar:
nereden,nereye,plaka,boş koltuk, dolu koltuk şeklinde olacak

cikti_test(satislar = [8,6,4,10],iadeler = [1,1,2,3]) çağrısı için

Ankara,Osmaniye,06T9876,3,7
Osmaniye,Ankara,80TT458,1,4
İstanbul,Osmaniye,06RE876,10,2
Osmaniye,İstanbul,34UY887,3,5

cikti_test(satislar = [11,5,13,7], iadeler = [4,3,2,1]) çağrısı için
Ankara,Osmaniye,06T9876,4,6
Osmaniye,Ankara,80TT458,3,2
İstanbul,Osmaniye,06RE876,2,10
Osmaniye,İstanbul,34UY887,2,6
"""