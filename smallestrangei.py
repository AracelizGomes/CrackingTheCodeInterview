'''
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

'''

class Solution:
    def smallestRangeI(self, A, K):
        x = (max(A) - K) - (min(A) + K)
        if x < 0:
            x=0
        return x
        
