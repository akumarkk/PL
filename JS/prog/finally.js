



function fn() {
    console.log("hello from agent")
    throw Error("fn err")
}


try{
    fn();
} catch ( e) {
    console.log(e)
    // return -1
} finally {
    console.log("finally")

}

class NetworkError extends Error {
    constructor(response) {
        super(response.text)
        this.name = "NetworkError"
        this.message = "Network Error"
        this.response = "Network Error response"
    }

    toString() {
    
        return [this.name , this.message, this.response].join(",")
    }
}

response = {text: "can't parse json" }
try{
    throw new NetworkError(response)
} catch ( e) {

    console.log(e.name)
    console.log(e.message)
    console.log(e.response)
    console.log(e.toString())
    
    return -1
} finally {
    console.log("finally")

}