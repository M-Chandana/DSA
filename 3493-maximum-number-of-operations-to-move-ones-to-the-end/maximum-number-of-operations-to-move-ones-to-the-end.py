class Solution:
    def maxOperations(self, s: str) -> int:
        ones=0
        operations=0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            elif ones > 0 and s[i - 1] == '1':
                operations += ones

        return operations
        