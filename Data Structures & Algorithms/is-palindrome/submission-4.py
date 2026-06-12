class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for strr in s:
            if strr.isalnum():
                string += strr
        
        l = 0
        r = len(string) - 1
        
        while (l <= r):
            if (string[l].lower() != string[r].lower()):
                return False
            
            l += 1
            r -= 1
            
        return True
        