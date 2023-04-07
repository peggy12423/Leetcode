class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        sort_strs = sorted(strs)
        first_str = strs[0]
        last_str = strs[-1]
        for i in range(min(len(first_str),len(last_str))):
            if(first_str[i] == last_str[i]):
                ans = ans + first_str[i]
        return ans
