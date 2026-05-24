class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        mindiff = float('inf')

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                if a > b:
                    a, b = b, a
                val = b - a
                if val < mindiff:
                    mindiff = val
                d[val].append([a, b])
        return sorted(d[mindiff])