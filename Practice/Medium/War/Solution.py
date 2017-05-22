import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Player:
    def DrawCards(self):
        n = int(input())
        for i in range(n):
            c = input()
            self.cards.append(c)
    def GetCard(self):
        result = self.cards[0]
        self.cards.pop(0)
        self.cards_queue.append(result)
        return result
    def HandLost(self):
        result = self.cards_queue
        self.cards_queue = []
        return result
    def HandWin(self, v, pos):
        if pos == 1:
            #I am First
            for i in self.cards_queue:
                self.cards.append(i)
            for i in v:
                self.cards.append(i)
        elif pos == 2:
            #I am Second
            for i in v:
                self.cards.append(i)
            for i in self.cards_queue:
                self.cards.append(i)
        self.cards_queue = []

    def Hand(self):
        return len(self.cards)

    def ShowHand(self):
        for i in self.cards:
            Debug(i)

    def __init__(self):
        self.cards = []
        self.cards_queue = []
        self.card_index = 0


player1 = Player()
player2 = Player()
player1.DrawCards()
player2.DrawCards()






DeckValues = []
#Deck Costs
for i in range(1, 11):
    DeckValues.append(str(i))
DeckValues += ['J', 'Q', 'K', 'A']

def play():
    if player1.Hand() < 1:
        p = 2
        return 2
    if player2.Hand() < 1:
        p = 1
        return 1
    p1c = player1.GetCard()[:-1]
    p2c = player2.GetCard()[:-1]
    p1c = DeckValues.index(p1c)
    p2c = DeckValues.index(p2c)
    if p1c == p2c:
        #Recurse until Winner!!

        for i in range(3):
            if player1.Hand() < 1:
                return -1
            if player2.Hand() < 1:
                return -1
            p1w = player1.GetCard()
            p2w = player2.GetCard()
        return play()

    if p1c > p2c:
        v = player2.HandLost()
        player1.HandWin(v, 1)
    elif p2c > p1c:
        v = player1.HandLost()
        player2.HandWin(v, 2)
    return 0

rounds = 0
p = 0
while (True):
    p = play()
    if p == 1 or p == 2:
        break
    if p == -1:
        break
    rounds += 1


if p == -1:
    print("PAT")
else:
    print(p, rounds)
