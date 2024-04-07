class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == int(str(x)[::-1]):
            return True
        else:
            return False
def _driver():
    ret = Solution().isPalindrome(param_1)
    print(ret)
