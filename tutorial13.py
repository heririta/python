#13. How to Read a text file 

file = open('file.txt','r')
f = file.readlines()

#print(f)

newList = []
for line in f:
#    if line[-1] == '\n' : 
        newList.append(line.strip())
#    else : 
#        newList.append(line)

print(newList)