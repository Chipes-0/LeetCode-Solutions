class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr = []
        qd = []

        for i in range(len(senate)):
            if senate[i] == "R":
                qr.append(i)
            else:
                qd.append(i)
        
        while qr and qd:
            _ir = qr.pop()
            _id = qd.pop()

            if _ir < _id:
                qr.append(_ir + len(senate))
            else:
                qd.append(_id + len(senate))
        
        return "Radiant" if qr else "Dire"
