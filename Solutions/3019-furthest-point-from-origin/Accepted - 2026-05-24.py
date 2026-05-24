class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        viaje1 = 0
        for m in moves:
            if m in ("L_"):
                viaje1 -= 1
            else:
                viaje1 += 1
        viaje2 = 0
        for m in moves:
            if m in ("R_"):
                viaje2 += 1
            else:
                viaje2 -= 1
        return max(abs(viaje2), abs(viaje1))