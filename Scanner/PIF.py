from prettytable import PrettyTable

class PIF:
    def __init__(self):
        self.__content = []

    def addToken(self, elem, stPos):
        self.__content.append((elem, stPos))

    def writePIF(self):
        table = PrettyTable(['TOKEN', 'ST_POS'])
        for item in self.__content:
            table.add_row([item[0], item[1]])
        file = open('PIF.txt', 'w')
        file.write(str(table))
        file.close()

    def __str__(self):
        table = PrettyTable(['TOKEN', 'ST_POS'])
        for item in self.__content:
            table.add_row([item[0], item[1]])
        return str(table)