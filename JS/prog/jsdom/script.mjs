function t1()
{
    console.log(h) // undefined
    var h = "hello from agent";
    console.log(h) // "hello from agent"

    {
        console.log(d);
        var d ='hello from d';
    }
    console.log(d);
}

t1();
console.log(h)