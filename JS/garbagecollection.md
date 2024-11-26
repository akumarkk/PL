###### Garbage collection
Mark and sweep
1. Marking - 
    collector traverses through the graph of objects linked to globals, marks each one it finds

2. Sweep -
    collector traverses all the objects in the heap and deletes that are unmarked and unreachable from root/globals
