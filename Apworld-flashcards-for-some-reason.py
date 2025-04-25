
#intro stuff
import json
from random import randint
print("Ap world review - industrialization :3 (11/8/24)")


#dictionary w/questions
flashcards = {
    'who made the flush toilet? ': 'Thomas Crapper',
    'what does the bessemer process do? ' : 'make steel',
    'what is John James Hughes known for? ': 'developing donetsk',
    'who invented the colt revolver? ': 'Samuel Colt',
    'what happened to the first colt revolver? ': 'it blew up on first use',
    'what is Sheng Xuanhuai known for? ': 'telephone lines, founded universities, imperial bank of china',
    'what do bloomers symbolize? ': 'womens rights and freedom',
    'definition of freedom? ': 'the absence of necesary action or coersion',
    'who inspired Thomas Jefferson? ': 'sir frances bacon',
    'what is John Locke known as? ': 'the father of liberalism',
    'definition of Republic? ': 'power held by the people, elect representitives',
    'definition of Democracy? ': 'citizens with power to control state through direct elections',
    'definition of Political Liberalism? ': 'political/moral philosophy based on equality and liberity',
    'from what time to what time did the English Civil War happen? ': '1642-1651',
    'what was the English Civil War about/who were the opposing parties? ': 'royalists vs parliamentains',
    'what is the trans-siberian railroad? ': 'longest railroad in the world'
    }


#file saver yaaaa
with open("flashcards.json", "r") as file:
    flashcards = json.load(file)


#asking questions
questions = []
for question in flashcards:
    questions.append(question)

askedquestions = []
correct = []

while len(askedquestions) < len(questions):
    question = questions[randint(0, (len(questions) - 1))]

    if question not in askedquestions:
        answer = input(question)
        if answer.lower() == flashcards[question].lower():
            print("Correct! :D")
            askedquestions.append(question)
            correct.append(question)
        else:
            print("Incorrect :( correct answer was: " + flashcards[question])
            
            
                         
