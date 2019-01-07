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


#done again 1/7/19
#return True is string of Unique Characters
def Unique(s):
  if s == '':
    output = "list is null"
  arr = list(s)
  output = "Is Unique"
  for i in range(len(arr)):
    for j in range(i+1,len(arr)-1):
      if (arr[i] == arr[j]):
        output = "Is not Unique"
  
  return output


print(Unique("abs"))        
