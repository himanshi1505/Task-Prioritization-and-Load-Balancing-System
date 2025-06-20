'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure



#comparison function to compare the crewmates according to the priority 
def comp1(crewmate1,crewmate2):    
    if crewmate1.load+crewmate1.last_arrival_time<crewmate2.load+crewmate2.last_arrival_time:
        return True
    else:
        return False

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        
        self.m=m #number of crewmates
        self.all_treasures = []  # Track all treasures added
        

    def add_treasure(self, treasure):
                
        self.all_treasures.append(treasure) #add treasure to the all_treasures list
            

    
    def get_completion_time(self):
        n=len(self.all_treasures) #number of treasures
        l=min(n,self.m)
        crewmates = [crewmate.CrewMate() for _ in range(l)] 
        heap1 = heap.Heap(comp1, crewmates)
        completion_order = []        
        
        
            
        for t_original in self.all_treasures: 
            t = treasure.Treasure(t_original.id, t_original.size, t_original.arrival_time)  #creating a dummy treasure
            time_now = t.arrival_time
            
            crewmate1 = heap1.extract() # crewmate to which the treasure should be added
            time1 = crewmate1.last_arrival_time 
               
            # process crewmate1 from the time when last treasure was added till the current times   
            while time1 < time_now and crewmate1.heap2.top() is not None:

                current_treasure = crewmate1.heap2.extract() #treasure to be processed first according to the priority
                    
                x = min(current_treasure.size, time_now - time1)  # Process up to time_now or till the size becomes 0
                current_treasure.process(x)
                crewmate1.load -= x

                time1+=x # update time accordingly

                if current_treasure.size != 0: #if size is not 0 insert back into the crewmates heap2
                    crewmate1.heap2.insert(current_treasure)
                    
                        
                else: # if size becomes 0 update it's completion time and append to completion order
                    current_treasure.completion_time = time1
                    completion_order.append(current_treasure)      

            
            #update the last arrial time   
            crewmate1.last_arrival_time=time_now
           
            # Add the new treasure to the crewmate  
            crewmate1.add_treasure_to_crew(t)
            #insert the crewmate into heap
            heap1.insert(crewmate1)
        
        # Process any remaining treasures after the last arrival
        for crew in heap1.heap:          
            
            time1 = crew.last_arrival_time
            
            while crew.heap2.top() is not None:
                current_treasure = crew.heap2.extract()  # get the treasure with the highest priority
                x = current_treasure.size  
                current_treasure.process(x) # process the entire size of the current treasure
                time1 += x  # update the time              
                current_treasure.completion_time = time1  # update the completion time 
                completion_order.append(current_treasure) #append to completion order
        

        # Return treasures sorted by their completion time (earliest first)
        completion_order.sort(key=lambda t: t.id)
        return completion_order
