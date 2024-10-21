


function fn() {
    console.log("hello from agent")
    throw Error("fn err")
}


try{
    fn();
} catch (e) {
    console.log(e)
    return -1
} finally {
    console.log("finally")

}