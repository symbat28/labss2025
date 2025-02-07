#1
def grams_to_ounces(grams):
    ounces = grams/28.3495231
    return ounces
grams=float(input())
print(grams_to_ounces(grams))

#2
def Ftemp_to_Ctemp(Fahrenheit):
    C = (5 / 9) * (Fahrenheit - 32)
    return C
Fahrenheit=float(input())
print(Ftemp_to_Ctemp(Fahrenheit))


#3
def slove(numheads,numlegs):
    x=(numlegs-2*numheads)/2
    y=numheads-x
    return x,y
numheads=35
numlegs=94
rabbit,chickens=slove(numheads,numlegs)
print(rabbit,chickens)


#4
def filter_prime(numbers):
    if(numbers<=1):
        return 0
    for x in range(2,numbers):
        if(numbers%x==0):
            return 0
    return 1
numbers=int(input())
if (filter_prime(numbers)):
    print("yes,it is prime number")
else:
    print("no,it isnt prime number")
print(filter_prime(numbers))


#5
from itertools import permutations
def permuta(words):
    return [''.join(x) for x in permutations(words)]
words=input()
print(permuta(words))


#6
def rever(words):
    words=words.split( )
    reversed_words=reversed(words)
    return ' '.join (reversed_words)
words=input()
print(rever(words))