class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ls = s.split()
        ls=ls [::-1]
        st= " ".join(ls)
        return st
