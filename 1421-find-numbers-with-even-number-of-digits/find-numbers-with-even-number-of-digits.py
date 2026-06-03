class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            cnt=0
            while i!=0:
                i//=10
                cnt+=1
            res.append(cnt)
        even_nums=sum(1 for x in res if x%2==0)
        return even_nums


        

        