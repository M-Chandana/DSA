import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        g=nums[0]
        for x in nums:
            g=math.gcd(g,x)
        if g!=1:
            return -1
        ones=nums.count(1)
        if ones>0:
            return n-ones
        min_len=float('inf')
        for i in range(n):
            g=0
            for j in range(i,n):
                g=math.gcd(g,nums[j])
                if g==1:
                    min_len=min(min_len,j-i+1)
                    break
        return (min_len-1)+(n-1)
