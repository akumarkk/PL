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

###### Abstraction
    - abstract method no implementation, share the contract for an conc. classes
    -  @abstractmethod
            drive():
                pass
    - abs class can have atleast one abs. method
    - use abc module(ABC, @abstractmethod)
    - no interfaces, abstract class used as interface with all the methods abstract 



###### Encapsulation
 - bundling data and methods within the single unit
 - protecting the properties and functionalities of an obj from another obj.
 - name mangling: __field privarte # hdidden by interpreter, accessible by self.

 - s.__Class__field name mangling
 -   




###### Polymorphism
i. static - no
ii. runtime
    a. base class - no
    b. method overriding - yes
- duck typing -
    ```
    def callTalk(obj):
        obj.talk()

    callTalk(Duck)
    callTalk(manobj)

    ```
- dep injection - engine interface(airbus, boeing) onto flight
    ```
    class Flight:
        def __init__(self, engine):
            self.engine = engine
    
    class AirbusEngine():
        def start(self):
            pass
    class BoeingEngine():
        def start(self):
            pass
    
    ae = AirbusEngine()
    f = Flihgt(ae)


    ```
- method overriding - 
- operator overloading - string, list
- 



###### Inheritence
- inheriting from an existing obj/class.
- re-usability and 'is-a' relation
- car is a vehicle, car contains engine(DI/'has-a')
- derived class ctor : invoke super()/base(base_class_name) class ctor
- no compile/rt-time check for super() ctor call
- super() function
    ```
    class BMW:
        def __init__(self, make):
            pass
    
    class ThreeSeries(BMW):
        def __init__(self, make, coup):
            super().__init__(make)
            or
            BMW.__init__(make)

    ```
- 


###### garbage collection
- runs in bg, dealloc's obj which aren't referenced anymore.
- import gc; gcisenabled(), gc.enable(), gc.disable()



