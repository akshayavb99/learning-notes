---
title: Leetcode 133 - Clone Graph
tags:
  - leetcode
  - neetcode-150-list
  - python
  - graph
  - bfs
updated_date: 2026-07-20
url: https://leetcode.com/problems/clone-graph/
---

# Leetcode 133 - Clone Graph

## Understanding the Problem

The goal is to create a **deep copy** of a connected undirected graph. Each node in the graph contains:

- A unique integer value (`val`)
- A list of neighboring nodes (`neighbors`)

A deep copy means every node in the original graph must have a newly created counterpart with the same value and neighbor relationships, but without sharing any references with the original graph.

A natural approach is to perform a **Breadth-First Search (BFS)** starting from the given node while maintaining a mapping from original nodes to their cloned nodes.

- **State Tracking:** A dictionary `old_to_new` maps each original node to its cloned node. This ensures each node is cloned exactly once and prevents infinite traversal caused by cycles.
- **Initialization:** Clone the starting node and place the original node into the BFS queue.
- **Traversal:** For every node dequeued:
  - Visit each of its neighbors.
  - If a neighbor has not yet been cloned, create its clone, store it in the dictionary, and enqueue the original neighbor.
  - Append the cloned neighbor to the cloned current node's `neighbors` list.
- **Cycle Handling:** Since graphs may contain cycles, checking whether a node already exists in `old_to_new` prevents revisiting and recloning the same node.

---

## Solution Implementation

### Code

```python
from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)

                old_to_new[curr].neighbors.append(old_to_new[nei])

        return old_to_new[node]
```

### Time Complexity

Each node is visited exactly once during the BFS traversal, and every edge is processed exactly once when building the neighbor lists of the cloned graph.

For a graph with `V` vertices and `E` edges:

**Overall time complexity — $O(V + E)$**

### Space Complexity

- **Hash Map:** Stores one cloned node for every original node, requiring $O(V)$ space.
- **Queue:** In the worst case, the BFS queue may contain up to $O(V)$ nodes.
- The cloned graph itself also contains $O(V + E)$ nodes and edges, but this is required output space and is typically not counted as auxiliary space.

**Overall auxiliary space complexity — $O(V)$**

---

## Key Takeaways

- Use a hash map to maintain a one-to-one mapping between original nodes and cloned nodes.
- Clone each node **only once**. Reuse the existing clone whenever the node is encountered again.
- The hash map simultaneously serves as a **visited set**, preventing infinite loops in cyclic graphs.
- As each original edge is traversed, connect the corresponding cloned nodes to reconstruct the graph structure.

---

## Additional Resources

- https://neetcode.io/problems/clone-graph
- https://leetcode.com/problems/clone-graph/
