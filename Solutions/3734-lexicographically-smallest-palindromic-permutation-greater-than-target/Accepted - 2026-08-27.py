from collections import defaultdict

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        mid = n // 2

        count = defaultdict(int)
        for ch in s:
            count[ch] += 1

        odd_char = None
        for ch in count:
            reps = count[ch]
            if reps & 1:
                if odd_char is not None:
                    return ""
                odd_char = ch
            count[ch] //= 2
            
            
        
        def bt(index, curr, greater):
            if index == mid:
                if n & 1:
                    candidate = curr + odd_char + curr[::-1]
                else:
                    candidate = curr + curr[::-1]
                return candidate if candidate > target else ""

            start = 0 if greater else ord(target[index]) - ord('a')
            for char in range(start, 26):
                char = chr(ord('a') + char)
                if count[char]:
                    count[char] -= 1
                    out = bt(index + 1, curr + char, greater or char > target[index])
                    count[char] += 1

                    if out:
                        return out
            return ""
        out = bt(0, "", False)
        return out