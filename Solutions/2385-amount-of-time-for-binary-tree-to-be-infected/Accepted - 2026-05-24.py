# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        def convert_to_graph(root, val):
            if not root:
                return
            graph[val].append(root.val)
            graph[root.val].append(val)
            convert_to_graph(root.left, root.val)
            convert_to_graph(root.right, root.val)
        convert_to_graph(root.left, root.val)
        convert_to_graph(root.right, root.val)

        def bfs(graph, start):
            visited = set()
            queue = deque([(start, 0)])
            distances = {start: 0}

            while queue:
                current_node, current_distance = queue.popleft()
                if current_node not in visited:
                    visited.add(current_node)
                    for neighbor in graph.get(current_node, []):
                        if neighbor not in visited:
                            queue.append((neighbor, current_distance + 1))
                            distances[neighbor] = current_distance + 1
            return current_distance
        return bfs(graph, start)