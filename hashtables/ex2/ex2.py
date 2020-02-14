#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)



class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)

    """
    YOUR CODE HERE
    """
    n = 0
    for i in tickets:
        # print(i.source)
        # if i.source == "NONE":
        #     n=0
        #     hash_table_insert(hashtable,"",i.destination)
        #     route.insert(0,i.destination)
        #     n+=1
        # elif i.destination == "NONE":
        #     hash_table_insert(hashtable,i.source,"")
        #     route.insert(length-1,i.source)
            
        # else: # i.source == route[0]:
        #     # route.insert(n,i.destination)
        
        hash_table_insert(hashtable,i.source,i.destination)
            
    # for i in range(length):

        
    initial = "NONE"

    for i in range(length-1):
        print(initial)
        route[i] = hash_table_retrieve(hashtable, initial)
        initial = route[i]

    return route
            
        
        
        
            # n+=1
            # print("i2: "+i.destination)
        # for j in tickets[1:]:
        #     if i.destination == j.source:
        #         print("j1: "+j.source)
        #         hash_table_insert(hashtable,n,j.source)
        #         n+=1
                
        # elif i[1] == None
        #     hash_table_insert(hashtable,length-1,i[0])
        
        # tkt = Ticket()
    # for i in hash_table_retrieve(hashtable, ):
    #     route.append(i)
    # print(hashtable.storage)

    return route
