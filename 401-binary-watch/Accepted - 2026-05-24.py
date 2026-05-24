class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        bits = ["0"] * 11

        def traduce(arr):
            return int("".join(arr), 2)
        
        def generate(arr, i, count):
            if i == len(arr):
                return
            if count > turnedOn:
                return
            elif count == turnedOn:
                h = traduce(arr[:4])
                m = traduce(arr[4:-1])
                if h > 11 or m > 59:
                    return
                res.append(f"{h}:{str(m).zfill(2)}")
                return 
            arr[i] = "1"
            generate(arr, i + 1, count + 1)
            arr[i] = "0"
            generate(arr, i + 1, count)
        
        generate(bits, 0, 0)
        return res