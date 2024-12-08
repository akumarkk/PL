function print() {
    console.log(this);
}

function person() {
    this.name = "Tarak i";
    this.greet = function () {
        console.log(this);
    };

    this.arrprint = () => {
        console.log("arrprint", this.name, this);
    }
}

const per = {
    name: "Tarak",
    greet() {

        console.log(this.name, this);
    },
    arrprint :() => {
        console.log("obj arrprint", this);
    }
}

const arrprint = () => {
    console.log("arrprint", this);
};


const callobj = {

    callobjGreet(){
        console.log(`callobj`);
    },
    callfunc: null,
    name:"callobj"
}

callobj.callfunc = print;
console.log(`ctx callobj:print `);
callobj.callfunc()


let p= new person();
callobj.callfunc = p.greet;
console.log(`ctx callobj:p.greet `);
callobj.callfunc()

callobj.callfunc = p.arrprint;
console.log(`ctx callobj:p.arrprint `);
callobj.callfunc()

callobj.callfunc = per.greet;
console.log(`ctx callobj:per.greet(literal) `);
callobj.callfunc()

callobj.callfunc = per.arrprint;
console.log(`ctx callobj:per.arrprint(literal) `);
callobj.callfunc()

callobj.callfunc = arrprint;
console.log(`ctx callobj:arrprint `);
callobj.callfunc()


