class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d={}
        for i in range(len(s)-9):
            sq=s[i:i+10]
            d[sq]=d.get(sq,0)+1
        res=[sq for sq in d if d[sq]>1]
        return res