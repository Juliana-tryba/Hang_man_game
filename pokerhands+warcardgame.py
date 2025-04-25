from random import shuffle


#deck of cards to start
suits = ["H", "C", "S", "D"]

values = ["A", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K"]

deck = []

for s in range(len(suits)):
    for v in range(len(values)):
        suit = suits[s]
        value = values[v]
        card = suit + " " + value
        deck.append(card)

shuffle(deck)
shuffle(deck)
shuffle(deck)


#higher or lower (refined)
def value(card1, card2):
    card1values = card1.split(' ')
    card2values = card2.split(' ')

    value1 = values.index(card1values[1])
    value2 = values.index(card2values[1])
    if value1 > value2:
        return True
    elif value1 < value2:
        return False
    else:
        suit1 = suits.index(card1values[0])
        suit2 = suits.index(card2values[0])
        if suit1 > suit2:
            return True
        else:
            return False

#pokerhands
def pokerhands(playerdeck):
    clubstraightflush = ["C J", "C 10", "C 9", "C 8", "C 7"]
    heartstraightflush = ["H J", "H 10", "H 9", "H 8", "H 7"]
    diamondstraightflush = ["D J", "D 10", "D 9", "D 8", "D 7"]
    spadestraightflush = ["S J", "S 10", "S 9", "S 8", "S 7"]
    fourofakind = ["C", "D", "H", "S"]
    fullhouse = ["S 6", "H 6", "D 6", "C K", "H K"]
    flush = ["D J", "D 9", "D 8", "D 4", "D 3"]
    straight = ["10", "9", "8", "7", "6"]
    threeofakind = ["C", "S", "H"]
    twopair = [""]
    firstcardsuit = playerdeck[0].split(' ')[0]
    print(firstcardsuit)
    for i in range(len(playerdeck)):
        suit = []
        number = []
        values = playerdeck[i].split(" ")
        suit.append(values[0])
        number.append(values[1])
        values = ''
    
    
#battle begins
player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")


#game
current_card = 0
player1deck = []
player2deck = []

for i in range(5):
    player1deck.append(deck[i])
    del deck[i]

for i in range(5):
    player2deck.append(deck[i])
    del deck[i]

while current_card < len(deck):
    card1 = deck[current_card]
    current_card += 1
    print(player1 + "'s card: " + card1)
    card2 = deck[current_card]
    current_card += 1
    print(player2 + "'s card: " + card2)
    
    pokerhands1 = pokerhands(player1deck)
    pokerhands2 = pokerhands(player2deck)
    winner = value(card1, card2)
    if winner == True:
        player1deck.append(card1)
        player1deck.append(card2)
        print(player1 + " wins the round!")
    else:
        player2deck.append(card1)
        player2deck.append(card2)
        print(player2 + " wins the round!")

print('                                            ')        
print(player1 + "'s deck: " + str(player1deck))
print(player1 + " rounds won: " + str(len(player1deck)))
print(player2 + "'s deck: " + str(player2deck))
print(player2 + " rounds won: " + str(len(player2deck)))
print('                                            ')  

if len(player1deck) > len(player2deck):
    print(player1 + " wins!")
elif len(player1deck) < len(player2deck):
    print(player2 + " wins!")
else:
    print("Congrats! " + player1 + ' and ' + player2 + ' tied!')

