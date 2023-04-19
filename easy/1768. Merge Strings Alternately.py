class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      result = []
      max_length = 0
      if len(word1) >= len(word2):   //找比較長的字串
        max_length = len(word1)
      else:
        max_length = len(word2)
      for i in range(max_length):
        if i < len(word1):
          result.append(word1[i])
        if i < len(word2):
          result.append(word2[i])
      return "".join(result)          //用join把arrray變string
