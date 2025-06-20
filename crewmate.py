'''
    Python file to implement the class CrewMate
'''
import treasure
import heap

#comparison function which compares the treasure according to the priority 
def comp2(treasure1, treasure2):
    
    if treasure1.size+treasure1.arrival_time<treasure2.size+treasure2.arrival_time:
        return True
    elif treasure1.size+treasure1.arrival_time>treasure2.size+treasure2.arrival_time:
        return False
    else:
        if treasure1.id<treasure2.id:
            return True
        else:
            return False

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
       
        self.load = 0 # sum of remaining sizes of treasures
        self.heap2 = heap.Heap(comp2, []) #heap of treasures
        self.last_arrival_time=0 # time when last treasure arrived
        

    def add_treasure_to_crew(self, treasure):
        self.heap2.insert(treasure) #insert the treasure
        self.load += treasure.size #update load

    