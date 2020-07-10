def intersection(arrays):
    """
    YOUR CODE HERE

    add the first list to the cache with each digit as key and the value as one
    add each successive list to the cache, only if the digit already exists. if it exists increase the value by one.

    for each item in the cache:
        if the value is equal to the number of arrays, add it to the result.

    return result

    """


    
    # Your code here

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
