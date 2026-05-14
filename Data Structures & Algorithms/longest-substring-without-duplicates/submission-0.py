class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_length = len(s)
        if s_length == 0:
            return 0
        index_start = 0
        seen = set()
        longest_substring_size = 0
        cur_substring_size = 0 
        for index_end in range(s_length):
            if ( not s[index_end] in seen ) or (index_start == index_end):
                seen.add(s[index_end])
                cur_substring_size += 1
                if cur_substring_size > longest_substring_size:
                    longest_substring_size = cur_substring_size
            else:
                while s[index_start] != s[index_end]:
                    seen.remove(s[index_start])
                    index_start += 1
                index_start += 1
                cur_substring_size = index_end - index_start + 1
        return longest_substring_size