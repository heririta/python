#9. Iteration by Item

fruits = ['apples','pears','strawberrys', 3 , 8 , 90]

for fruit in fruits :
    if fruit == 'pears' :
        print(fruit)
    else :
        print('not pears')

print('--------------')

for x in range (len(fruits)) : 
    if fruits[x] == 'pears' :
        print(fruits[x])
    else : 
        print('not pears')

# for x in range (0,10)
#     print(x)

