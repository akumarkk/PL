
s= performance.now();
console.time();

let m = new Map();
m.set("key", "val");
m.set({a: "val"}, "obj val")
t= console.timeEnd();
e = performance.now()

console.log(m, `"completed in ${e-s} microsecs"`);


function sum(num) {
    let ret = 0;
    for (var i = 0; i < num; i++) {
        ret += i;
    }
    return ret;
}

const memoize = (fn) => {
let cache = {};

    return function(n) {
        if (cache[n] !== undefined) {
            return cache[n];
        }

        cache[n] = fn(n);
        return cache[n];
        
    }
}

let sumFn =  memoize(sum);
s = performance.now();
sumFn(10000);
e = performance.now();
console.log(m, `"sumFn completed in ${e-s} microsecs"`);

s = performance.now();
sumFn(10000);
e = performance.now();
console.log(m, `"sumFn completed in ${e-s} microsecs"`);
