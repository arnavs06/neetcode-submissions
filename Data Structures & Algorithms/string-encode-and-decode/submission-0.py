class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        '''
        create new answer array to store the store the encoded strings
        append all the lengths of the words in the string + a # to separate them + the number of string
        '''

        for i in strs:
            ans.append(str(len(i)) + '#' + i)
        return ''.join(ans)


    
            
    def decode(self, s: str) -> List[str]:
        '''
        set 2 pointers, i and j and move j up until the word is complete (indicated by a # symbol)

        when that word is done, append it splicing from the start of it to the word to the last letter before the #

        '''
        ans = []
        i = 0

        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i=j+1
            j=i+length
            ans.append(s[i:j])
            i=j

        return ans