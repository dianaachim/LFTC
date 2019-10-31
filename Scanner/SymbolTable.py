from prettytable import PrettyTable
from SortedTable import SortedTable

class SymbolTable:
    def __init__(self, type):
        self.__content = SortedTable()
        self.__tableType = type

    def add(self, value):
        self.__content.add(value)
        return self.__content.getID(value)

    def getPos(self, value):
        return self.__content.getID(value)

    def writeST(self):
        table = PrettyTable(['POS', 'NAME'])
        for item in self.__content.getContent():
            table.add_row([item[1], item[0]])
        name = self.__tableType + '_ST.txt'
        file = open(name, 'w')
        file.write(str(table))
        file.close()