class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cnt = {}
        for s in strs:
            freq = [0 for i in range(0,26)]
            for i in s:
                freq[ord(i) - ord('a')] +=1
            
            key = tuple(freq)
            if key in cnt:
                cnt[key].append(s)

            else:
                cnt[key] = [s]
        
        output = []
        for k,v in cnt.items():
            output.append(v)

        return output