const Person = function(nm) {
    this.name = nm;
    this.speak1 = function(words) {
        console.log(this.name, words)
    }
}


// instead use prototype for speak()

Person.prototype.speak = function(words) {
    console.log(words)
}


pu = new Person("punith")
pu.speak("'hello, i'm punith")
pu.speak1("'hello, i'm punith")

su = new Person("suvith")
su.speak("'hello, i'm suvith")
su.speak1("'hello, i'm suvith")

console.log(pu.speak1 == su.speak1, pu.speak1=== su.speak1)

