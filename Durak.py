class LogicEngine:
    def __init__(self):
        self.board = []
    def addToBoard(self, card):
        self.board.append(card)
    def printBoard(self):
        print(", ".join(self.board))


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def getName(self):
        return self.name

    def getHand(self):
        return self.hand

    def attack(self):
        userInput = ""
        while userInput not in self.hand:
            userInput = input('Attack:\t')
        return userInput

    def defend(self):
        userInput = ""
        while userInput not in self.hand:
            userInput = input('Defend:\t')
        return userInput

def findPlayerWithLowestTrumpCard(players, trumpCard):
    lowestTrumpCard = ""
    playerWithLowestTrump = ""
    for i in players:
        p = players[i]
        for c in p.getHand():
            if c[1] == trumpCard[1]:
                if c[0] == '6':
                    return p.getName()
                elif lowestTrumpCard == "" or \
                    rank.index(c[0]) > rank.index(lowestTrumpCard):
                    lowestTrumpCard = c[0]
                    playerWithLowestTrump = p.getName()
    return playerWithLowestTrump


import random
suit = ['h', 'c', 'd', 's']
rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6']

deck = [r+s for s in suit for r in rank]
#for s in suit:
    #for r in rank:
        #deck.append(r + s)
random.shuffle(deck)
trumpCard = deck[-1]

players = {}

numberOfPlayers = int(input('How many players?\t'))
for p in range(numberOfPlayers): #for (i = 0; i<numberOfPlayers; i++)
    playerName = input('Name of Player?\t', )
    players[playerName] = Player(playerName, deck[:6]) #create player with name and give him 6 cards
    del deck[:6] #remove 6 cards from deck
print('Trump Card is:\t' + trumpCard)

for p in players:
    print(players[p].getName() + '\t' + ", ".join(players[p].getHand()))


firstPlayer = findPlayerWithLowestTrumpCard(players, trumpCard)
print('First Player is:\t' + firstPlayer)

board = LogicEngine()
attackingPlayer = players[firstPlayer]
defendingPlayer = [players[p] for p in players if players[p].getName != firstPlayer][0]


while True:
    card1 = attackingPlayer.attack()
    board.addToBoard(card1)
    board.printBoard()
    defendingPlayer.defend()





