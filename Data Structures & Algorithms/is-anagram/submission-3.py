class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anaS = "".join(sorted(list(s)))
        anaT = "".join(sorted(list(t)))
        return anaS == anaT