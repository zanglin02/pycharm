"""
三数之和：
    给你一个包含n个整数的数组nums
    判断nums中是否存在三个元素a，b，c ，
    使得a + b + c = 0 ？
    请你找出所有和为0且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例1：
输入：nums = [-1, 0, 1, 2, -1, -4]
输出：[[-1, -1, 2], [-1, 0, 1]]
示例2：
输入：nums = []
输出：[]
示例3：
输入：nums = [0]
输出：[]
提示：
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
import random

"""
1.列表排序
2.a循环
3.bc 由剩余列表两端开始取值，右移b 左移c 来调整和趋向0
4.注意过程中 a b c 的去重
"""

def threeSum(nums:list):
    res = []
    length = len(nums)
    # 列表少于3个元素直接返回空列表
    if length < 3:
        return res
    nums.sort()  # 排序
    for i in range(length):
        if nums[i] > 0:
            # 当a取值大于0 a+b+c一定大于0 跳出循环
            break
        if i > 0 and nums[i] == nums[i-1]:
            # a 取值去重
            continue
        left, right = i + 1, length - 1
        while left < right:
            print(i, left, right)
            sumThree = nums[i] + nums[left] + nums[right]
            if sumThree == 0:
                res.append([nums[i], nums[left], nums[right]])
                # b，c 取值去重
                while nums[left] == nums[left+1]:
                    left += 1
                while nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif sumThree > 0:
                right -= 1
            elif sumThree < 0:
                left += 1
    return res

test = [random.randint(-10,10) for i in range(10)]
print(test)
print(threeSum(test))