class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s = dict()
        count_t = dict()
        for i,j in zip(s,t):
            count_i = count_s.get(i,0)
            count_j = count_t.get(j,0)
            count_i = count_i + 1
            count_j = count_j + 1
            count_s[i] = count_i
            count_t[j] = count_j
        if count_s==count_t:
            return True
        return False        