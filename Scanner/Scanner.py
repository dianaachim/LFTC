from codification_table import ctable
from PIF import PIF
from SymbolTable import SymbolTable
import re

def isIdentifier(token):
    token = token.strip(" ")
    print('"' + token + '"')

    return re.fullmatch(r'[A-Z]{0,7}', token) is not None

def isConstant(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None

def isEscapedQuote(line, index):
    if index == 0:
        return False
    return line[index - 1] == '\\'

def getStringToken(line, index):
    token = ''
    quote_count = 0
    while index < len(line) and quote_count < 2:
        if line[index] == '"' and not isEscapedQuote(line, index):
            quote_count += 1
        token += line[index]
        index += 1
    return token, index

class Scanner:
    def __init__(self):
        self.__codificationTable = ctable
        self.__PIF = PIF()
        self.__symbolTableConstants = SymbolTable("constant")
        self.__symbolTableIdentifiers = SymbolTable("identifier")
        self.__operators = []
        self.__separators = []
        self.__reservedWords = []
        self.fillLists()

    def fillLists(self):
        # keys = list(self.__codificationTable.keys())
        # values = list(self.__codificationTable.values())
        for i in range(2, 9):
            #self.__separators = keys[values.index(i)]
            self.__separators = self.__codificationTable.keys()

        for i in range(10, 20):
            #self.__operators = keys[values.index(i)]
            self.__operators = self.__codificationTable.keys()

        for i in range(20, 41):
            #self.__reservedWords = keys[values.index(i)]
            self.__reservedWords = self.__codificationTable.keys()

    def isPartOfOperator(self, token):
        for op in self.__operators:
            if token in op:
                return True
        return False

    def getOperatorToken(self, line, index):
        token = ''
        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1
        return token, index

    def tokenGenerator(self, line):
        token = ''
        index = 0

        while index < len(line):
            if line[index] == '"':
                if token:
                    yield token
                token, index = getStringToken(line, index)
                yield token
                token = ''

            elif self.isPartOfOperator(line[index]):
                if token:
                    yield token
                token, index = self.getOperatorToken(line, index)
                yield token
                token = ''

            elif line[index] in self.__separators:
                if token:
                    yield token
                token, index = line[index], index + 1
                yield token
                token = ''

            else:
                token += line[index]
                index += 1

        if token:
            yield token

    def tokenize(self, filename):
        lineNumnber = 0
        with open(filename, 'r') as file:
            for line in file:
                lineNumnber += 1
                for token in self.tokenGenerator(line.strip()):
                    if token == ' ':
                        continue
                    elif token in self.__codificationTable.keys():
                        self.__PIF.addToken(self.__codificationTable[token], -1)
                    elif isIdentifier(token):
                        stPos = self.__symbolTableIdentifiers.add(token)
                        self.__PIF.addToken(self.__codificationTable["identifier"], stPos)
                    elif isConstant(token):
                        stPos = self.__symbolTableConstants.add(token)
                        self.__PIF.addToken(self.__codificationTable["constant"], stPos)
                    else:
                        raise Exception("Unknown token " + token + " at line " + str(lineNumnber))
        file.close()

    def run(self, filename):
        self.tokenize(filename)
        print(self.__symbolTableConstants)
        print(self.__symbolTableIdentifiers)
        self.__symbolTableConstants.writeST()
        self.__symbolTableIdentifiers.writeST()
        print(self.__PIF)
        self.__PIF.writePIF()
