function test() {
    this.a = "hello from a!";

    this.print1 = function () { 
        console.log("print1 ", this.a); 
    }
    // return {
    //     print: () => {
    //         console.log(this.a);
    //     },
    //     a: this.a
    // }

}
let t1 = new test();
// t1.print();
t1.print1();
console.log(t1.a);