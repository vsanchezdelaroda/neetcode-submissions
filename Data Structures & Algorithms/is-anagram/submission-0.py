class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Arrays must have the same length
        if len(s) != len(t):
            return False
    
        char_s =  {}
        char_t = {}

        for i in range(len(s)):
            if s[i] not in char_s:
                char_s[s[i]] = 1
            else:
                char_s[s[i]] += 1
            
            if t[i] not in char_t:
                char_t[t[i]] = 1
            else:
                char_t[t[i]] += 1
        
        return char_t == char_s