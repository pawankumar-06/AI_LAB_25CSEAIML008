import math

# Alpha-Beta pruning function
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):

    # Base case: leaf node reached
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        # Check both children
        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )

            best = max(best, value)
            alpha = max(alpha, best)

             # beta cutoff
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        # Check both children
        for i in range(2):
            value = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best
# Main program
values = list(map(int, input("Enter the leaf node values: ").split()))

height = int(math.log2(len(values)))

alpha = -math.inf
beta = math.inf

result = alpha_beta(
    0,
    0,
    True,
    values,
    alpha,
    beta,
    height
)

print("Optimal value:", result)