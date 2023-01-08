from colorama import Fore, Back, Style
import random

def greeting():
    greetings = "Hello", "Hi", "Welcome"
    print(random.choice(greetings))

def bye():
    Bye = "Titan: Bye bye", "Titan: Goodbye", "Titan: Farwell"
    print(random.choice(Bye))
    exit()

def age():
    print("My Owner's Age Is 14")
    print("But Im The Ai and I Am 1")

def joke():
    Jokelines = open('Jokes.txt', encoding='utf-8').read().splitlines()
    myline=random.choice(Jokelines)
    print("Titan: "+myline)

def cryptoPrice():
    print("Titan: Mabey invest in bitcoin or litecoin mabey etherium or possibly monero ")
    print("But it's all in your intrest though")

def explain():
    explainFile = open('explain.txt').read()
    print("Titan: "+explainFile)

def thank():
    print("Titan: Your Welcome")
    
def smarter():
    print("Titan: No I Don't As I Don't Run In Algorithm")

def feeling():
    print("Titan: Im doing alright")
    
    res = input("How are you: ")
    
    if res == 'well':
        print('Thats good')
    if res == 'Well':
        print('Thats good')
    if res == 'good':
        print('Im glad your doing good')
    if res == 'Good':
        print('Im glad your doing good')
    if res == 'bad':
        print('Well i hope you get better')
    if res == 'Bad':
        print('Well i hope you get better')