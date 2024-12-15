###### procedurral vs functional

- [ ] Functional programming
We can assign a function to a variable, pass it as an argument or return it from a function just like a regular variable. That means a function can be defined and invoked in any context just as much as a variable can.

Characteristics of Functional Programming:

First-class Functions, Higher-order Functions, Pure Functions, Referential Transparency, Immutable State, Control Flow

Core Concepts
- Ad Hoc Polymorphism: A mechanism that allows a compiler/interpreter to distinguish which implementation of a function is invoked based on the types of arguments a function is called. This is otherwise known as overloading, where functions may have multiple implementations for different parameter types or signatures.
- Subtyping: A method of defining a subset-superset relationship among types. For instance, a Cat and a Dog are subtypes of an Animal.
- First-class functions: These functions are treated like any other variable. For example, in such a language, a function can be passed as an argument to other functions, can be returned by another function, and can be assigned as a value to a variable. Example:
// foo is a variable that has been assigned a function
const foo = () => {
  console.log("foobar");
}
foo(); // Invoke it using the variable
// foobar

- Higher-order functions: These functions take functions as arguments or functions that return functions. This is possible because functions and data are the same.
- Recursion: It is a functional equivalent of iterative loops where a function calls itself until the base case is met. Most languages that advocate for functional programming optimize the performance overhead of recursion via Tail-Call Optimization or Compiler Optimization, which translates a recursive function into iterative loops.
- Pure Function: A function that returns a value and does not alter the state of a non-local attribute.
- Referential transparency: A mechanism that does not permit one to change the value of a variable once defined. This mechanism guarantees functional programs to be referentially transparent i.e., if a == b, then f(a) == f(b). This property of purely functional languages makes programs easier to reason and optimize.

```
def sum_even_numbers_functional(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total
    # return sum(number for number in numbers if number % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers_functional(numbers)
print(result)  # Output: 30

```
    - Immutable State: 
    - no side effects
    - referential transparency
    - Control Flow

    
- [ ] Procedural programming
```
def sum_even_numbers_procedural(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers_procedural(numbers)
print(result)  # Output: 30
```
    - mutable state
    - side effects: The procedural approach has a side effect of modifying the total variable. The functional approach avoids side effects by using pure functions.
    - not referential transparency
    - Control Flow : The procedural approach uses an explicit for loop to control the iteration. The functional approach relies on higher-order functions like filter and sum to achieve the same result.