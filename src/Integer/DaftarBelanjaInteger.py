from .BarangInteger import *

class DaftarBelanjaInteger(object):
    def __init__(self, biayaMaks: int):
        sentinel = BarangInteger("sentinel", 10, 0)
        self.__listBelanja = [sentinel]
        self.__banyakBarang = 0
        self.__biayaMaks = biayaMaks

    def tambahBarang(self, b: BarangInteger, jumlah: int):
        while (jumlah >= 1):
            self.__listBelanja.append(b)
            self.__banyakBarang += 1
            jumlah -= 1

    def urutkanBarang(self):
        self.__listBelanja.sort(key=lambda x:x.getDensity(), reverse=True)

    def getBanyakBarang(self) -> int:
        return self.__banyakBarang

    def getListBelanja(self) -> list[BarangInteger]:
        return self.__listBelanja
    
    def getBarangBelanja(self, i: int) -> BarangInteger:
        return self.__listBelanja[i]
    
    def getBiayaMaks(self) -> int:
        return self.__biayaMaks