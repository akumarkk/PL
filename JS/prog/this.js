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