import random
article=["A","THE"]
noun=["BOY","GIRL","BAT","BALL"]
preposition=["WITH","BY"]
verb=["HIT","SAW","LIKED"]
def sentence():
    return nounphrase() + " " + verbphrase()
def nounphrase():
    return random.choice(article) + " " + random.choice(noun)
def verbphrase():
    return random.choice(verb) + " " + nounphrase() + " " + prepostionphrase()
def prepostionphrase():
    return random.choice(preposition) + " " + nounphrase()
def main():
    num=int(input("Enter no. of sentence"))
    for i in range(num):
        print(sentence())
if __name__=="__main__":
    main()