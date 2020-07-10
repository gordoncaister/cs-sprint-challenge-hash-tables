def intersection(arrays):
    """
    YOUR CODE HERE

    add the first list to the cache with each digit as key and the value as one
    add each successive list to the cache, only if the digit already exists. if it exists increase the value by one.

    for each item in the cache:
        if the value is equal to the number of arrays, add it to the result.

    return result

    """

    cache ={}

    for i in arrays[0]:
        cache[i] = 1

    for i in range(len(arrays)-1):
        for j in arrays[i+1]:
            if j in cache:
                cache[j]+=1
    results = []
    for i in cache:
        if cache[i] == len(arrays):
            results.append(i)
    
    return results

    # Your code here




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
