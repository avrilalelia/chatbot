import random
import time

name = input("Hi! I'm Chad. What's your name? ")
time.sleep(2)

print("Oh, hello " + name + "!")
feeling = input("How are you today? ")

time.sleep(2)
if "good" in feeling.lower():
    print("I'm also feeling good!")
elif "great" in feeling.lower():
    print("Good to know that! I'm also feeling great!")
elif "not bad" in feeling.lower():
    print("Oh, okay. I hope that means you're good.")
elif "fine" in feeling.lower():
    print("Great! I'm feeling fine too")
else:
    print("I'm sorry to hear that")

time.sleep(1.5)
color = input("What's your favorite color? ")

time.sleep(2)
print("I also like " + color)

colour = ["Red", "Green", "Blue"]
print("But my favorite color is " + random.choice(colour))
weather = input("How was the weather today?")

time.sleep(2)
if "rain" in weather.lower():
    print("Yeah, it's been pretty rainy these days huh")
elif "sunny" in weather.lower():
    print("A great day to go outside!")
elif "good" or "great" or "awesome" in weather.lower():
    print("Nice to know that!")
elif "bad" or "not" in weather.lower():
    print("Be careful of your health in such weather!")
else:
    print("Well I think so too! Be mindful of your health!")

time.sleep(1.5)
answer = input("Wanna play a game with me? ")

time.sleep(2)
if "yes" or "sure" in answer:
    print("Okay then, Let's play a game called madlib. You say a random noun and I'll put it into Shakespeare's monologue randomly."
          "Be sure to pick a funny noun/word!")
    import random

    f = open("madlib.txt", "r")

    rand = f.readlines()

    noun = input("Input a word: ")

    for x in rand:
        rw = x.split(" ")
        w = random.choice(rw)
        x = x.replace(w, noun)
        print(x)
    print("Haha! Funny right?")
elif "no" in answer:
    print("Okay bye.. Maybe next time.")