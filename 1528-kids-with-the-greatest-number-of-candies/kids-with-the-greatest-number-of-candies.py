class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx=max(candies)
        res=[]
        for candy in candies:
            res.append(candy+extraCandies>=mx)
        return res


        

        