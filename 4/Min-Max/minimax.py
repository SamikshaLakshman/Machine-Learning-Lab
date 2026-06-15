# Min-Max Algorithm


def minimax(depth, node, is_max, scores, max_depth):

    if depth == max_depth:
        return scores[node]


    if is_max:

        return max(
            minimax(depth+1,node*2,False,scores,max_depth),
            minimax(depth+1,node*2+1,False,scores,max_depth)
        )


    else:

        return min(
            minimax(depth+1,node*2,True,scores,max_depth),
            minimax(depth+1,node*2+1,True,scores,max_depth)
        )



depth = int(
    input("Enter tree depth: ")
)


leaf_nodes = 2 ** depth


scores = []


for i in range(leaf_nodes):

    scores.append(
        int(input())
    )


result = minimax(
    0,
    0,
    True,
    scores,
    depth
)


print(
    "Optimal value:",
    result
)