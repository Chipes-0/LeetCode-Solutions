class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        # ()
        # ()()               (())
        # ()()() (())() ()(()) (()()) ((()))
        def bt(current, opened, closed):
            nonlocal out
            if closed == n:
                out.append(current)
                return
            if opened < n:
                bt(current + "(", opened + 1, closed)
            if opened > closed:
                bt(current + ")", opened, closed + 1)
        bt("", 0, 0)
        return out