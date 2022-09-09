
'''we are using a dict to store the values to the indices and use this trick to acheive
low complexity '''
def twoSum(nums,target):
    d = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in d:
            return [i,d[diff]]

        d[nums[i]] = i 


print(twoSum([1,2,3],5))


