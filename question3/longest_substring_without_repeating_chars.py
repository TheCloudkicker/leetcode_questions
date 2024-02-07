class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = 0
        char_set = set()
        left = 0

        for right in range(n):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)

            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                char_set.add(s[right])

        return max_length
        # longest_sub_string = ''

        # for i1 in range(len(s)):
        #     # If remaining chars are smaller than existing substring break from loop
        #     if len(s) - i1 <= len(longest_sub_string):
        #         break
            
        #     # If not start init array and check for
        #     sub_string = ''

        #     for i2, c in enumerate(s[i1:]):

        #         # If char repeats break and check
        #         if c in sub_string:
        #             if len(sub_string) > len(longest_sub_string):
        #                 longest_sub_string = sub_string
        #             break

        #         # If last char check and break
        #         sub_string += c
        #         if i2 + 1 == len(s) - i1:
        #             if len(sub_string) > len(longest_sub_string):
        #                 longest_sub_string = sub_string
        
        # return len(longest_sub_string)
        



if __name__ == '__main__':
    sol = Solution()
    a1 = sol.lengthOfLongestSubstring("abcabcbb")
    print("a1:", a1)

    a2 = sol.lengthOfLongestSubstring("bbbbb")
    print("a2:", a2)

    a3 = sol.lengthOfLongestSubstring("pwwkew")
    print("a3:", a3)

    a4 = sol.lengthOfLongestSubstring(" ")
    print("a4:", a4)

    a5 = sol.lengthOfLongestSubstring("aab")
    print("a5:", a5)