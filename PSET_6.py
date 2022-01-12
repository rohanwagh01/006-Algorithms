import math


def ez_money(D):
    """Find a sequence of commodities to exchange to get more of that
    commodity.

    Args:
        D: A list of deals, each deal is of the form (A, x, B, y)
           which means someone will give you y of B for x of A.

    Returns:
        None if no such opputunity is found, otherwise a List of
        commodities to exchange.
    """
    #CREATE Adj, w, find s
    Adj = {}
    w = {}
    nodes = set()
    for deal in D:
        A = deal[0]
        B = deal[2]
        nodes.add(A)
        nodes.add(B)
        x = deal[1]
        y = deal[3]
        #save Adj[A] = [...B...] and vice versa
        if A in Adj:
            Adj[A].append(B)
        else:
            Adj[A] = [B]
        #save w(A,B) as log(x/y) and w(B,A) as log(y/x)
        w[A,B] = math.log(x/y)
    res, parent, v = bellman_ford(Adj, w, A, nodes)
    if res:
        #now walk back to recreate loop
        output = []
        visited = {}
        for i in range(len(nodes)+1):
            output.append(v)
            visited[v] = i
            #find next
            v = parent[v]
            if v in visited:
                output = output[visited[v]:]
                output.reverse()
                return output
        output.reverse()
        return output
    else:
        if B in Adj and A in Adj[B]:
            #check if microloop, which doesn't get caught in my BF
            if w[A,B] + w[B,A] != 0: #uneven trade
                return [A,B]
        return None


        


'''
Note that the relax() method is the only thing not provided to you.
You will need to implement it on your own!
'''

def bellman_ford(Adj, w, s, n): # Adj: adjacency list, w: weights, s: start
    # initialization
    infinity = float('inf') # number greater than sum of all + weights
    d = {_:infinity for _ in n} # shortest path estimates d(s, v)
    parent = {_:None for _ in n} # initialize parent pointers
    d[s], parent[s] = 0, s # initialize source
    # construct shortest paths in rounds
    V = len(Adj) # number of vertices
    for i in range(V - 1): # relax all edges in (V - 1) rounds
        for u in Adj: # loop over all edges (u, v)
            for v in Adj[u]: # relax edge from u to v
                relax(Adj, w, d, parent, u, v)
    # check for negative weight cycles accessible from s
    for u in Adj: # Loop over all edges (u, v)
        for v in Adj[u]:
            if d[v] > d[u] + w[u,v]: # If edge relax-able, report cycle
                return True,parent,v
    return False,parent,d

def relax(Adj, w, d, parent, u, v):
    #update d[v] to have the smallest distance to v and also update parent with the new parent value if this happened
    if d[v] > d[u] + w[u,v]: #if relaxable
        d[v] = d[u] + w[u,v] #update d
        parent[v] = u #update parent

print(ez_money([('node_2', 18, 'node_4', 1), ('node_2', 6, 'node_7', 8), ('node_4', 7, 'node_6', 5), ('node_4', 6, 'node_5', 1), ('node_5', 8, 'node_8', 4), ('node_5', 8, 'node_9', 3), ('node_6', 8, 'node_4', 15), ('node_7', 17, 'node_3', 5), ('node_7', 7, 'node_9', 15), ('node_8', 9, 'node_2', 3)]))