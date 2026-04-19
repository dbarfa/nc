class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        s = []
        for i in range(len(arr)):
            g = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > g:
                    g = arr[j]
            s.append(g)
        return s
