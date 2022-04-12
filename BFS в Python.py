"""
BFS в Python
{'G': ['F'], 'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C'], 'E': ['D'], 'F': ['D'], 'X': [], 'Y': ['X', 'A'], 'Z': ['X'], 'V': ['Z', 'Y'], 'W': ['V']}

"""

import collections

def breadth_first_search(graph, root, peak):
    if root not in graph:
        return print(peak, root, 'No')
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print(peak, root, visited, end=' ')
    if peak in visited:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    graph = {'G': ['F'], 'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C'], 'E': ['D'], 'F': ['D'], 'X': [], 'Y': ['X', 'A'], 'Z': ['X'], 'V': ['Z', 'Y'], 'W': ['V']}
    breadth_first_search(graph, 'G', 'A')
    breadth_first_search(graph, 'Z', 'A')
    breadth_first_search(graph, 'W', 'A')
    breadth_first_search(graph, 'W', 'X')
    breadth_first_search(graph, 'QWE', 'X')
    breadth_first_search(graph, 'X', 'A')
    breadth_first_search(graph, 'X', 'X')
    breadth_first_search(graph, '1', '1')