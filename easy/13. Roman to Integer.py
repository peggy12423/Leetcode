class Solution:
    def romanToInt(self, s: str) -> int:
      roman = { "I":1 , "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }  //s->roman
      result = 0
      for i in range(len(s)):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:    //i比i+1的對應數字還小
          result = result - roman[s[i]]                     //i對應字元為負，應該用減的
        else:
          result = result + roman[s[i]]
      return result
