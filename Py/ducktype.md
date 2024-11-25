###### Ducktyping
if it walks like a duck, if it quacks like a duck, it's a duck!

programming technique, where Based on methods and properties present on the object, object is useed in the place of type/class.

With duck typing, an object is considered to be certain type if it has all the properties and type required by the type.
```
class Ratelimit {
    name:str

    def limit():
        pass
}

class ClusterRatelimit {
    name:str

    def limit():
        pass

}

def test(r: Ratelimit):
    r.apply()

we can either pass Ratelimit/ClusterRatelimit to test based on duck test


```
 