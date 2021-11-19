#12. Functions 

def addTwo(x) : 
    return (x + 2) * 2  

def subtractTwo(number) : 
    return number -2 

def accel(mass, force) : 
    a = mass * force 
    return a

def printString(string) : 
    print(string)

def doSomething() :
    print('hi')

newNumber = addTwo(7)

newNumber2 = subtractTwo(8)

print(newNumber)

print(newNumber2)

doSomething()
printString('hello')
printString('My name is heri')

print(accel(2,3))