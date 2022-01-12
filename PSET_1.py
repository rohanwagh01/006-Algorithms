##################################################
# Problem 1. BackFront
##################################################

# Create a datastructure to support O(1) random access,
# and O(1) amortized inserts/deletes to the front and back end of the record

class BackFront():
    def __init__(self):
        self.prepend_count = 0
        self.append_count = 0
        self.prepend_buffer = 0
        self.append_buffer = 0
        self.prepends = []
        self.appends = []
    
    def get_index(self,key):
        if self.prepend_count > key:
            return -key-1
        else:
            return key-self.prepend_count+self.append_buffer

    def __setitem__(self, key, value):
        '''
        Stores value at the index of key
        '''
        new_key = self.get_index(key)
        if new_key < 0:
            self.prepends[new_key] = value
        else:
            self.appends[new_key] = value

    def __getitem__(self, key):
        '''
        Returns value at the index of key
        '''
        new_key = self.get_index(key)
        if new_key < 0:
            return self.prepends[new_key]
        else:
            return self.appends[new_key]

    def as_list(self):
        '''
        Should return all the elements in the record in order
        '''
        if self.prepend_buffer == 0:
            return self.prepends[::-1] + self.appends[self.append_buffer:]
        else:
            return self.prepends[:self.prepend_buffer-1:-1] + self.appends[self.append_buffer:]

    def append(self, value):
        '''
        Should add on value to the record at the end
        '''
        self.appends.append(value)
        self.append_count += 1


    def delete_last(self):
        '''
        Should remove the last element in the record
        '''
        #if there are things in append then pop, otherwise add one to prepend buffer
        if self.append_count > 0:
            self.appends.pop()
            self.append_count -= 1
        elif self.prepend_count > 0: #do nothing if both counts are zero
            self.prepend_buffer += 1 
            self.prepend_count -= 1
        


    def prepend(self, value):
        '''
        Should add on value to the beginning of the record
        '''
        self.prepends.append(value)
        self.prepend_count += 1

    def delete_first(self):
        '''
        Should remove the first element in the record
        '''
        #if there are things in prepends then pop, otherwise add one to append buffer
        if self.prepend_count > 0:
            self.prepends.pop()
            self.prepend_count -= 1
        elif self.append_count > 0: #do nothing if both counts are zero
            self.append_buffer += 1 
            self.append_count -= 1