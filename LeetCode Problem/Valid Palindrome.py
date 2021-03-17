class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i)
                
        for i in range(len(l)//2):
            if l[i].lower() != l[-(i+1)].lower():
                return False
        
        return True
