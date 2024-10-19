###### cross-platform desktop apps Apps

https://www.electronjs.org/

###### JS Engine

- JS Engine executes the code with callstack

CS CALLSTACK

GEC (Global EC)

- creation phase  variables are declared and assigned undefined
- Execution phase

BEC (Block EC)


FEC (Function EC)


##### Interpreter
JavaScript Hoisting is the behavior where the interpreter moves function and variable declarations to the top of their respective scope before executing the code. This allows variables to be accessed before declaration, aiding in more flexible coding practices and avoiding “undefined” errors during execution.


```
function real() {
    console.log("test1")
}

function real() {
    console.log("test1")
}

real()
function real() {
    console.log("test1")
}

---->

function real() {
    console.log("test1")
}

function real() {
    console.log("test11")
}

function real() {
    console.log("test3")
}

real() // print test3

```

CDN
    - third-party lib
    - src in cdn