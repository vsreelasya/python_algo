#Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        print(s)
        if ( s[::-1] == s ):
            return True
        else:
            return False
