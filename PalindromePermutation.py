#method to find all perumtations of a string 
from itertools import permutations

def allPermutations(s):
  permList = list(permutations(s)) #list of all perumtaions of s in list form
  stringPermList = [] 
  # take out spaces, and convert each permutation from list to string and add to list declared above
  for perm in permList:
    stringPermList.append("".join(perm).replace(" ",""))
  return stringPermList

def Palindrome(s):
  permList = allPermutations(s) #list of strings which are perumtations of s
  palindromeList = []
  #index through permutations and if the reverse of the permutation is the same its a palindrome 
  #so we add the palindrome to the palindromeList
  for i in range(len(permList)):
    subList = list(permList[i])
    reversedsubList = list(permList[i])
    reversedsubList.reverse()
    if subList == reversedsubList:
      if permList[i] not in palindromeList:
        palindromeList.append(permList[i])
  if palindromeList != []:
    print("True permutations that are palindromes:", palindromeList)

print(Palindrome("tact coa"))
      
