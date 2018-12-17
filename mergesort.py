import math

def mergesort(A):
  if len(A)>1:
    m = math.floor((len(A))/2) #middle
    L = A[:m] #left of array
    R = A[m:] #right side of array
    
    #merge the sorted sub-arrays 
    mergesort(L)
    mergesort(R)
   
    i=j=k=0
    
    while i < len(L) and j < len(R):
      if (L[i] > R[j]):
        A[k]=R[j]
        j+=1 
      else:
        A[k] = L[i]
        i+=1 
      k+=1 
    
    while i< len(L):
      A[k] = L[i]
      i+=1 
      k+=1 
    
    while j<len(R):
      A[k] = R[j]
      j+=1 
      k+=1
    
  print(A)

print(mergesort([1,5,4,3,2]))
