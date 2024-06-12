from .BarangFractional import *

class DaftarBelanjaFractional(object):
    def __init__(self, biayaMaks: int):
        self.__listBelanja = []
        self.__biayaMaks = biayaMaks

    def tambahBarang(self, b: BarangFractional):
        self.__listBelanja.append(b)

    def urutkanBarang(self):
        self.__listBelanja.sort(key=lambda x:x.getDensity(), reverse=True)

    def getListBelanja(self) -> list[BarangFractional]:
        return self.__listBelanja
    
    def getBarangBelanja(self, i: int) -> BarangFractional:
        return self.__listBelanja[i]
    
    def getBiayaMaks(self) -> int:
        return self.__biayaMaks