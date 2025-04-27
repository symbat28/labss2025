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


#7
def has33(num):
    for x in range(len(num)-1):
        if(num[x]==3 and num[x+1]==3):
            return True
    return False 
num=list(map(int,input().split()))
print(has33(num))


#8
def spy_games(num):
    n=[0,0,7]
    for x in num:
        if x==n[0]:
            n.pop(0)
        if not n:
            return True
    return False
           
num=list(map(int,input().split()))
print(spy_games(num))


#9
def sphere_volume(r):
    volume=4/3*3.14*r**3
    return volume
r=int(input())
print(sphere_volume(r))


#10
def flist(li):
    new=[]
    for x in li :
        if(x not in new):
            new.append(x)
    return new
li=list(map(int,input().split()))
print(flist(li))


#11
def palindrome(word):
    rever_word=word[::-1]
    if(rever_word==word):
        return "Yes,is palindrome"
    else:
        return "NOOOO"
word=input()
print(palindrome(word))


#12
def histogram(num):
    for x in num:
        li='*'*x
        print(li)
num=list(map(int,input().split()))
histogram(num)


#13
from random import randint
def random_games():
    random_num=randint(1,20)
    count=0
    print("Hello!I am thinking of a number between 1 and 20.")
    print("take a guess")
    while True:
        guess=int(input("enter a number: "))
        count+=1
        if(guess<random_num):
            print("Your guess is too low.take a guess")
        elif(guess>random_num):
            print("Your guess is too hight.")
        else:
            print(f"Good job! You guessed my number in {count}guess ")
            break
random_games()

