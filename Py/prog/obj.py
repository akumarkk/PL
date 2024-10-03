import gc

class obj:
    major = 'CSE'
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    def rate(self, r):
        self.rating=r

    def __del__(self):
        print("destr")
        

print(gc.isenabled())
o1 = obj('dev', 5)
o1.rate(5)
print(o1.rating)
print(obj.major)
o1 = None

o1 = obj('dev', 5)
o1.rate(5)
print(o1.rating)


