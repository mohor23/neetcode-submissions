class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        max_length=0
        seen=defaultdict(int)
        l=0
        max_count=0
        for r in range(len(s)):
            seen[s[r]]+=1
            max_count=max(max_count,seen[s[r]])
            while r-l+1-max_count>k:
                seen[s[l]]-=1
                l+=1
            max_length=max(max_length,r-l+1)
        return max_length