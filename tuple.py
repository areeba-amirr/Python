tuple1 = (1,2,3,4,5,4,5,5)
empty= () #Emplty tuple
print(type(tuple1))
tuple2 = ("Areeba",19,99.0)
print(tuple2)
print(tuple2[2])
# tuple[2] = 44.5 Error
print(tuple1.count(5))
print(tuple1.index(4))
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))
print(sorted(tuple1)) #returns list not tuple
a = sorted(tuple1)
print(a)
a[4] = 6
print(a)
#Tuple Concatination
t1 = (1,5,7)
t2 = ("Areeba",66)
print(t1+t2)
#Multiply tuple
print(t1*5)
#memebership testing
print(1 in t1)
print("Areeba" in t2)
#list <-> tuple
l1 = list(t1)
l1.append(8)
t3 = tuple(l1)
print(t3)
#tuple to variable
a,b,c,d= t3
print(a,b,c,d)
#all theseoperations are valid for strings too
