class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        out = 0
        possible = []
        def backtracking(current: int, nums: str):
            nonlocal out, possible
            if current > amount:
                return
            elif current == amount:
                sort = "".join(sorted(nums))
                if sort not in possible:
                    out += 1
                    possible.append(sort)
                return
            for coin in coins:
                current += coin
                nums += str(coin)
                backtracking(current, nums)
                current -= coin
                nums = nums[:-1]
        backtracking(0, "")
        return out