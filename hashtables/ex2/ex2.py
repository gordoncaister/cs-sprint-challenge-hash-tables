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
    tickcache = {}
    for x in tickets:
        tickcache[x.source] = x.destination
    
    starttick = tickcache[None]

    
        
    
