###### GC Garbage Collection Algorithms in Python

Python primarily employs a reference counting garbage collection algorithm, supplemented by a generational garbage collector for more complex scenarios.

Reference Counting
How it works:
Each object in Python has a reference count.
Whenever a new reference is assigned to an object, its reference count increases.
When a reference is removed, the reference count decreases.
If an object's reference count reaches zero, it is considered garbage and is immediately reclaimed.
Generational Garbage Collector
Why it's needed:
Reference counting is efficient for simple cases but can be inefficient for cyclic references.
The generational garbage collector addresses this limitation.
How it works:
Objects are divided into generations based on their age.
Newer objects are placed in younger generations.
Older objects are moved to older generations.
The garbage collector performs less frequent and less thorough garbage collection on older generations.
This optimization reduces the overhead of garbage collection, especially for long-running applications.