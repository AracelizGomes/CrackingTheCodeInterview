#quicksort algorithm implementation in python

#partition - given an array sort it in terms of pivot
def partition(A, start, end):
  i = start-1 #i starts before array
  pivot = A[end] #lets make pivot the last element in array
  
  for j in range(start, end): #loop through sub-array starting at j=0
    if A[j] <= pivot: #if element at j is <= pivot 
      i+=1 #increment i
      A[i],A[j] = A[j], A[i] # swap location i and j
      
  A[i+1], A[end] = A[end], A[i+1] #move pivot to be right after all values smaller than it
  return (i+1) #return partition index

def quicksort(A, start, end):
  if start < end:
    partitionIndex = partition(A, start, end) #partition index 
    
    #separately sort elements before and after partition
    quicksort(A, start, partitionIndex-1)
    quicksort(A, partitionIndex+1, end)
    
    

#Test 
n = [1,7,4,3,5,2]
quicksort(n, 0, len(n)-1)
print(n)



