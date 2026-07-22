MOD = 1000000007

class Node:
    def __init__(self, id, pid, amt, h):
        self.id = id
        self.pid = pid
        self.amt = amt
        self.h = h
        self.children = []

class BlockChain:
    def __init__(self):
        self.nodes = {}
        self.root = None

    # Step 1: Build nodes
    def add_block(self, id, pid, amt, h):
        node = Node(id, pid, amt, h)
        self.nodes[id] = node

    # Step 2: Build tree structure
    def build_tree(self):
        for node in self.nodes.values():
            if node.pid == -1:
                self.root = node
            else:
                parent = self.nodes[node.pid]
                parent.children.append(node)

    # Step 3: Validate blocks
    def validate(self, node, parent_hash):
        expected_hash = (parent_hash * 31 + node.amt) % MOD

        if node.h != expected_hash:
            return None  # prune subtree

        valid_children = []
        for child in node.children:
            valid_child = self.validate(child, node.h)
            if valid_child:
                valid_children.append(valid_child)

        node.children = valid_children
        return node

    # Step 4: Find best chain
    def find_best_chain(self):
        best = None

        def dfs(node, path, total):
            nonlocal best

            path.append(node.id)
            total += node.amt

            if not node.children:  # leaf
                candidate = (total, len(path), path.copy())

                if best is None or \
                   candidate[0] > best[0] or \
                   (candidate[0] == best[0] and candidate[1] > best[1]) or \
                   (candidate[0] == best[0] and candidate[1] == best[1] and candidate[2] < best[2]):

                    best = candidate

            for child in node.children:
                dfs(child, path, total)

            path.pop()

        dfs(self.root, [], 0)

        return best[2] if best else []

# -----------------------------

# Example Usage

blockchain = BlockChain()

data = [
(1,-1,10,10),
(2,1,5,315),
(3,1,6,316),
(4,2,4,9769),
(5,2,3,9768),
(6,3,2,9808),
(7,3,1,9807)
]

for id,pid,amt,h in data:
    blockchain.add_block(id,pid,amt,h)

blockchain.build_tree()

blockchain.root = blockchain.validate(blockchain.root, 0)

result = blockchain.find_best_chain()

print("Canonical Blockchain:", result)   
