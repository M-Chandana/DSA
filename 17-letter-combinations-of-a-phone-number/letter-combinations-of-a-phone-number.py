class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        phone={
            "2":"abc",
            "3":"def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result=[""]
        for digit in digits:
            new_res=[]
            for combination in result:
                for letter in phone[digit]:
                    new_res.append(combination+letter)
            result=new_res
        return result

        