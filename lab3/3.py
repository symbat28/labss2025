#1
class myclass:
    def _init_(ss):
        ss.string=""
    def getstring(ss):
        ss.string=input()
    def printstring(ss):
        print(ss.string.upper())
my_object=myclass()
my_object.getstring() 
my_object.printstring()

#2
class shape:
    def _init_(self):
        pass
    def area(self):
        return 0
        
class square(shape):
    def _init_(self,length):
        self.length=length
    def area(self):
        return self.length**2
    

#3
class rectangle:
    def _init_(self):
        pass
    def area(self):
        return 0
        
class square(rectangle):
    def _init_(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    

#4
class point:
    def _init_(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print (self.a ,self.b)
    def move(self,n_a,n_b):
        self.a=n_a
        self.b=n_b
    def dist(self,other):
        return(((self.a-other.a)**2+(self.b-other.b)**2)**0.5)


#5
class Bankaccount:
    def _init_(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amout):
        self.balance+=amout
        print(amout,self.balance)
    def withdraw(self,amount):
        if self.balance < amount:
             print("Withdrawal failed: Insufficient funds.")
        else:
             self.balance -= amount
             print(self.balance,amount)


#6
def is_prime(numbers):
    if(numbers<=1):
        return 0
    for x in range(2,numbers):
        if(numbers%x==0):
            return False
    return True

def filter_prime(numbers):
    print (list(filter(lambda n: is_prime(n),numbers)))