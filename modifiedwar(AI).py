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
shuffle(deck)
shuffle(deck)
shuffle(deck)


#higher or lower (refined)
def value(playercard, card2):
    card1values = playercard.split(' ')
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

        
#battle begins
player1 = input("Enter your name: ")
print("VS artificial inteligence!")
player1deck = []

for i in range(5):
    player1deck.append(deck[i])
    del deck[i]


#game
current_card = 0
AIdeck = []

while len(deck) > 0:
    print("Your deck: " + str(player1deck))
    playercard = input("Card to play: ")
    current_card += 1
    print(player1 + "'s card: " + playercard)
    card2 = deck[current_card]
    current_card += 1
    print("AI's card: " + card2)
    
    winner = value(playercard, card2)
    if winner == True:
        player1deck.append(playercard)
        player1deck.append(card2)
        print(player1 + " wins the round!")
    else:
        AIdeck.append(playercard)
        AIdeck.append(card2)
        print("AI wins the round!")
    player1deck.append(deck[current_card])
    current_card += 1
    AIdeck.append(deck[current_card])

print('                                            ')        
print(player1 + "'s deck: " + str(player1deck))
print(player1 + " rounds won: " + str(len(player1deck)))
print("AI's deck: " + str(AIdeck))
print("AI rounds won: " + str(len(AIdeck)))
print('                                            ')  

if len(player1deck) > len(AIdeck):
    print(player1 + " wins!")
elif len(player1deck) < len(AIdeck):
    print("AI wins!")
else:
    print("Congrats! " + player1 + ' and AI tied!')

