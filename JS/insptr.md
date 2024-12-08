###### this
| context   |  browser(this) | nodejs(this) | nodemjs(this) |
|-----------|----------------|--------------|---------------|
| function  | global/window  |global        |               |
| ctor method | ctor function/object | ctor function/object| ctor function/object |
| object method   | object         | object       | object        |
| arrow function  | window |{}        |    undefined           |
| arrow ctor method | ctor function/object | ctor function/object| ctor function/object |
| arrow object method   | window       | {}       | undefined        |

###### call context : Global
| context   |  browser(this) | nodejs(this) | nodemjs(this) |
|-----------|----------------|--------------|---------------|
| function  | global/window  |global        |               |
| ctor method | global/window | global| global |
| object method   | global/window        | global       | object        |

| arrow function  | window |{}        |    undefined           |
| arrow ctor method | ctor function/object | ctor function/object| ctor function/object |
| arrow object method   | window       | {}       | undefined        |

###### call context : Another class/obj literal(callObjLiteral)
| context   |  browser(this) | nodejs(this) | nodemjs(this) |
|-----------|----------------|--------------|---------------|
| function  | callObjLiteral  |callObjLiteral        |               |
| ctor method | callObjLiteral | callObjLiteral| callObjLiteral |
| object method   | callObjLiteral        | global       | object        |

| arrow function  | window |{}        |    undefined           |
| arrow ctor method | callObjLiteral | callObjLiteral| callObjLiteral |
| arrow object method   | window       | {}       | undefined        |

Note: Arrow function doesn't have their own context, only in case of ctor function, gets ctor function as context!
    - Arrow function context in node is {}/undefined irrepective of calling context(another obj, global context)
    - Arrow function context in browser is window irrepective of calling context(another obj, global context)

 Functions gets ctor context in case of ctor call context! 