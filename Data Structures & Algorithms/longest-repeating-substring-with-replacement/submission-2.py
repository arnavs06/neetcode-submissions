from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        choose up to k chars to replace in string s, performing at most k replacements to
        the string (replacing a's with b's etc)


        sliding window? to check the uniform lengths of the same character 

        "would it be cheaper to swap all A's with B's or vice versa?"

        min_swaps = min(A,B)

        ex. 

            s = "AAABABB" 

            'AAABABB'
            L
                R

        "AAABABB"



            char1, char2 = 0,0 to count letter frequency

            hashmap to check frequency? where key,val = char, amt 

        while the character is the same, move R to the right 1 char 

        else, move L one to the left, and track the length (r-l) whenever you move the window,


        char_map = defaultdict(list)
        L,Best = 0,0

        for R,c in enumerate(s):
            char_map[c]+=1

        '''
        #create hashmap, sliding window and longest singular substring
        char_map = defaultdict(int)
        L,Best = 0,0

        for R,c in enumerate(s):
            char_map[c] += 1 # one indexing
            while (R - L + 1)- max(char_map.values()) > k:
                char_map[s[L]] -= 1
                L+=1

            Best = max(Best, R-L+1)
        return Best
