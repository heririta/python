#20. Classes and Object

# x = 'string'
# y = 23
# boo = True

#print(type(x))
#print(type(y))

#z = x + y


#print(x.count('1'))


# def func() :
#     print('hello')

# func()

x = 'string'
y = 23
boo = True

class number() :
    def __init__(self, num) :
        self.var = num

    def display(self, x) :
        print(x)


num = number(23)
num.display(num.var)



