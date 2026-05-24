class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        version1 = [int(x) for x in version1]
        version2 = [int(x) for x in version2]
        if len(version1) < len(version2):
            big = version2
            small = version1
        else:
            big = version1
            small = version2
        for i in range(len(small)):
            if version1[i] > version2[i]:
                return 1
            if version2[i] > version1[i]:
                return -1
        for i in range(len(big) - len(small)):
            if big[len(small) + i] != 0:
                return 1 if big == version1 else -1
        
        return 0