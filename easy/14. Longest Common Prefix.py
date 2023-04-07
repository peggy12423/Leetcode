class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first_str = strs[0]
        last_str = strs[-1]
        for j in range(min(len(first_str),len(last_str))):
            if(first_str[j] != last_str[j]):
                break
            ans = ans + first_str[j]
        return ans
