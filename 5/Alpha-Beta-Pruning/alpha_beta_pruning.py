# Alpha Beta Pruning Algorithm


def alphabeta(depth,node,maximizing,scores,max_depth,alpha,beta):

    if depth == max_depth:
        return scores[node]


    if maximizing:

        value = float('-inf')


        for i in range(2):

            value = max(
                value,
                alphabeta(
                    depth+1,
                    node*2+i,
                    False,
                    scores,
                    max_depth,
                    alpha,
                    beta
                )
            )

            alpha = max(alpha,value)


            if alpha >= beta:
                break


        return value


    else:

        value = float('inf')


        for i in range(2):

            value = min(
                value,
                alphabeta(
                    depth+1,
                    node*2+i,
                    True,
                    scores,
                    max_depth,
                    alpha,
                    beta
                )
            )

            beta = min(beta,value)


            if alpha >= beta:
                break


        return value



depth = int(
    input("Enter depth: ")
)


scores=[]


for i in range(2**depth):

    scores.append(
        int(input("Leaf value: "))
    )


result = alphabeta(
    0,
    0,
    True,
    scores,
    depth,
    float('-inf'),
    float('inf')
)


print(
    "Optimal Value:",
    result
)