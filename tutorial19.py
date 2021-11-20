#19. Global vs Local Variables 

var = 9 #global variable 
loop = True

def func(x) : 
    newVar = 7 #local variables
    print(var)
    if x == 5 : 
        return newVar

def otherFunc() :
    newVar = 5 


#print(newVar)


func(2)
#otherFunc()
