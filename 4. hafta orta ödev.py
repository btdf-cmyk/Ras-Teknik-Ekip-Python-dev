from abc import ABC, abstractmethod
class EnvanterEşyası(ABC):
        def __init__(self, isim, ağırlık):
          @abstractmethod 
          def kullan(self):
            pass
          @abstractmethod
          def bilgi(self): 
            pass
class Silah(EnvanterEşyası):
    def __init__(self, isim, hasar, ağırlık, dayanıklılık):
         super().__init__(isim, ağırlık)
         self.dayanıklılık=dayanıklılık
         self.hasar=hasar
    def kullan(self):
           self.dayanıklılık-=1
           print(f"{self.isim} kullanıldı. Kalan dayanıklılık:{self.dayanıklılık}")   
    def bilgi(self):
        print(f"Silah: {self.isim} | hasar: {self.hasar} | ağırlık: {self.ağırlık}")
                



class Zırh(EnvanterEşyası):
    def __init__(self, isim, dayanıklılık, koruma, ağırlık):
        super().__init__(isim, ağırlık)
        self.koruma = koruma
        self.dayanıklılık = dayanıklılık
    def kullan(self):
            self.dayanıklılık-=1
            print(f"{self.isim} kullanıldı. Kalan dayanıklılık:{self.dayanıklılık}")
    def bilgi(self):
            print(f"Zırh: {self.isim} | Koruma: {self.koruma} | ağırlık: {self.ağırlık} | dayanıklılık: {self.dayanıklılık}")




class Oyuncu:
    def __init__(self, isim, ağırlık, *args):
        self.isim = isim
        self.ağırlık = ağırlık
        self.eşyalar = list(args)
    def esya_ekle(self, *args):
     self.eşyalar.extend(args)
    def envanter_göster(self):
        print(f"{self.isim} Envanteri")
        toplam_ağırlık = sum([esya.ağırlık for esya in self.eşyalar])
        print(f"Toplam Ağırlık: {toplam_ağırlık}")
        for esya in self.eşyalar:
            esya.bilgi()    
            silah1 = Silah("Kılıç", 25, 10, 100)
    zırh1 = Zırh("Zırh", 75, 50, 15)

    # Oyuncu oluştur ve eşyaları ekle
    oyuncu1 = Oyuncu("Ahmet", 90, silah1, zırh1)

    # Envanteri göster
    oyuncu1.envanter_göster()