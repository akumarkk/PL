function Swimmable(Base) {
return class extends Base {
    swim() {
        console.log("swim...")
    }
}
}


function Flyable(Base) {
    return class extends Base {
        fly() {
            console.log("fly...")
        }
    }

}

class Animal{}

const duck = Flyable(Swimmable(Animal))
// or

class Duck extends Flyable(Swimmable(Animal)) {}
console.log(duck)
d = new duck()
d.fly()
d.swim()


d1 = new Duck()
d1.fly();
d1.swim();