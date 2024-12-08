###### Scope

1. global scope - anywhere in the code.
2. Function scope
3. Block scope
    let, const

    let, const - have block, function and global scope!(after ES6)
        no hoisting // ReferenceError: Cannot access 'e' before initialization
        no redeclaration within the same scope!
        recommended over var
        caniuse.com



###### Hoisting
var-declared variables and functions are hoisted to the top of their containing scope.
JavaScript had only two types of scopes: global and function. Variables declared with the var keyword are hoisted to the top of their function scope.

var does not have block-level scope. It is function-scoped, meaning it's accessible within the entire function, regardless of block boundaries like if statements, for loops, or while loops.
var redeclaration is possible
```
function t1()
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
```
t1();
console.log(h) // Reference error as hoisted within the function scope 

###### Shadowing
 - delcaring the same variable in diff/same scopes
 - legal shadowing - redeclaring in the same scope
 - illegal shadowing  - redeclaring in the diff scope

###### this
this - points to the enclosing scope!
```
let cap = {
    firName: "Tarak",
    sayHi: () => { consoloe.log(`hi from ${this.firName}`);}
};
cap.sayHi(); // 'Tarak'
var firName = "Tarak Devara";
let sayHi = cap.sayHi;
sayHi(); // 'Tarak Devara'


```


```
// file1.js
var myVariable = "hello";
console.log(myVariable); // Output: hello

// file2.js
console.log(global.myVariable); // Output: undefined (if not defined globally)
```
NodeJs: if declared outside of a function, it becomes a global variable accessible within that module. However, it's not directly attached to the global object.



###### Object
- collection of peroperties, methods and represented by k-v pair.
object vs json
    - obj key - can be non-quoted string 
    - JSON.parse("{\"a\": 10}") // {a: 10}

###### native vs host objects
Native - objects provided by js PL
Host object - objects provided by the env.
    Node - globals, process
    borwser - window, document, localStorage, sessionStorage
    
###### 
