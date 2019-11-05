from prettytable import PrettyTable

class SortedTable:
    def __init__(self):
        self.__content = []
        self.__lastPos = 0

    def getContent(self):
        return self.__content

    def getID(self, value):
        for i in self.__content:
            if i[0].strip(" ") == value.strip(" "):
                return i[1]
        return -1

    def sortTable(self):
        self.__content = sorted(self.__content, key = lambda t:t[0])
        sorted_table = []
        pos = 0
        for item in self.__content:
            sorted_table.append((item[0], pos))
            pos += 1
        self.__content = sorted_table

    def add(self, value):
        if self.getID(value) != -1:
            return self.getID(value)

        self.__content.append((value, self.__lastPos))
        self.__lastPos += 1
        self.sortTable()
        return self.getID(value)