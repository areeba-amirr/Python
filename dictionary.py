data = {
  "Areeab" : 19,
  "Haris" : 21,
  "Hasnain" : 13,
  "Hania" : 9
}
marks ={
  "Areeba" : [88,99,67,87],
  "Haris" : [33,66,77,98],
  "Hania" : (44,66,77,99)
}
print(data)
print(marks)
print(marks["Areeba"])

# newDict = {
#   [2,3,5]: "one" #Error
# }

#Dictionary Methods
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Areeba": [99,99,99,99],"Sara" : [66,77,88,99]})
print(marks)
print(marks.get("Areeba2"))
marks.pop("Hania")
print(marks)
marks.popitem()
print(marks)
data.clear()
print(data)
marks1 = marks.copy()
print(marks1)
marks.setdefault("Areeba" ,[3,5])
marks.setdefault("Areeba" ,[3,5])
print(marks)
