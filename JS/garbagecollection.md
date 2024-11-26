###### Garbage collection
Mark and sweep
1. Marking - 
    collector traverses through the graph of objects linked to globals, marks each one it finds

2. Sweep -
    collector traverses all the objects in the heap and deletes that are unmarked and unreachable from root/globals
    - also unmarks objects for subsequent reference

- identifies what's live and everything else become's garbage.

Reference Count
 - if reference count of an object is zero, considered garbage/dead object

Mutator and collector thread

Mutator - creating, reading and writing objects.
collector - garbage collecting thread

Explicit GC
- triggered by new()
obj  = alloc()
if obj ==  null:
    collector()
    obj = alloc()
    if obj == null:
        raise "OOM"
    return obj

Root node
    thread stack, globals

Explicit 
