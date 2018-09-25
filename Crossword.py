class Letter:
    def __init__(self, character):
        self.character = character
        self.adjacentLetters = []

    def addAdjacentLetter(self, letterObj):
        self.adjacentLetters.append(letterObj)

cross1 = [i.strip() for i in open('crossword1.csv')]

alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))

lexicographicOrder = {}
for l in alphabet:
    lexicographicOrder[l] = []

xRow = ['' for i in range(100)]
for line in cross1:
    arr = line.split(',')
    prevX = ''

    for i in range(len(arr)):
        x = arr[i]
        if x != '':
            obj = Letter(x)
            if prevX != '':
                prevX.addAdjacentLetter(obj)
            if xRow != [] and xRow[i] != '':
                xRow[i].addAdjacentLetter(obj)
            prevX = obj
            lexicographicOrder[x].append(obj)
            xRow[i] = obj
        else:
            prevX = ''
            xRow[i] = ''
    print(xRow)

def longestWord():

