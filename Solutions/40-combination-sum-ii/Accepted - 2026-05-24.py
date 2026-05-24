class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        loaded = set()
        out = list()
        candidates = [x for x in candidates if x <= target]
        def bt(i, current, nums):
            nonlocal out
            if current > target or i > len(candidates):
                return
            if current == target:
                hashed = "".join([str(x) for x in sorted(nums)])
                if not hashed in loaded:
                    loaded.add(hashed)
                    out.append(nums[:])
                    return 
            for j in range(i, len(candidates)):
                current += candidates[j]
                nums.append(candidates[j])
                bt(j + 1, current, nums)
                current -= candidates[j]
                nums.pop()    
        bt(0, 0, [])
        return out