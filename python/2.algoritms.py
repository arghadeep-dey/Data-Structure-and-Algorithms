# Algorithms
# 1. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 2. Binary Search (requires sorted array)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 3. Jump Search (requires sorted array)
import math 
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# 4. Interpolation Search (requires sorted array)
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        if pos < low or pos > high:
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# 5. Exponential Search (requires sorted array)
def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    # Binary search in the range [i/2, min(i, len(arr)-1)]
    return binary_search(arr[i // 2:min(i, len(arr))], target) + i // 2

# Sorting Algorithms
#1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 2. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# 3. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 4. Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# 5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# 6. Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# 7. Counting Sort (for non-negative integers)
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    return arr

# 8. Radix Sort (for non-negative integers)
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# 9. Bucket Sort (for uniformly distributed data)
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1) * bucket_count)
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr

# 10. Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# 11. Tim Sort (Python's built-in sorting algorithm)
def tim_sort(arr):
    return sorted(arr)

# Tree Traversal Algorithms
# 1. Tree Creation
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None  
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# 2. In-order Traversal
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)

# 3. Pre-order Traversal
def pre_order_traversal(root):
    if root:
        print(root.value, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# 4. Post-order Traversal
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=' ')

# 5. Level-order Traversal
from collections import deque
def level_order_traversal(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# 6. Depth-First Search (DFS)
def dfs(root):
    if root:
        print(root.value, end=' ')
        dfs(root.left)
        dfs(root.right)

# 7. Breadth-First Search (BFS)
def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# 8. Binary Search Tree (BST) Operations
def search_bst(root, target):
    if root is None or root.value == target:
        return root
    if target < root.value:
        return search_bst(root.left, target)
    return search_bst(root.right, target)

def delete_bst(root, target):
    if root is None:
        return root
    if target < root.value:
        root.left = delete_bst(root.left, target)
    elif target > root.value:
        root.right = delete_bst(root.right, target)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_value_node(root.right)
        root.value = temp.value
        root.right = delete_bst(root.right, temp.value)
    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# 9. Balanced Tree Check
def is_balanced(root):
    def check_balance(node):
        if node is None:
            return 0
        left_height = check_balance(node.left)
        if left_height == -1:
            return -1
        right_height = check_balance(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return check_balance(root) != -1

# 10. Lowest Common Ancestor (LCA) in BST
def lca_bst(root, n1, n2):
    while root:
        if root.value > n1 and root.value > n2:
            root = root.left
        elif root.value < n1 and root.value < n2:
            root = root.right
        else:
            return root
    return None

# 11. Lowest Common Ancestor (LCA) in Binary Tree
def lca_binary_tree(root, n1, n2):
    if root is None:
        return None
    if root.value == n1 or root.value == n2:
        return root

    left_lca = lca_binary_tree(root.left, n1, n2)
    right_lca = lca_binary_tree(root.right, n1, n2)

    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca

# Map Searching Algorithms
# 1. Hash Map Search
def hash_map_search(hash_map, key):
    return hash_map.get(key, None)

# 2. Trie Search
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# 3. Graph Search (DFS and BFS)
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph.get(node, []))

# 4. A* Search Algorithm
import heapq
def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph.get(current, []):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))
    return None

# 5. Dijkstra's Algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 6. Bellman-Ford Algorithm
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances

# 7. Floyd-Warshall Algorithm
def floyd_warshall(graph):
    nodes = list(graph.keys())
    distances = {node: {neighbor: float('inf') for neighbor in nodes} for node in nodes}

    for node in nodes:
        distances[node][node] = 0
        for neighbor, weight in graph[node].items():
            distances[node][neighbor] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

# 8. Prim's Algorithm
def prim_mst(graph):
    mst = []
    visited = set()
    min_heap = [(0, next(iter(graph)))]  # Start with an arbitrary node

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst.append((weight, node))
            for neighbor, edge_weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst

# 9. Kruskal's Algorithm
def kruskal_mst(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            edges.append((weight, node, neighbor))
    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    mst = []
    for weight, node1, node2 in edges:
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append((weight, node1, node2))

    return mst

# 10. Topological Sort
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Return reversed stack as topological order

# 11. Tarjan's Algorithm for Strongly Connected Components
def tarjan_scc(graph):
    index = 0
    stack = []
    lowlink = {}
    index_map = {}
    on_stack = set()
    sccs = []

    def strongconnect(node):
        nonlocal index
        index_map[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in index_map:
                strongconnect(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in on_stack:
                lowlink[node] = min(lowlink[node], index_map[neighbor])

        if lowlink[node] == index_map[node]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in index_map:
            strongconnect(node)

    return sccs

# 12. Kosaraju's Algorithm for Strongly Connected Components
def kosaraju_scc(graph):
    visited = set()
    stack = []

    def fill_order(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                fill_order(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            fill_order(node)

    transposed_graph = {}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in transposed_graph:
                transposed_graph[neighbor] = []
            transposed_graph[neighbor].append(node)
    visited.clear()
    sccs = []
    def dfs(node, scc):
        visited.add(node)
        scc.append(node)
        for neighbor in transposed_graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, scc)
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs(node, scc)
            sccs.append(scc)
    return sccs

