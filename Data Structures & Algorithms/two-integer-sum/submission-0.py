# list of interger --> nums .....n 
# varible interger --> target 
# i need to retun index as num[i]+num[j]== target 
# and i != j 
# output [i,j]

# empty list --> o(1)

# o(n**2)


# we need to check the first index then 
# move to the last untill we fine the right combination. 
# if condition met return indexed i and j 


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if i != j:
#                     if nums[i]+nums[j] == target:
#                         return[i,j]
#                     else:
#                         print("not possible")
#                 else: 
#                     print("not prossible")


# time compexity = o(n**2)--> how can i make it simple using hash maps ?


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        hashmap={}
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[nums[i]]=i
        return("Not possible")


