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
When using constructor functions (invoked with the new keyword), this refers to the newly created object. Constructor functions allow you to set up shared properties and methods across multiple instances. However, if you accidentally call a constructor function without the new keyword, this will not refer to the new object.

Your task is to fix the Person constructor so that it works correctly with or without the new keyword. If the new keyword is not used, the constructor should automatically call itself with new to avoid incorrect behavior.
```
function Person(name) {
    this.name = name;

    return {name}
}



```