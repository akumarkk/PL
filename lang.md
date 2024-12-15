###### procedurral vs functional
- [ ] functional programming
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

    
- [ ] procedural programming
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