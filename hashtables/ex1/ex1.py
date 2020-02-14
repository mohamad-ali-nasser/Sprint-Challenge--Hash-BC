#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    # """
    # i = 0
    # while weights:
        
    #     # for i in range(len(weights)):
    #         hash_table_insert(ht, i, weights[i])
    #         # number = weights[i]
    #         if i+1 < len(weights):
    #             # hash_table_insert(ht, i+1, weights[i+1])
    #             first = hash_table_retrieve(ht, i)
    #             second = weights[len(weights)-1]
    #             # second = hash_table_retrieve(ht, i+1)
                
    #             if first + second == limit:
    #                 if first > second:
    #                     return (i, i+1)
    #                 return(i+1, i)
    #             if len(weights)-1 is not None:
    #                 print(ht.storage)
    #                 hash_table_remove(ht,len(weights)-1)
                
    #             i+=1
                
            
            
    #     if hash_table_retrieve(ht, i) + hash_table_retrieve(ht, i+1)
        

    for i in range(len(weights)):
        for j in range(i+1, len(weights)):
                if weights[i]+weights[j] == limit:
                    if weights[i] > weights[j]:
                        return (i, j)
                    return(j, i)

        
    print(len(ht.storage))

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], length = 5, limit = 21)