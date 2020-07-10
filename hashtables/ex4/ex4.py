def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    setnumbers = set(a)
    result = []

    cache = {}
    for num in setnumbers:
        if num >= 0:
            if num not in cache:
                cache[num] = False
        if num < 0:
            if abs(num) in cache:
                cache[num] = True

    for num in cache:
        if cache[num]:
            result.append(abs(num))
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
