# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        for a in range(len(nums)):
            if a>0 and nums[a] == nums[a-1]:
                continue
            left,right = a+1, len(nums)-1            
            while left<right:
                sum = nums[a]+nums[left]+ nums[right]
                if sum<0:
                    left +=1
                elif sum>0:
                    right -=1
                elif sum==0:
                    triplets.append([nums[a], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right: # skip duplicate left
                        if nums[left]== nums[left-1]:
                            left +=1

                    while left<right: # skip duplicate right
                        if nums[right]==nums[right+1]:
                            right -=1
        return triplets
