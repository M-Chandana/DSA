class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range(1,n+1):
            for b in range(1,n+1):
                c_s=(a*a+b*b)
                c=int(c_s**0.5)
                if c<=n and c*c==c_s:
                    count+=1
        return count
        