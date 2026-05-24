class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""
        for i in range(len(num)):
            if num[i:i+3] == num[i] * 3:
                if largest == "":
                    largest = int(num[i])
                elif int(num[i]) > largest:
                    largest = int(num[i])
        return str(largest) * 3