class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)[::-1]
        out = []
        for i in range(len(deck)):
            print(deck)
            if out:
                last = out.pop()
                out.insert(0, last)
            out.insert(0, deck[i])
        return out