class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashMap= {}

        for i,n in enumerate(nums):
            dif = target - n
            if diff in myHashMap:
                return [myHashMap[dif], i]

            myHashMap[n]=i #putting the array element into the hash map
