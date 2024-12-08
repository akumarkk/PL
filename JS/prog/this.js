let cap = {
    firName: "Tarak",
    sayHi: function() {
        console.log(this); 
        console.log(`hi from ${this.firName}`);
    }
};
cap.sayHi(); // 'Tarak'
var firName = "Tarak Devara";
let sayHi = cap.sayHi;
sayHi(); // 'Tarak Devara'


let cap1 = {
    firName: "Tarak",
    sayHi: () => {
        console.log(this); 
        console.log(`hi from ${this.firName}`);
    }
};

cap1.sayHi(); // 'Tarak Devara'

