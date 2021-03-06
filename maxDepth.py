
class Solution:
    def maxDepth(self, root: 'Node') -> int: 
        def dfs(node):
            if not node:
                return 0
            if not node.children:
                return 1
            
            depth = 0
            for child in node.children:
                depth = max(depth, dfs(child))
                
            return depth + 1
        
        return dfs(root)
        
        
        
