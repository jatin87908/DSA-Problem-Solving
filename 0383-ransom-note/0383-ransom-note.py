class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        s= magazine
        t= ransomNote
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        for i in t:
            if i not in freq or freq[i]==0:
                return False
            else: 
                freq [i]-=1
            
        return True 