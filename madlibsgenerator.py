
#Dictionary holding words
from random import randint
import json

dictionary = {}
dictionary['adjectives'] = "happy", "depressed", "kind", "simple", "annoying", "calm", "lazy", "obnoxious", "abnormal", "disgusted", "guilty", "ancient", "vengeful", "cautious", "ignorant", "careless", "questionable", "impressive", "evasive"
dictionary['nouns'] = "kitten", "river", "school bus driver", "school bus", "chair", "skelaton", "king", "stranger", "country", "basketball", "politics", "DSMP member", "audience", "committee", "anxiety", "product", "student", "problem"  
dictionary['adverbs'] = "quickly", "frequently", "angrily", "bravely", "brightly", "occasionally", "accidentally", "wonderfully", "mysteriously", "correctly", "thankfully", "happily", "badly", "intensely", "gently", "curiously", "sucessfully", "overconfidently", "selfishly", "unimpressively"
dictionary['verbeds'] = "accepted", "cheated", "interrupted", "invented", "learned", "cried", "killed", "lived", "laughed at", "wanted", "joined", "phoned", "burned", "trained", "thanked", "promised"
dictionary['verbs'] = "think", "work", "cry", "die", "fall", "fight", "sing", "scream", "bark", "look sad", "collapse", "explode", "question", "contemplate their existance", "kick", "agree"

with open("words.json", "w") as file:
    json.dump(dictionary, file)
with open("words.json", "r") as file:
    dictionary = json.load(file)


#Function
def random_sentance():
    adjectives = dictionary['adjectives']
    nouns = dictionary['nouns']
    adverbs = dictionary['adverbs']
    verbeds = dictionary['verbeds']
    verbs = dictionary['verbs']

    string = "The "
    string += adjectives[randint(0,len(adjectives) - 1)] + " "
    string += nouns[randint(0,len(nouns) - 1)] + " "
    string += adverbs[randint(0,len(adverbs) - 1)] + " "
    string += verbeds[randint(0,len(verbeds) - 1)] + " "
    string += "the "
    string += adjectives[randint(0,len(adjectives) - 1)] + " "
    string += nouns[randint(0,len(nouns) - 1)] + ", "
    string += "which then proceeded to " + verbs[randint(0,len(verbs) - 1)] + "."

    return string


#Running it 50 times
sentances = ''
for i in range(50):
    result = random_sentance()
    print(result)
    sentances += result
    sentances += ' '
string = sentances


#Compression AHHHHHHHHH
print('                                  ')
print("Pre-compression: " + str(len(string)))

encoded = string
currentnumber = 0
words = string.split(" ")

for word in words:
    if currentnumber < 10:
        stringnumber = "00" + str(currentnumber)
    elif currentnumber < 100:
        stringnumber = "0" + str(currentnumber)
    else:
        stringnumber = str(currentnumber)
    
    if len(word) > 3:
        encoded = encoded.replace(word, stringnumber)

    currentnumber = int(stringnumber)
    currentnumber += 1
        
print("Compressed: " + str(len(encoded)))
print('                                  ')
print(encoded)


#Adding results to a file
with open("sentances.json", "w") as file:
    file.write(sentances)
