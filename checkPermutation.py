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
