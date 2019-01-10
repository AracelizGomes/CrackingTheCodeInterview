def checkPermutation(str1, str2):
  count=0
  if (len(str1) != len(str2)):
    return False
  else:
    for i in range(len(str1)):
      if str2[i] in (str1):
          count += 1
    if count == len(str2):
      return True
    else:
      return False


print(checkPermutation("ABC", "CBA"))
print(checkPermutation("", ""))

#ANSWERED AGAIN 1/10/10
#check if two string are permutaions of eachother
def Permutation(s1,s2):
  output = "not Permutation"
  count = 0
  if len(s1)==len(s2):
    for i in range(len(s1)):
      if s1[i] in s2:
        count +=1
        if count==len(s1):
          output = "is Permutation"
  return output
  

print(Permutation("abc","cba"))
