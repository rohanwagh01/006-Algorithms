'''
Student Template for Kresge Grass
'''

'''
You will probably want to put your implementation of a BST here.
Once again, we only have an array and there are no insertions or
deletions. Hence, it might not be wise to simply copy the
recitation notes implementation.
'''

'''
Represents an array data structure which allows incrementing over
a range of indices. For example, if we started with an array:

A = [5, 1, 7, 2, 11]

Here are some example queries:
    get(0) --> 5
    get(1) --> 1
    get(2) --> 7
    get(3) --> 2
    get(4) --> 11

However, if we then called:
    increment(2, 4, 6) --> A = [5, 1, 13, 8, 17]
    increment(0, 3, 2) --> A = [7, 3, 15, 10, 17]

So the previous queries would now yield:
    get(0) --> 7
    get(1) --> 3
    get(2) --> 15
    get(3) --> 10
    get(4) --> 17
'''


class KresgeGrass(object):

    def __init__(self, A) -> None:
        '''Initializing the Data Structure from array/list A'''
        self.root = tree_builder(A, 0, len(A)-1)
    
    def get(self, i) -> int:
        '''Return the i-th element in your data structure'''
        def gtr(n,i):
            if n.get_ind() == i: #found it
                return n.get_val() + n.get_aug()
            elif i < n.get_ind(): #left child
                return gtr(n.get_left(),i) + n.get_aug()
            else:
                return gtr(n.get_right(),i) + n.get_aug()
        return gtr(self.root,i)
            
    def increment(self, a, b, k) -> None:
        '''Increment elements from indices a to b by k'''
        #first find LCA
        def LCA(n,a,b):
            if n.get_ind() < b and n.get_ind() < a:
                #recurse on right
                return LCA(n.get_right(),a,b)
            elif n.get_ind() > b and n.get_ind() > a:
                #recurse on right
                return LCA(n.get_left(),a,b)
            else: #must be split
                return n
        #go on left side 
        def look_a(n,a,h,bool=True):
            if n.get_ind() == a:
                adjust_aug(n.get_left(),-h)
                if not bool:
                    adjust_aug(n,h)
            elif n.get_ind() < a: #go to the right
                if bool:
                    adjust_aug(n,-h)
                look_a(n.get_right(), a, h, False)
            else:
                if not bool:
                    adjust_aug(n,h)
                look_a(n.get_left(), a, h, True)
        #go on the right side
        def look_b(n,b,h,bool=True):
            if n.get_ind() == b:
                adjust_aug(n.get_right(),-h)
                if not bool:
                    adjust_aug(n,h)
            elif n.get_ind() > b: #go to the left
                if bool:
                    adjust_aug(n,-h)
                look_b(n.get_left(), b, h, False)
            else:
                if not bool:
                    adjust_aug(n,h)
                look_b(n.get_right(), b, h, True)
        
        p = LCA(self.root,a,b)
        adjust_aug(p,k)
        if p.get_ind() == a:
            adjust_aug(p.get_left(),-k)
        if p.get_ind() == b:
            adjust_aug(p.get_right(),-k)
        if p.get_ind() != a:
            look_a(p.get_left(),a,k)
        if p.get_ind() != b:
            look_b(p.get_right(),b,k)



def tree_builder(l,i,j):
    if j < i:
        return None
    if j == i:
        return Node(i,None,None,l[i])
    #find middle 
    mid = int((i+j)/2)
    return Node(mid,tree_builder(l,i,mid-1),tree_builder(l,mid+1,j),l[mid])

def adjust_aug(n,d):
    if n != None:
        n.aug += d

class Node(object):

    def __init__(self,i,l,r,v):
        self.ind = i
        self.left = l
        self.right = r
        self.aug = 0
        self.val = v

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_val(self):
        return self.val
    
    def get_ind(self):
        return self.ind
    
    def get_aug(self):
        return self.aug