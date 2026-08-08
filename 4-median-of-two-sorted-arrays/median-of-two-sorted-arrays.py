class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resN=sorted(nums1+nums2)
        if len(resN)%2==0:
            med1 = len(resN)//2
            med2 = med1 - 1
            median = (resN[med1] + resN[med2])/2
            return median
        else:
            ind=len(resN)//2
            return resN[ind]        