class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1];      //反轉x  abc->cba
        if(reverse == str(x)):
            return True
        else:
            return False;
