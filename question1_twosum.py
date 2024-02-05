class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index1, num1 in enumerate(nums):
            indexes = []
            indexes.append(index1)

            for index2, num2 in enumerate(nums):
                if index2 == indexes[0]:
                    continue
                if num1 + num2 == target:
                    indexes.append(index2)
                    return indexes
            

if __name__ == '__main__':
    solution = Solution()
    nums1 = [2,7,11,15]
    target1 = 9
    s1 = solution.twoSum(nums1, target1)
    print('soulution 1:', s1)


    nums2 = [3,2,4]
    target2 = 6
    s2 = solution.twoSum(nums2, target2)
    print('soulution 2:', s2)

    nums3 = [3,3]
    target3 = 6
    s3 = solution.twoSum(nums3, target3)
    print('soulution 3:', s3)