class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        
        self.comp = comparison_function
        if init_array:
            self.heap = init_array
            self.build_heap()  # Build the heap from the initial array
        else:
            self.heap = []
    
    def __len(self):
        return len(self.heap)
    
    def _parent(self, index):#returns the index of the parent node 
        
        if index == 0:
            return None  # root node has no parent
        return (index - 1) // 2

    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        self.heap.append(value)        
        self._up_heap(self.__len() - 1)  # move the last inserted element to its correct position

    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        if self.__len() == 0:
            return None
        if self.__len() == 1:
            return self.heap.pop()  # if there's only one element, remove and return it
        
        root = self.top()
        self.heap[0] = self.heap.pop()  # replace root with the last element
        self._down_heap(0)  # restore heap property by down-heap from the root
        return root

    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        if self.heap:
            return self.heap[0]
        return None

    def build_heap(self):
        
        # builds the heap from the initial array  O(n)
       
        n = self.__len()
        # start from the last non-leaf node and apply down heap
        i = n // 2  # start from the middle of the array
        while i >= 0:
            self._down_heap(i)  # call down heap on each index
            i -= 1  # move to the previous index

    def _down_heap(self, curr):
      
        # moves the element at index i down the heap to restore heap property  O(log(n))       
    
        n = self.__len()
        while True:
            high = curr# Initialize high as the current node
            left_child = 2 * curr + 1
            right_child = 2 * curr + 2
            
            # check if right child exists and is higher in priority than the current node
            if right_child < n and self.comp(self.heap[right_child], self.heap[high]):
                high = right_child

            # check if left child exists and is higher in priority than least node found 
            if left_child < n and self.comp(self.heap[left_child], self.heap[high]):
                high = left_child            
            
            if high == curr:
                break  # if no swap happens, the heap is restored
            else:  
                # Swap curr with the highest priority child          
                temp=self.heap[curr]
                self.heap[curr]=self.heap[high]
                self.heap[high]=temp
                curr = high  # move down to the child we swapped with
           

    def _up_heap(self, index):

        # moves the element at index up the heap to restore heap property O(log(n))  
        
        parent = self._parent(index)
        # continue moving up while parent exists and comparison is True
        while parent is not None and self.comp(self.heap[index], self.heap[parent]):
            temp=self.heap[index]
            self.heap[index]= self.heap[parent] 
            self.heap[parent]=temp 
            index = parent  # move up to the parent
            parent = self._parent(index)
