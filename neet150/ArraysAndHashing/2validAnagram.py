def validAnagram(s:str, t:str ):
  sSorted = sorted(s)
  tSorted = sorted(t)

  if sSorted == tSorted :
    return True
  else:
    return False
  

class Solution:
    def isAnagramHash(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


print(validAnagram("anagram", "nagaram"))         # True
print(validAnagram("rat", "car"))  
sol = Solution()
print(sol.isAnagramHash("ccaa", "caca"))
print(sol.isAnagramHash("ccaa", "cacca")) 

