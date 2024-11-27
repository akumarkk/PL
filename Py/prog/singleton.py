class EleSingleton:
    _instance = None
    count = 0
    

    def __init__(self, val):
        print(f"v {EleSingleton.count} {val} ")
        
        if EleSingleton.count == 0:
            print("init")
            self.val = val
        EleSingleton.count = 1 + EleSingleton.count

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        if cls._instance is None:
            print(cls._instance)
            cls._instance = super().__new__(cls)
        print(cls._instance)
        return cls._instance



e1 = EleSingleton(10)
e2 = EleSingleton(11)
e23 = EleSingleton(117)
print(e1.count, e2.count, e23.count)
print(e1.val, e2.val, e23.val)