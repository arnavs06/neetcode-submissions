class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        s2 contains a permutation of s1 if you can find any consecutive order of s1 within s2

        use sliding window and sorting to check, so if any window of len(s1)in s2 contains any 
        consecutive order of s1, then it is a permutation of s1.

        so:
        
        L = 0
        R = len(s1) - 1

        if sorted(s2[L:R]) == sorted(s1):
            return True
        else:

        L,R = 0, len(s1)-1
        while L<=R:
            if sorted(s2[L:R]) == sorted(s1):
                return True
            else:
                L+=1
                R+=1
        return False
            
        s1 = "abc", s2 = "lecabee"

        "lecabee"
         L
           R
        '''
        L,R = 0, len(s1)-1
        while R < len(s2):
            if sorted(s2[L:R+1]) == sorted(s1):
                return True
            else:
                L+=1
                R+=1
        return False