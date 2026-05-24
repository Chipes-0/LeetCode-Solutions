class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)

        for course, req in prerequisites:
            prereqs[course].append(req)
        
        state = [0] * numCourses
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1
            for c in prereqs[node]:
                if not dfs(c):
                    return False
            state[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True