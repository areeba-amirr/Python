set = {} #Empty Dictionary
set1 = {3,5,6,7} #Set
set2 = () #empty set
print(type(set) ,type(set1))
set1= {1,2,3,4,4,4,4,6,7,4,8,8,9,7,9,"Areeba",55.6}
print(set1)
#Set Methods
set1.add(44)
print(set1)
set1.add("Hania")
print(set1)
print(len(set1))
set1.remove(4)
print(set1)
set1.discard(66)
set1.pop()
print(set1)
set1.clear()
print(set1)
#Union
s1 = {4,5,6,78,8}
s2 = { 4,5,6,78,8,9,76}
print(s1.union(s2))
#or
print(s1 | s2)
#intersection
print(s1.intersection(s2))
#or
print(s1 & s2)
#Difference
print(s1 - s2 , s1.difference(s2))
#Symmetric Difference
print(s1^s2)
#subset
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s1.isdisjoint(s2))
