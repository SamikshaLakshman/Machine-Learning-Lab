# Best First Search Algorithm

import heapq


def best_first_search(graph, heuristic, start, goal):

    pq = [(heuristic[start], start)]
    visited = set()

    while pq:

        h, node = heapq.heappop(pq)

        if node == goal:
            return "Goal Found"

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor], neighbor)
                )

    return "Goal Not Found"


# Input

n = int(input("Number of nodes: "))

graph = {}
heuristic = {}

for i in range(n):

    node = input("Node: ")

    heuristic[node] = int(
        input("Heuristic: ")
    )

    graph[node] = input(
        "Neighbors (space separated): "
    ).split()


start = input("Start node: ")
goal = input("Goal node: ")


print(
    best_first_search(
        graph,
        heuristic,
        start,
        goal
    )
)