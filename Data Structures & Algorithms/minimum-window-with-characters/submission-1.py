class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_dic = {}
        for c in t:
            t_dic[c] = 1 + t_dic.get(c,0)

        l,r = 0,0
        window = {}
        min_len = float('inf')
        res = None
        match = 0

        for r in range(0, len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in t and window[c] == t_dic[c]:
                match +=1
            
            while match == len(t_dic):
                if r-l +1 < min_len:
                    min_len =  r - l +1
                    res = [l,r]
            
                rem = s[l]

                if rem in t_dic and window[rem] == t_dic[rem]:
                    match -=1
                window[rem] -=1
                l +=1

        if min_len == float('inf'):
            return ''

        l ,r = res
        return s[l:r+1]



