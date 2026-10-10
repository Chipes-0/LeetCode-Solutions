class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        class DSU:
            def __init__(self, n):
                self.rank = [0] * n
                self.parent = [0] * n

                for i in range(n):
                    self.parent[i] = i
            
            def find(self, num):
                if self.parent[num] != num:
                    self.parent[num] = self.find(self.parent[num])
                return self.parent[num]

            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return
                if self.rank[ra] < self.rank[rb]:
                    self.parent[ra] = rb
                elif self.rank[ra] > self.rank[rb]:
                    self.parent[rb] = ra
                else:
                    self.parent[rb] = ra
                    self.rank[ra] += 1
        
        unique_mails = dict()
        email_to_name = dict()
        count = 0
        for acc in accounts:
            name = acc[0]
            for mail in acc[1:]:
                email_to_name[mail] = name
                if mail not in unique_mails:
                    unique_mails[mail] = count
                    count += 1
    
        N = len(unique_mails)
        dsu = DSU(N)
        for user in accounts:
            mail = user[1]
            for alternate in user[1:]:
                a = unique_mails[mail]
                b = unique_mails[alternate]
                dsu.union(a, b)
        
        groups = {}
        for mail, idx in unique_mails.items():
            root = dsu.find(idx)
            if root not in groups:
                groups[root] = []
            groups[root].append(mail)

        out = []
        for group in groups.values():
            name = email_to_name[group[0]]
            val = [name] + sorted(group)
            out.append(val)
        return out
            