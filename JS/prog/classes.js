class User {
    constructor(name, age, email) {
        this.name = name;
        this.age =age;
        this.email = email;
    }

    get name() {
        return this._name;
        
    }

    set name(value) {
        if(value.length <=4) {
            console.error(`name ${value} can't be less than 4chars`);
            throw new Error("value error")
        }

        this._name = value;
    
    }

}

try {
    u = new User("tk", 10, "test@gmail.com")

} catch(e) {
    console.error("err: ")
    console.log(e)

}
