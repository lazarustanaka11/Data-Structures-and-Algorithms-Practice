class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums [0,0,1,1,1,2,2,3,3,4]
        # use iterators i and j
        #if num[i] != nums[i-1]
        # overwrite on j, and increment j

        n = len(nums)
        if n <=1:
            return n
        i=1
        j=1
        while i<n:
            if nums[i]!=nums[i-1]:
                nums[j]= nums[i]
                j+=1
            i+=1
        return j
