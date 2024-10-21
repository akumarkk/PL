###### value vs reference type assignment

- Primitive type - are value types
    bool
    string
    number
    null
    undefined
- Non-primitive type - reference type assignment
    array
    map

- generally refers to 
    - assignment to var
    - assignment from fun  params

###### Object
 - properties
 - methods
 
 Computed properties
    let bag = { [fruit]: 5}
        // property name - fruit
 Property value shorthand
    let o {name, age, marks}

 Inherited Properties
    hasOwnProperty //To check if a property is an object’s own property
    
 Property Attributes

    - value: The property’s value.
    - writable: When true, the property’s value can be changed
    - enumerable: When true, the property can be iterated over by “for-in” enumeration. Otherwise, the property is said to be non-enumerable.
    - configurable: If false, attempts to delete the property, change the property to be an access-or property, or change its attributes (other than [[Value]], or changing [[Writable]] to false) will fail.

    - non-strict mode no error on writing to non-writable property
    - Making a property non-configurable is a one-way road. We cannot change it back with defineProperty.
    - Object.getOwnPropertyDescriptors - obj get's own property descriptor
    - there are no limitations on property names
    -  integer properties are sorted, non-integer properties appear in create order
    - property keys must be string/symbols

 Property existence test, “in” operator

    user.noSuchProperty === undefined
    "key" in object
 
 
 Object create

    - {}

    - constructor/Factory functions
    
    ```
        function Stud(name, age, marks) {
                this.name = name,
                this.age = age,
                this.marks = marks
        }

        s = new Stud('arush', 10, 100)
    ```

    - Object.create()

    ```
        stud = {name: 'arush', age: 10, marks: 100}
        Object.create(stud)

    ```

    - es6 classes
    
    ```
            class Vehicle {
                constructor(name, maker, engine) {
                this.name = name;
                this.maker =  maker;
                this.engine = engine;
                }
            }

            v = new Vehicle('BMW', 'BMW', 'Bmw')
    ```


###### reducers

```
reducer = (state, action) => {
    if(action == 'DARKEN') {
        // additional action
        return state += 'er'
    }

    if(action == 'LIGHTEN') {
        // additional action
        return state.replace('er', '')
    }

}
```

- function that take's state, action/condition; based on condition, returns new stateof the obj

###### Enumerable
object is enumerable
    ```
    for key in obj:
        log(key)
    ``` 

    defineProperty(obj, property, {enumerable: false}) // not enumerable

###### Finite state machine

initial state
terminal state

each state consists of set of valid states, in which transitions are possible.

```
const 

const states = {
  idle: {
    on: {
      CLICK: 'loading'
    }
  },
  loading: {
    on: {
      SUCCESS: 'success',
      ERROR: 'error'
    }
  },
    : {
    on: {
      RESET: 'idle'
    }
  },
  error: {
    on: {
      RETRY: 'loading',
      RESET: 'idle'
    }
  }
};


// Initial state
let currentState = 'idle';

// Function to transition between states
function transition(action) {
  const nextState = states[currentState]?.on[action];
  if (nextState) {
    currentState = nextState;
    console.log('Transitioned to state:', currentState);
  } else {
    console.log('Invalid action for current state');
  }
}

// Example transitions
transition('CLICK'); // Transition to loading state
transition('SUCCESS'); // Transition to success state
transition('RESET');
```
- dispatch basically executes the action
 - transition - transition to the given state
 https://gist.github.com/prof3ssorSt3v3/9eb833677b8aa05282d72f0b3c120f03




###### Factory functions and prototype

- prototype objects are used when we've common functions/properties across the instances of the obj.
```
const Person = function(nm) {
    this.name = nm;
    this.speak = function(words) {
        console.log(words)
    }
}


instead use prototype for speak()
Person.prototype.speak = function(words) {
        console.log(words)
}

```

- variables without this operator becomes function scoped and not available on instance.
