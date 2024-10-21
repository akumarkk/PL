console.log("hello from agent")

o = {
a : 10
}

o1 = {
a1: 11
}

obj = {o, o1
}
console.log(obj)
console.log(o1.a1)



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

state = reducer('dark', 'DARKEN')
state = reducer('dark', 'LIGHTEN')
state = reducer('dark', 'LIGHTEN')
console.log(state)

// abc

// line by line execution