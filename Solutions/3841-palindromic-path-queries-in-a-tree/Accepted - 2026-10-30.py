from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        ch = [1 << (ord(c) - 97) for c in s]
        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        tin, sz, order = [0] * n, [1] * n, []
        seen, stack = [False] * n, [0]
        seen[0] = True
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = True
                    up[0][v] = u
                    stack.append(v)
        for u in reversed(order[1:]):
            sz[up[0][u]] += sz[u]
        for k in range(1, LOG):
            p = up[k - 1]
            up[k] = [p[p[v]] for v in range(n)]

        def anc(a, b):
            return 0 <= tin[b] - tin[a] < sz[a]

        def lca(u, v):
            if anc(u, v):
                return u
            for k in range(LOG - 1, -1, -1):
                if not anc(up[k][u], v):
                    u = up[k][u]
            return up[0][u]
        fw = [0] * (n + 2)

        def add(i, x):
            i += 1
            while i <= n + 1:
                fw[i] ^= x
                i += i & -i
        def get(i):
            i, r = i + 1, 0
            while i:
                r, i = r ^ fw[i], i & (i - 1)
            return r
        def flip(v, x):
            add(tin[v], x)
            add(tin[v] + sz[v], x)
        def path(a, b):
            m = get(tin[a]) ^ get(tin[b])
            return m ^ ch[lca(a, b)]
            
        for v in range(n):
            flip(v, ch[v])
        ans = []
        for q in queries:
            t, a, b = q.split()
            a = int(a)
            if t == "update":
                x = 1 << (ord(b) - 97)
                flip(a, ch[a] ^ x)
                ch[a] = x
            else:
                m = path(a, int(b))
                ans.append(m & (m - 1) == 0)
        return ans