class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s.lower())==sorted(t.lower()):
            return True
        else:
            return False