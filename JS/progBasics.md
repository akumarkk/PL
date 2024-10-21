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

###### Finite state machine
