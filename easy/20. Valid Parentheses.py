'''
class Solution:
    def isValid(self, s: str) -> bool:
      index = len(s)
      while(index != 0):
        if s[index-1] == ')' and s[index-2] != '(':
          return False
          break
        elif s[index-1] == ']' and s[index-2] != '[':
          return False
          break
        elif s[index-1] == '}' and s[index-2] != '{':
          return False
          break
        return True
        index = index-2
'''
'''
class Solution:
    def isValid(self, s: str) -> bool:
      count1 = 0
      count2 = 0
      count3 = 0
      for i in range(len(s)):
        if s[i] == '(':
          count1 += 1
        elif s[i] == '[':
          count2 += 1
        elif s[i] == '{':
          count3 += 1
        elif s[i] == ')':
          count1 -= 1
        elif s[i] == ']':
          count2 -= 1
        elif s[i] == '}':
          count3 -= 1
      if count1 == 0 and count2 == 0 and count3 == 0:
        return True
      return False
'''
