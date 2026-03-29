class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mem = []
        k = []
        for i in nums:
            if i not in mem:
                k.append(i)
                mem.append(i)
        for i in range(len(k)):
            nums[i] = k[i]
        return len(k)