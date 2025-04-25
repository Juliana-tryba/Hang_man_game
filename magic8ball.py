from random import randint

print("Welcome to magic 8 ball!")


def magic8():
    question = input("What is your question (yes or no)? ")
    while question == "what is the magic word?":
        print("How did you know :0? its 'love'")
        question = input("What is your question (yes or no)? ")

    responses = ["Yes, definitely!", "It is certain.", "Ask again later.", "I don't think so.", "No way!", "Absolutely!", "Very doubtful.", "Better not tell you now.", "I can't tell you at this time."]
    magicword = "love"
    if magicword in question:
        print("YOU HAVE BROKEN THE PROGRAM!! NO RESPONSE FOR YOU >:(")
    else:
        answer = responses[randint(0, (len(responses) - 1))]
        print(answer)


number1 = magic8()
for i in range(1000000):
    again = input("Another question? Answer yes or no: ")
    if again == 'yes' or again == 'Yes':
        magic8()
    else:
        print("aww okay :(")
        break
