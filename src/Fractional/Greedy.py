from .BarangFractional import *
from .DaftarBelanjaFractional import *

class Greedy(object):
    def __init__(self, daftarBelanja: DaftarBelanjaFractional):
        self.__daftarBelanja = daftarBelanja
        self.__daftarBelanja.urutkanBarang()

    def process(self) -> tuple[list[tuple[float, str]], int]:
        temp = []
        hargaAkhir = 0

        i = 0
        while (i < len(self.__daftarBelanja.getListBelanja()) and hargaAkhir <= self.__daftarBelanja.getBiayaMaks()):
            currentBarang = self.__daftarBelanja.getBarangBelanja(i)
            i += 1

            if (not currentBarang.isPecahan()):
                max = (self.__daftarBelanja.getBiayaMaks() - hargaAkhir) // currentBarang.getHargaSatuan()
            else:
                max = (self.__daftarBelanja.getBiayaMaks() - hargaAkhir) / currentBarang.getHargaSatuan()
                max = round(max, 2)

            if (max > 0):
                if (max > currentBarang.getJumlah()): max = currentBarang.getJumlah()
                hargaAkhir += max * currentBarang.getHargaSatuan()
                temp.append((max, currentBarang.getNama()))
        return (temp, hargaAkhir)