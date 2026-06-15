# Hill Climbing Algorithm

import random

# Objective Function
def objective_function(x):
    return -x**2 + 5


# Hill Climbing
def hill_climbing(start_x, step_size, max_iterations):

    current_x = start_x
    current_score = objective_function(current_x)

    for i in range(max_iterations):

        new_x = current_x + random.uniform(
            -step_size,
            step_size
        )

        new_score = objective_function(new_x)

        print(
            "Iteration",
            i + 1,
            "x =",
            round(current_x, 4),
            "f(x) =",
            round(current_score, 4)
        )

        if new_score > current_score:
            current_x = new_x
            current_score = new_score


    print("\nBest Solution")
    print("x =", round(current_x, 4))
    print("f(x) =", round(current_score, 4))


# User Input
start = float(input("Enter starting value: "))
step = float(input("Enter step size: "))
iterations = int(input("Enter number of iterations: "))


hill_climbing(start, step, iterations)