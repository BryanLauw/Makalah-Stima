from .DaftarBelanjaInteger import *
from .BarangInteger import *
from .Node import *

class BranchNBound(object):
    def __init__(self, daftarBelanja: DaftarBelanjaInteger):
        self.__daftarBelanja = daftarBelanja
        self.__daftarBelanja.urutkanBarang()
        self.__priorityQueue = []

    def head(self) -> Node:
        return self.__priorityQueue[0]

    def insertQueue(self, n: Node):
        i = 0
        found = False
        
        while (i < len(self.__priorityQueue) and (not found)):
            if (self.__priorityQueue[i].getCost() < n.getCost()):
                found = True
            else: i += 1

        self.__priorityQueue.insert(i, n)
    
    def generateRoot(self):
        barang1 = self.__daftarBelanja.getBarangBelanja(0)
        self.__priorityQueue.append(Node([], 0, self.__daftarBelanja.getBiayaMaks(), 0, barang1.getDensity()))

    def generateChild(self):
        headNode = self.head()
        self.__priorityQueue.pop(0)
        currentSolution = headNode.getListSolusi()
        barangSekarang = self.__daftarBelanja.getBarangBelanja(len(currentSolution))
        barangNext = self.__daftarBelanja.getBarangBelanja(len(currentSolution)+1)

        leftNode = Node(currentSolution + [0], headNode.getProfit(), self.__daftarBelanja.getBiayaMaks(), 
                        headNode.getWeight(), barangNext.getDensity())
        self.insertQueue(leftNode)

        rightNode = Node(currentSolution + [1], headNode.getProfit()+barangSekarang.getPrioritas(), self.__daftarBelanja.getBiayaMaks(),
                         headNode.getWeight()+barangSekarang.getHarga(), barangNext.getDensity())
        if (rightNode.isNodeValid(self.__daftarBelanja.getBiayaMaks())): self.insertQueue(rightNode)

    def finish(self) -> bool:
        headNode = self.head()
        if len(headNode.getListSolusi()) == self.__daftarBelanja.getBanyakBarang():
            for i in range(1, len(self.__priorityQueue)):
                if (self.__priorityQueue[i].getCost() > headNode.getCost()):
                    return False
            return True
        return False

    def process(self) -> list[(int, str)]:
        self.generateRoot()
        
        while not self.finish():
            self.generateChild()
        
        temp = []
        finalSolution = self.__priorityQueue[0]
        listSolution = finalSolution.getListSolusi()
        
        for i in range(len(listSolution)):
            if (listSolution[i] == 1):
                temp.append(self.__daftarBelanja.getBarangBelanja(i).getNama())
        
        ret = []
        while (len(temp) > 0):
            strHead = temp[0]
            ret.append((temp.count(strHead), strHead))
            temp = [item for item in temp if item != strHead]

        return ret