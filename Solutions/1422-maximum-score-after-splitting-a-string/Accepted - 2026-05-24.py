class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum = [0]
        maximum = float("-inf")
        for c in s[::-1]:
            prefix_sum.insert(0, prefix_sum[0] + int(c))
        zeros = 0
        prefix_sum = prefix_sum[1:]
        for i in range(len(s)):
            if s[i] == "0":
                zeros += 1
            if zeros + prefix_sum[i] > maximum:
                maximum = zeros + prefix_sum[i]
        return maximum
