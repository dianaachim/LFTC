from prettytable import PrettyTable
from SortedTable import SortedTable

class SymbolTable:
    def __init__(self, type):
        self.__content = SortedTable()
        self.__tableType = type

    def add(self, value):
        self.__content.add(value)
        return self.getPos(value)

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

    def __str__(self):
        table = PrettyTable(['POS', self.__tableType + ' NAME'])
        for item in self.__content.getContent():
            table.add_row([item[1], item[0]])
        return str(table)