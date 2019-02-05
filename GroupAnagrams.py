class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = dict()
        r = []
        
        for word in strs:
            sw = ''.join(sorted(word))
            if sw in d:
                d[sw].append(word)
            else:
                d[sw] = [word]
        
        for k,val in d.items():
            s = []
            for v in val:
                s.append(v)
            r.append(sorted(s))
        return r
