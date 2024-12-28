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