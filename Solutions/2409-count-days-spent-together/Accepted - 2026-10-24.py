class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        arriveAlice = list(map(int, arriveAlice.split("-")))
        leaveAlice = list(map(int, leaveAlice.split("-")))
        
        arriveAlice = months[arriveAlice[0] - 1] + arriveAlice[1]
        leaveAlice = months[leaveAlice[0] - 1] + leaveAlice[1]

        arriveBob = list(map(int, arriveBob.split("-")))
        leaveBob = list(map(int, leaveBob.split("-")))
        
        arriveBob = months[arriveBob[0] - 1] + arriveBob[1]
        leaveBob = months[leaveBob[0] - 1] + leaveBob[1]

        if arriveAlice <= leaveBob and arriveBob <= leaveAlice:
            return min(leaveAlice, leaveBob) - max(arriveAlice, arriveBob) + 1
        return 0