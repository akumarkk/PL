function print() {
    console.log(this);
}

print();

function person() {
    this.name = "Tarak i";
    this.greet = function () {
        console.log(this);
    };

    this.arrprint = () => {
        console.log("arrprint", this.name, this);
    }
}

let p = new person();
p.greet();
p.arrprint();

const per = {
    name: "Tarak",
    greet() {

        console.log(this.name, this);
    },
    arrprint :() => {
        console.log("arrprint", this);
    }
}

// let p1 = new per();
per.greet();
per.arrprint();
// 
const arrprint = () => {
    console.log("arrprint", this);
};
arrprint();


