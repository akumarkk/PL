obj = {
    name : "tarak",
    age: 40
};

const handler = {
    get(object, prop) {
        console.log(`getting prop ${prop}`)
        return object[prop];
    },

    set(object, prop, val) {
        if(prop == 'age') {
            if(val ==0 || val < 0) {
                
                // console.log("age can't be negative")
                throw new Error("age can't be negative")
            }
        }
        console.log(`setting prop ${prop} ${val}`)
        object[prop] = val;
    }
}

const proxy = new Proxy(obj, handler)
proxy.name = 'Tarak'
try{
    proxy.age = 0;
    // new Error("age can't be negative")
}catch (e) {
    console.error(e)

}
// proxy.age = 0;
proxy.age = 1000;