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

class Employee extends User {
    constructor(name, age, email, dep) {
        super(name, age, email);
        this.dep = dep;
    }

}

try {
    u = new Employee("tarak", 10, "test@gmail.com", "commerce")
    console.log(u)

} catch(e) {
    console.error("err: ")
    console.log(e)

}
