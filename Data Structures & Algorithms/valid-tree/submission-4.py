class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        index = defaultdict(list)

        for src, dest in edges:
            index[src].append(dest)
            index[dest].append(src)
        
        visit = set()

        def DFS(src: int, parent: int) -> bool:
            if src in visit:
                return False

            visit.add(src)

            for nei in index[src]:
                if nei == parent:
                    continue
                if not DFS(nei, src):
                    return False
            
            return True
        
        return DFS(0, -1) and len(visit) == n
