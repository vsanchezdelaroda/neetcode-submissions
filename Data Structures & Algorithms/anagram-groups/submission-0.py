class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        dict_res = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in dict_res:
                dict_res[sorted_s] = [s]
            else:
                dict_res[sorted_s].append(s)
            
        return list(dict_res.values())