# name = "Areeba"
# name1 = '''Aamir'''
# name2 = 'Haris'
# print(name,name1,name2)
# print(len(name))
# # Slicing [start:end]
# print(name[0:2])
# print(name[1:4])
# print(name[4])
# print(name[-4:-1])
# print(name[:4]) #starts from 0 [0:4]
# print(name[0:]) #ends at length [0:length]
# # name[3] = 's' error
# # Silicing with skip value
me = "Areeba Muhammad Aamir"
# print(me[0:16])
# print(me[6])
# print(me[0:16:4])
# me1 = len(me[0:16:4])
# print(me1)
# no = "1234567890"
# print(no[1:8:2])

# String Builtin Functions
print(len(me))
print(me.endswith("ir")) #True
print(me.endswith("aar")) #False
print(me.endswith("r")) #True
print(me.startswith("A")) #True
print(me.startswith("a")) #False
print(me.capitalize()) #capatilized only starting character
print(me[8].capitalize())
print(me.find("amm")) #Returns first index
print(me.find("ttt")) #-1 if not found
print(me.index("m"))#return first occurance index
# print(me.index("p")) #error if not found
print(me.replace("ree","REE"))
newStr = me.replace("ree","REE")
print(newStr)
print(me.replace("am","uuu")) #replace all occurances
print(me.replace("u","b"))
print(me.lower()) #lower case entire string
print(me.upper()) #uppercase entire string
print(me.swapcase()) #upper to lower and vice versa
str1= "    hello world    "
print(str1)
print(str1.strip()) #remove spaces from both ends
print(me.isalpha()) #Check if string has only letters
print(me.isdigit()) #check if string only contains digit
str2 = "8879ghgufuf"
print(str2.isalnum()) #check if string only conatain digit+letters both or any one of them

#Fstring
name = "Areeba"
print(f"Hello {name}")
