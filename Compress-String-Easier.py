class Solution:
    def solve(self, s):
        l = [s[0]]
        for c in s[1:]:
            if c == l[-1]:
                continue
            else:
                l.append(c)
        return "".join(l)