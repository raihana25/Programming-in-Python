# Find the third largest number in a list.
l=[1,9,2,8,3,7,4,6,5]
ldup=l
print(ldup)
ldup.remove(max(ldup))
ldup.remove(max(ldup))
print(max(ldup))