"""
this is without watching the video for this lesson
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set() # {r, a, c, e}
        list_s = list(s) #[r, a, c, e, c, a, r]
        list_t = list(t) #[c, a, r, r, a, c, e]
        ashset = set()
        for x in list_s:
            if x in hashset:
                ashset.add(x)
                hashset.remove(x)
            else:
                hashset.add(x)
        alone = next(iter(hashset))
        if alone in list_t:
            return True
        else:
            return False
# s = "racecar"
# t = "carrace"
s = "jar"
t = "jam"
print(Solution().isAnagram(s, t))