class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.sortString(s) == self.sortString(t)

    def sortString(self, s):
        chars = list(s)
        n = len(chars)
        for i in range(n):
            for j in range(0, n-i-1):
                if chars[j] > chars[j+1]:
                    chars[j], chars[j+1] = chars[j+1], chars[j]
        return ''.join(chars)