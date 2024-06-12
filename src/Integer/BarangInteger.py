class BarangInteger(object):
    def __init__(self, nama: str, harga: int, prioritas: int):
        self.__nama = nama
        self.__harga = harga
        self.__prioritas = prioritas
        self.__density = prioritas/harga

    def getNama(self) -> str:
        return self.__nama
    
    def getHarga(self) -> int:
        return self.__harga
    
    def getPrioritas(self) -> int:
        return self.__prioritas
    
    def getDensity(self) -> float:
        return self.__density

    def __str__(self):
        return (f"{self.__nama}")

    def __repr__(self):
        return (f"{self.__nama!r}")