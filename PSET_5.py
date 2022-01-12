from collections import deque


def homomorphic_hash(board, prev_hash, move):
    """Update the hash of a board after applying a move in O(1) time.

    Args:
        board: An instance of the `Board` class. Please see the helper `board.py` file.
        prev_hash (int): Hash of the previous board.
        move (Tuple[int, int, int, int]): Contains (r1, c1, r2, c2) where the move will
                swap location (r1, c1) with (r2, c2). Note that (r2, c2) must be the
                hole location.
    
    Returns (int):
        Returns the hash of the board after move has been applied.
    """
    #find the values of v_1 and v_
    v_1 = board[move[0]][move[1]]
    v_2 = board[move[2]][move[3]]
    #return H_sigma(vals)
    return prev_hash ^ hash((move[0],move[1],v_1)) ^ hash((move[2],move[3],v_2)) ^ hash((move[0],move[1],v_2)) ^ hash((move[2],move[3],v_1))
    

def solve(B):
    """Find the moves that would solve the board given by `B`.

    Args:
        B: An instance of the `Board` class. Please see the `board.py` file. This is the
            starting state of the board that you need to solve.

    Returns:
        A list of moves, in the form of (r1, c1, r2, c2) that would solve `B`.
    """
    brd_solved = B.get_solved_board()
    #neighbor_dict links child:parent,move
    neighbor_dict_b = {}
    neighbor_dict_s = {}
    b_seen = {hash(B)}
    s_seen = {hash(brd_solved)}
    b_next = {B}
    s_next = {brd_solved}
    #now look through the BFS for both sides, terminate when a neighbor from B is in s_seen
    while b_next and s_next:
        neighbors = set()
        for brd_1 in s_next:
            moves = brd_1.get_legal_moves()
            #do each move
            for mv in moves:
                #do move and update seen and neighbor_dict
                brd_2 = brd_1.make_move(mv)
                h_brd_2 = hash(brd_2)
                if h_brd_2 in b_seen: #over
                    neighbor_dict_s[h_brd_2] = (hash(brd_1),(mv[2],mv[3],mv[0],mv[1]))
                    return BackTrack(neighbor_dict_b,neighbor_dict_s,hash(B),hash(brd_solved),h_brd_2)
                if not h_brd_2 in s_seen: #new neighbor
                    neighbors.add(brd_2)
                    s_seen.add(h_brd_2)
                    neighbor_dict_s[h_brd_2] = (hash(brd_1),(mv[2],mv[3],mv[0],mv[1]))
        #now neighbors are new next
        s_next = neighbors
        ###do the same for b now###
        neighbors = set()
        for brd_1 in b_next:
            moves = brd_1.get_legal_moves()
            #do each move
            for mv in moves:
                #do move and update seen and neighbor_dict
                brd_2 = brd_1.make_move(mv)
                h_brd_2 = hash(brd_2)
                if h_brd_2 in s_seen: #over
                    neighbor_dict_b[h_brd_2] = (hash(brd_1),mv)
                    return BackTrack(neighbor_dict_b,neighbor_dict_s,hash(B),hash(brd_solved),h_brd_2)
                if not h_brd_2 in b_seen: #new neighbor
                    neighbors.add(brd_2)
                    b_seen.add(h_brd_2)
                    neighbor_dict_b[h_brd_2] = (hash(brd_1),mv)
        #now neighbors are new next
        b_next = neighbors
    return None
    
def BackTrack(nb,ns,b,s,m):
    """
    backtracks the path from b to something
    """
    #find the path to m from b
    output = []
    curr = m
    while curr != b:
        #find move to next curr
        curr,mv = nb[curr]
        output.append(mv)
    output.reverse()
    curr = m
    while curr != s:
        #find move to next curr
        curr,mv = ns[curr]
        output.append(mv)
    return output



