'''Write a python program to take a list of integers.
Create another list with those numbers in the master list that are less than a number entered by the user.
Print the new list contents.'''
print("Enter 10 elememts")
l=[int(input("Elemnt: ")) for i in range(0,10) ]
k=int(input("Enter master elemnt"))
ldup=[l[i] for i in range(0,10) if(l[i]<k)]
print(l)
print("The slave list is",ldup)
