class Solution:
    def solve(self, s):
        s = list(s)
        p1 = 0
        l = []
        for i in range(len(s)):
            if s[i] != s[p1] :
                p1 += 1
                s[p1] = s[i]
        p1 += 1
        s = s[:p1]
        return "".join(s)