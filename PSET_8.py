def num_opt_even_weight_paths(graph, s):
    '''
    The num_opt_even_weight_paths function should return a dictionary mapping node v to the number of optimal
    paths of even weight from s to v.

    graph - an adjacency list of a DAG in the form {u: {v:w(u,v)} mapping nodes to a dictionary 
            where the keys are their adjacencies and the values are the edge weights
            graph[u][v] would be equal to the weight of the edge u to v.
            you may assume that graph.keys() represents all nodes present
    s - start node

    return: a dictionary mapping node v to the number of optimal paths of even weight from s to v. 
            optimal[s] should be 1.
    '''
    # MAKE TOPOLOGICAL SORT OF GRAPH 
    def topo(n,v,l):
            # Mark the current node as visited.
            v[n] = True
            # Recur for all the vertices adjacent to this vertex
            for b in graph[n]:
                if v[b] == False:
                    topo(b,v,l)
            # Push current vertex to stack which stores result
            l.insert(0,n) 
    vis = {i:False for i in graph}
    stck = []
    for nd in graph:
        if vis[nd] == False:
            topo(nd,vis,stck)
    #stck is topo sort
    #REVERSE ADJ
    rv = {}
    for par in graph:
        if not par in rv:
            rv[par] = []
        for ch in graph[par]:
            if ch in rv:
                rv[ch].append(par)
            else:
                rv[ch] = [par]
    #DO BOTTOM UP IMP IN TOPO ORDER
    E = {node:float('inf') for node in graph}
    D = {node:float('inf') for node in graph}
    X_E = {node:0 for node in graph}
    X_D = {node:0 for node in graph}
    E[s] = 0
    X_E[s] = 1
    for node in stck:
        #update for this, use Try Catch so only s descendents can be operated on
        if node != s:
            ###update E | D###
            #for p in rv[node]
            E[node] = min([E[p]+graph[p][node] if graph[p][node]%2==0 else D[p]+graph[p][node] for p in rv[node]]+[E[node]]) 
            D[node] = min([D[p]+graph[p][node] if graph[p][node]%2==0 else E[p]+graph[p][node] for p in rv[node]]+[D[node]]) 
            ###update X###
            for p in rv[node]: #sum over all parents
                w = graph[p][node]
                if w%2==0: #edge even
                    if E[p] + w == E[node]: #a shortest even path
                        X_E[node] += X_E[p]
                    if D[p] + w == D[node]: #a shortest odd path
                        X_D[node] += X_D[p]
                else: #edge odd
                    if D[p] + w == E[node]: #a shortest even path
                        X_E[node] += X_D[p]
                    if E[p] + w == D[node]: #a shortest odd path
                        X_D[node] += X_E[p]
    return X_E

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""  
    #initialize the subproblems
    D = {i:float('inf') for i in graph}
    E = {i:float('inf') for i in graph}
    X = {i:0 for i in graph}
    D[s] = float('inf')
    E[s] = 0
    X[s] = 1
    #start at the start node and get all neighbors, then update each E and D
    curr = s                                                                          
    nxt = set(graph[s].keys())
    while nxt:
        if curr == 'b':
            print("hi")
        #map from current node to all nodes in it's adjecency
        for n in graph[curr]: #for key in this adj+
            if graph[curr][n]%2 == 0: #even
                E[n] = min(E[curr]+graph[curr][n], E[n])
                D[n] = min(D[curr]+graph[curr][n], D[n])
            else:
                if curr == 'b' and n == 'c':
                    print(min(D[curr]+graph[curr][n], E[n]))
                E[n] = min(D[curr]+graph[curr][n], E[n])
                D[n] = min(E[curr]+graph[curr][n], D[n])
        #now curr is done so reset the stuff, since it is possible to repeat nodes all neighbors should be added
        nxt.union(set(graph[s].keys()))
        curr = nxt.pop()
    return E,D
"""





if __name__ == "__main__":
    pass