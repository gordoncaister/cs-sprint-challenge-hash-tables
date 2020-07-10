#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    tickcache = {}
    
    for x in tickets:
        print(x.source,x.destination)
        tickcache[x.source] = x.destination

    starttick = tickcache['NONE']

    

    while starttick != 'NONE':
        route.append(starttick)
        starttick = tickcache[starttick]

    route.append("NONE")
    return route
    
        
    
