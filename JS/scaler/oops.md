###### Scope

1. global scope - anywhere in the code.
2. Function scope
3. Block scope
    let, const


###### Hoisting
var-declared variables are hoisted to the top of their containing scope.
JavaScript had only two types of scopes: global and function. Variables declared with the var keyword are hoisted to the top of their function scope.

var does not have block-level scope. It is function-scoped, meaning it's accessible within the entire function, regardless of block boundaries like if statements, for loops, or while loops.
```
funciton t1()
{
    console.log(h) // undefined
    var h = "hello from agent";
    console.log(h) // "hello from agent"

    {
        console.log(d);
        var d ='hello from d';
    }
    console.log(d);
}

t1();
console.log(h) // Reference error as hoisted within the function scope 
