class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        if root is None:
            return None

        tree_sum = self.sum_of_tree(root)
        max_subtree_product = float("-inf")

        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):  # get level values
                cur_node = queue.popleft()
                child_sum = self.sum_of_tree(cur_node)
                max_subtree_product = max(max_subtree_product, (tree_sum - child_sum) * child_sum)

                if cur_node.left is not None:
                    queue.append(cur_node.left)

                if cur_node.right is not None:
                    queue.append(cur_node.right)
        
        return max_subtree_product % MOD
        
    @staticmethod 
    def sum_of_tree(root):
        if root is None:
            return None

        tree_sum = 0
        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):  # get level values
                cur_node = queue.popleft()
                tree_sum += cur_node.val

                if cur_node.left is not None:
                    queue.append(cur_node.left)

                if cur_node.right is not None:
                    queue.append(cur_node.right)
           
        return tree_sum


class Solution2:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []
        
        # Helper function to calculate sums and store them, we use DFS and store intermediary results
        # Uses DFS, goes till the end and saves node sums
        def get_sums(node):
            if not node:
                return 0
            
            # Subtree sum = current val + left sum + right sum
            current_sum = node.val + get_sums(node.left) + get_sums(node.right)
            subtree_sums.append(current_sum)
            return current_sum

        # Calculate all subtree sums and get the total tree sum
        total_sum = get_sums(root)
        
        # Iterate through stored sums to find the max product
        max_prod = 0
        for s in subtree_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        return max_prod % (10**9 + 7)

