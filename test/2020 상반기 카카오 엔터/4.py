
import collections
import heapq
import itertools
import math

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        heapq.heappush(self.queue, item)

    def pop_min(self):
        return heapq.heappop(self.queue)[1]

    def update_priority(self, key, priority):
        for v in self.queue:
            if v[1] == key:
                v[0] = priority
        heapq.heapify(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = collections.defaultdict(lambda: [])

    def add_edge(self, v, u, w):
        self.graph[v].append((u, w))

def dijkstra(graph, start):
    Q = PriorityQueue()
    distances = dict.fromkeys(graph.vertices, math.inf)
    parent_vertices = dict.fromkeys(graph.vertices, None)

    distances[start] = 0

    def update(u, v, w):
        if distances[v] > distances[u] + w:
            distances[v] = distances[u] + w
            Q.update_priority(v, distances[v])
            parent_vertices[v] = u

    for v in graph.vertices:
        Q.insert([distances[v], v])

    while not Q.is_empty():
        u = Q.pop_min()
        for v, w in graph.graph[u]:
            update(u, v, w)

    return distances, parent_vertices

def get_minimum_cost(start, end):
    distances, parent_vertices = dijkstra(graph, start)
    if distances[end] == math.inf:
        return -1
    return distances[end]

n, m = map(int, input().split())

graph = Graph(["".join(comb) for comb in itertools.product(('o', 'x'), repeat=n)])

for _ in range(m):
    s1, s2, cost = input().split()
    graph.add_edge(s1, s2, int(cost))

q = int(input())

inputs = [input().split() for _ in range(q)]
for s1, s2 in inputs:
    print( get_minimum_cost(s1, s2) )
