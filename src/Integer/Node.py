class Node(object):
    def __init__(self, listSolusi: list[int], F: int, K: int, W: int, density: float):
        self.__listSolusi = listSolusi
        self.__profit = F
        self.__weight = W
        self.__cost = F + (K - W) * density

    def getListSolusi(self) -> list[int]:
        return self.__listSolusi
    
    def getCost(self) -> int:
        return self.__cost
    
    def getProfit(self) -> int:
        return self.__profit
    
    def getWeight(self) -> int:
        return self.__weight
    
    def isNodeValid(self, K) -> bool:
        return K >= self.__weight