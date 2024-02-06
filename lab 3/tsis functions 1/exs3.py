def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        if (2 * numchickens + 4 * numrabbits) == numlegs:
            return numchickens, numrabbits
    return None