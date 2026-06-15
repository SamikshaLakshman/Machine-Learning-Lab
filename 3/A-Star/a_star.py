# A* Algorithm

import heapq


def a_star(graph, heuristic, start, goal):

    pq = [
        (heuristic[start], 0, start)
    ]

    visited = set()


    while pq:

        f, g, node = heapq.heappop(pq)


        if node == goal:
            return "Goal Found"


        if node in visited:
            continue


        visited.add(node)


        for neighbor, cost in graph[node]:

            if neighbor not in visited:

                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor)
                )


    return "Goal Not Found"



n = int(input("Number of nodes: "))

graph = {}
heuristic = {}


for i in range(n):

    node = input("Node: ")

    heuristic[node] = int(
        input("Heuristic: ")
    )

    graph[node] = []


    k = int(
        input("Number of neighbors: ")
    )


    for j in range(k):

        nbr = input("Neighbor: ")
        cost = int(input("Cost: "))

        graph[node].append(
            (nbr,cost)
        )


start = input("Start node: ")
goal = input("Goal node: ")


print(
    a_star(
        graph,
        heuristic,
        start,
        goal
    )
)