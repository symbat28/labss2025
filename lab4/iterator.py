#1
def generator_ss(n):
    for x in range(1,n+1):
        yield x**2
n=int(input())
for y in generator_ss(n):
    print(y)


#2
def generator_ss(n):
    for x in range(0,n+1):
        yield x
n=int(input())
result=",".join(str(y) for y in generator_ss(n))
print(result)


#3
def generator_num(s):
    for x in range(0,s+1):
        if(x%4==0 and x%3==0):
            yield x
s=int(input())
for y in generator_num(s):
    print(y)



#4
def generator_num(a,b):
    for x in range(a,b+1):
            yield x**2
a=int(input())
b=int(input())
for y in generator_num(a,b):
    print(y)



#5
def generator_num(n):
    for x in range(0,n+1):
            yield x
n=int(input())
for y in generator_num(n):
    print(y)