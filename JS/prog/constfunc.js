function test() {
    this.a = "hello from a!";

    return {
        print: () => {
            console.log(this.a);
        },
        a: this.a
    }

}
let t1 = new test();
t1.print();
console.log(t1);