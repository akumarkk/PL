class obj:
    major = 'CSE'
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    def rate(self, r):
        self.rating=r
        

o1 = obj('dev', 5)
o1.rate(5)
print(o1.rating)
print(obj.major)