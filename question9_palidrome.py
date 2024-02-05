class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """

        # x_str = str(x)
        # x_str_reverse = x_str[::-1]
        # return x_str == x_str_reverse

        num_array = []
        num_array_backwards = []
        if num < 0:
            num_array.append(-1)
            num_array_backwards.insert(0, -1)
            num = abs(num)

        while num > 0:
            num, digit = divmod(num, 10)
            num_array.append(digit)
            num_array_backwards.insert(0, digit)

        return num_array == num_array_backwards 




if __name__ == '__main__':
    solution = Solution()
    s1 = solution.isPalindrome(121)
    print('soulution 1:', s1)

    s2 = solution.isPalindrome(-121)
    print('soulution 2:', s2)

    s3 = solution.isPalindrome(10)
    print('soulution 3:', s3)