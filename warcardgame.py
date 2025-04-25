from random import shuffle


#deck of cards to start
def deckmaker():
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
    
    return deck


#higher or lower
def value(card1, card2):
    suits = ["D", "S", "C", "H"]

    values = ["A", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "J", "Q", "K"]
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


#game
def game(deck):
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    current_card = 0
    player1deck = []
    player2deck = []

    while current_card < len(deck):
        card1 = deck[current_card]
        current_card += 1
        print(player1 + "'s card: " + card1)
        card2 = deck[current_card]
        current_card += 1
        print(player2 + "'s card: " + card2)
    
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
        winner = 'win'
    elif len(player1deck) < len(player2deck):
        winner = 'lose'
    else:
        winner = 'tie'
        
    return winner, player1, player2, player1deck, player2deck


#ACTUAL game
def gameloop():
    deck = deckmaker()

    winner, player1, player2, player1deck, player2deck = game(deck)
    if winner == player1:
        print(player1 + "wins!")
        
    elif winner == player2:
        print(player2 + " wins!")
    else:
        print("Congrats! " + player1 + ' and ' + player2 + ' tied!')




