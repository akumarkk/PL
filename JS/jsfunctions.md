###### Functions
Function - base object for functions.
```
function add(a, b) {
    return a + b;
}

Function.prototype.hello = function(a, b) {
    return "a + b";
}

add.hello();
```

###### Constructors functions
When using constructor functions (invoked with the new keyword), this refers to the newly created object. Constructor functions allow you to set up shared properties and methods across multiple instances. However, if you accidentally call a constructor function without the new keyword, this will not refer to the new object and could cause unexpected behavior.
Your task is to fix the Person constructor so that it works correctly with or without the new keyword. If the new keyword is not used, the constructor should automatically call itself with new to avoid incorrect behavior.
```
function Person(name, age) {
    this.name = name;
    this.age = age;
}

var p1 = Person("John", 30); // error

function Person(name, age) {
    this.name = name;
    this.age = age;

    if((typeof window !== 'undefined' && this == window) || this == undefined || (global && this ==global)) {
      return new Person(name, age);
    }

    // or 

    return {name, age};
}
```

- When a function is called without the new keyword, this is set to the global object in non-strict mode and undefined in strict mode. You can use a condition to check if this is an instance of Person to decide whether to re-invoke the constructor with new.

- Consider using a conditional statement inside the constructor to check whether this is an instance of the constructor function (Person). If not, use return new Person(name, age); to force the correct behavior.