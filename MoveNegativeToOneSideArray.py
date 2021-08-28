class Solution:
    def move_negative_to_one_side(self, nums):
        counter = 0
        neg, pos = 0, len(nums) - 1
        while neg <= pos:
            counter +=1
            if nums[neg] < 0:
                neg += 1
            elif nums[pos] <0:
                nums[neg], nums[pos] = nums[pos], nums[neg]
                neg += 1
            elif nums[pos] > 0:
                pos -= 1
        print(counter)
        return nums 
c = Solution()
res = c.move_negative_to_one_side([-12, 11, -13, -5, 6, -7, 5, -3, 11])
print(res)