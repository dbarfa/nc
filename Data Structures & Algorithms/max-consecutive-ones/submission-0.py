class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp +=1
            if i == 0:
                tmp = 0
            if tmp > max:
                max = tmp
        return max