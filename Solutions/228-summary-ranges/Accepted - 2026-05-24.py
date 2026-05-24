class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        r = []
        for num in nums:
            if not r:
                r.append(num)
            else:
                if num == r[len(r) - 1] + 1:
                    r.append(num)
                else:
                    if len(r) == 1:
                        output.append(str(r[0]))
                        r = [num]
                    else:
                        s = ""
                        s += str(r[0])
                        s += "->"
                        s += str(r[-1])
                        output.append(s)
                        r = [num]
        if len(r) == 1:
            output.append(str(r[0]))
        else:
            s = ""
            s += str(r[0])
            s += "->"
            s += str(r[-1])
            output.append(s)
        return output