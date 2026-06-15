# Single Layer Perceptron for AND OR Gates

import numpy as np



# Activation Function

def activation(x):

    if x >= 0:
        return 1
    else:
        return 0



# Perceptron

def perceptron(inputs, targets, lr=0.1, epochs=10):

    weights = np.zeros(
        len(inputs[0])
    )

    bias = 0


    for i in range(epochs):

        for j in range(len(inputs)):

            net = np.dot(
                inputs[j],
                weights
            ) + bias


            output = activation(net)


            error = targets[j] - output


            weights = weights + lr * error * inputs[j]

            bias = bias + lr * error


    return weights, bias



inputs = np.array(
    [
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ]
)



# AND

and_targets = np.array(
    [0,0,0,1]
)


w,b = perceptron(
    inputs,
    and_targets
)


print("AND Gate")


for x in inputs:

    print(
        x,
        "->",
        activation(
            np.dot(x,w)+b
        )
    )



# OR


or_targets = np.array(
    [0,1,1,1]
)


w,b = perceptron(
    inputs,
    or_targets
)



print("\nOR Gate")


for x in inputs:

    print(
        x,
        "->",
        activation(
            np.dot(x,w)+b
        )
    )