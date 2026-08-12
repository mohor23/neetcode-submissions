class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        l=0
        seen=Counter(s1)
        window=Counter()
        for r in range(len(s2)):
            window[s2[r]]+=1
            if r-l+1 > len(s1):
                window[s2[l]]-=1
                l+=1
            if seen == window:
                return True
        return False
            