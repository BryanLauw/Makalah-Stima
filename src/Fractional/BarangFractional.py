class BarangFractional(object):
    def __init__(self, nama: str, hargaSatuan: int, prioritas: int, jumlah: float, pecahan: bool):
        self.__nama = nama
        self.__hargaSatuan = hargaSatuan
        self.__prioritas = prioritas
        self.__jumlah = jumlah
        self.__pecahan = pecahan
        self.__density = prioritas/hargaSatuan

    def getNama(self) -> str:
        return self.__nama
    
    def getHargaSatuan(self) -> int:
        return self.__hargaSatuan
    
    def getPrioritas(self) -> int:
        return self.__prioritas
    
    def getJumlah(self) -> float:
        return self.__jumlah
    
    def getDensity(self) -> float:
        return self.__density

    def isPecahan(self) -> bool:
        return self.__pecahan