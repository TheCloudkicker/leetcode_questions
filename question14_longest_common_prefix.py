class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # common_prefix = ''
        # if len(strs) == 1: return strs[0]

        # i = 1
        # continue_checking = True
        # while continue_checking:
        #     prefs = { s[0:i] for s in strs }
        #     if len(prefs) > 1:
        #         continue_checking = False
        #     elif len(list(prefs)[0]) == len(strs[0]):
        #         common_prefix = list(prefs)[0]
        #         continue_checking = False
        #     else:
        #         common_prefix = list(prefs)[0]
        #         i += 1

        # return common_prefix

        answer = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if (first[i] != last[i]):
                print('a', first[i], last[i], answer)
                return answer
            answer += first[i]


if __name__ == '__main__':
    solution = Solution()
    s1 = solution.longestCommonPrefix(["flower", "flow", "flight"])
    print('soulution 1:', s1)

    s2 = solution.longestCommonPrefix(["dog","racecar","car"])
    print('soulution 2:', s2)

    s3 = solution.longestCommonPrefix([""])
    print('soulution 3:', s3)

    s4 = solution.longestCommonPrefix(["flower","flower","flower","flower"])
    print('soulution 4:', s4)