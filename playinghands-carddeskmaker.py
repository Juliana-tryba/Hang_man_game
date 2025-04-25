from random import shuffle

deck = []
suit = 0
values = 0
current = ''

#very inefficeint program :3
for i in range(4):
    suit += 1
    current = ''
    values = 0
    for i in range(13):
        current = ''
        values += 1
        if values == 1:
            current += 'A'
        elif values == 2:
            current += '2'
        elif values == 3:
            current += '3'
        elif values == 4:
            current += '4'
        elif values == 5:
            current += '5'
        elif values == 6:
            current += '6'
        elif values == 7:
            current += '7'
        elif values == 8:
            current += '8'
        elif values == 9:
            current += '9'
        elif values == 10:
            current += '10'
        elif values == 11:
            current += 'J'
        elif values == 12:
            current += 'Q'
        elif values == 13:
            current += 'K'
        
        if suit == 1:
            current += 'H'
        elif suit == 2:
            current += 'C'
        elif suit == 3:
            current += 'S'
        elif suit == 4:
            current += 'D'
        deck.append(current)

print("Finished deck: ")
print(deck)

#you cant just shuffle a deck once ;)
shuffle(deck)
shuffle(deck)
shuffle(deck)
shuffle(deck)
shuffle(deck)
shuffle(deck)

print("Shuffled deck: ")
print(deck)
