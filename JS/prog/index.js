console.log("hello from agent")

o = {
a : 10
}

o1 = {
a1: 11
}

function dispatch(state, ...payload) {
    console.log(payload)
}


dispatch('idle', 'hi', {a:10})

student = {
    name : 'Arush',
    age: 14
}
Object.defineProperty(student, 'marks', {
    value: 98,
    configurable: false,
    writable: true,
    enumerable: true,
});

student.marks = 100 // ignore set
delete student.marks
for (i in student) {
 console.log(i, student[i])
}


console.log(student)




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