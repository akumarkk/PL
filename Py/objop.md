###### oop
- obj - properties, methods
- classes - blueprint of an obj

```
class Product:
    // static var
    major = "CSE"
    numObj=0

    @staticmethod
    def displayCount():
        print(Product.numObj)

    // ctor
    def __init__(self, name, description, price,ratings):
        self.name = name
        self.description= description
        self.price = price
        numObj+=1

    def avg(self):
        return self.ratings/len(ratings)
    
    # setter
    def setName(self, name):
        self.name=name

    # getter
    def getName(self):
        return self.name
    
    # setter
    def setName(self, name):
        self.name=name

    # getter
    def getName(self):
        return self.name
    
    def display(self):
        print(self.name, self.ratings)
        <!-- return self.name -->

    # destr
    def __del__(self):
        #db cleanup

class Car:
    def __init__(self, model):
        self.model = model
    
    class Engine:
        def __init__(self, num):
            self.num = num
        
        def start(self):
            pass

c = Car()
e = c.Engine()
e.start()


p1 = Product()
Product.major
```

- class name in u-camel case
- var set in any methods, setter/getter not lang 
- static/instance methods/vars
- nested class car/engine
- Abstraction



- Encapsulation



- Polymorphism



- Inheritence

###### garbage collection
- runs in bg, dealloc's obj which aren't referenced anymore.
- import gc; gcisenabled(), gc.enable(), gc.disable()



