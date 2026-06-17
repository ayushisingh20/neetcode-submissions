
# anagram : is a string that contains the exact same characters as another string but order of strings can be diff 

# given 2 string resturn TRUE id anagram otherwise false 
# if else statement 

# brute force method s = n Characters, t = n characters 

# n^2 # worst case i am not sure 

# len = len 
# All characters should be there as well 




# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) !=len(t):
#             return False
        
#         t = list(t)
    
#         for i in s:
#             if i in t: 
#                 t.remove(i)
#             else: 
#                 return False
#         return True

# compare length then only move ahead 
# create hashmap of s - create empty then add key as characters and value as their count 
# create hashmap of t 
# compare by traversing through s 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        else:
            hashmap_s,hashmap_t={},{} # create 2 empty dict 
            for i in s: #0,1,2,3,4 --> if len is
                if i in hashmap_s:
                    hashmap_s[i] +=1
                else:
                    hashmap_s[i] = 1 
            for i in t: #0,1,2,3,4 --> if len is
                if i in hashmap_t:
                    hashmap_t[i] +=1
                else:
                    hashmap_t[i] = 1            
            if hashmap_s ==hashmap_t:
                return True
            else:
                return False 




# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False 
#         else:
#             if sorted(s)==sorted(t):
#                 return True 
#             else:
#                 return False

