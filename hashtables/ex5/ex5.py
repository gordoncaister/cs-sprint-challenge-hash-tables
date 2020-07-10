# Your code here
"""
actually gonna plan this one:
I think the best thing to do here is figure out the index of the last '/' and then return the letters after that as the key and then the whole thing as the value. Then when you query files, you just lookup the key and return the value

for file in files:
    the cache key is files[lastindexof'/':] = file 

for query in queries:
    append cache[query] to result

return result
"""


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for fil in files:
        filname = fil[fil.rfind("/")+1:]
        if filname not in cache:
            cache[filname] = []
        cache[filname].append(fil)

    for query in queries:
        if query in cache:
            for url in cache[query]:
                result.append(url)

    return(result)


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    # print(finder(files, queries))

    files = []

    for i in range(40):
        files.append(f"/dir{i}/file{i}")

    for i in range(40):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(100):
        queries.append(f"nofile{i}")

    queries += [
        "file12",
        "file14",
        "file39",
        "file27"
    ]

    result = finder(files, queries)
    result.sort()

    print(result)
