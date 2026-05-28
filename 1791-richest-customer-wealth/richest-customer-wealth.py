class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=[]
        n=len(accounts)
        for i in range(n):
            res.append(sum(accounts[i]))
        return max(res)


        