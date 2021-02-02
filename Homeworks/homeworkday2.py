#Q1

myList = ['a','b','c','d','e','f','g','h','i','j']
newlist = []
k = len(myList)
x=int(k/2)
for i in range(x,len(myList)):
    newlist.append(myList[i])
for i in range(0,x):    
    newlist.append(myList[i])

print(newlist)    

#Q2
num = int(input("Enter a number... "))
for i in range(0,(num+1)):
    if i%2 == 0:
        print(f" {i} is even number")
    else:
        continue
