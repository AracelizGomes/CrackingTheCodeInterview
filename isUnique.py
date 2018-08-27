def isUnique(s):
  temp= []
  if s=='':
    return False
  for i in s:
    if i in temp:
      print("there are duplicates")
    else:
      temp.append(i)

str="abcbdefg"
print(isUnique(str))
