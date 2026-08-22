class Solution(object):
 def isPalindrome(self,n):
        result=""
        for char in n:
            if char.isalnum():
                result +=char.lower()
        return result==result[::-1]
         