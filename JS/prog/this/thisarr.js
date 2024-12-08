const g = this;
const gl = global;
const f = () => {
    let that = this;
    console.log("f - ", this, that, g, gl)
}
f()