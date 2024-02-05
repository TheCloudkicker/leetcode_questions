class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)):
            if i < len(s) -1 and m[s[i]] < m[s[i+1]]:
                total -= m[s[i]]
            else:
                total += m[s[i]]

        return total
        

if __name__ == '__main__':
    solution = Solution()
    s1 = solution.romanToInt("III")
    print('soulution 1:', s1)

    s2 = solution.romanToInt("LVIII")
    print('soulution 2:', s2)

    s3 = solution.romanToInt("MCMXCIV")
    print('soulution 3:', s3)
