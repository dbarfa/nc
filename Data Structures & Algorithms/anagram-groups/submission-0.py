class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAna = dict()
        res = []
        for i in strs:
            sortedAna = "".join(sorted(list(i)))
            if sortedAna in dictAna:
                dictAna[sortedAna].append(i) 
            else:
                dictAna[sortedAna] = [i]
        for i,j in dictAna.items():
            res.append(j)
        return (res)