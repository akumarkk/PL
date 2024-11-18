
s= performance.now();
console.time();

let m = new Map();
m.set("key", "val");
m.set({a: "val"}, "obj val")
t= console.timeEnd();
e = performance.now()

console.log(m, `"completed in ${e-s} microsecs"`);