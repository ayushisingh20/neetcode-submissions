# list of strings : strs [a,a,b,b,b]
# output [[a,a],[b,b,b]]
# if input is empty or one element return that as it is in a new list
# we did solve somthing similar where we created 2 hashmaps and compared can we do that here as well ?


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)
        for i in strs:
            count = [0]*26
            for s in i:
                count[ord(s)-ord('a')]+=1 
            key = tuple(count)
            res[key].append(i)
        return list(res.values())
                
