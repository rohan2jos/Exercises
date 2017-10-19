import logging
logging.basicConfig(filename="logs/priority_queue.log", level=logging.DEBUG, format='%(asctime)s %(funcName)5s() %(levelname)s: %(lineno)d  %(message)s', datefmt='%I:%M:%S %p')


'''
=============================================================================

insertWithPriority()

Insert new item into the priority queue.
We have to specify the data and the priority associated with that given data

----------------------------------------------------------------------------

getHighestPriorityElement()

Returns the element with the highest priority
    - Reconstruct the heap after returning the element

    1. Max Heap: Returns the maximum element
    2. Min Heap: Returns the minimum element

-----------------------------------------------------------------------------

peek()

Returns the element with the highest priority without changing the structure
of the heap

=============================================================================

'''


class Priority_Queue():
    def __init__(self):
        logging.debug("creating an object of the PriorityQueue")