###### this
| context   |  browser(this) | nodejs(this) | nodemjs(this) |
|-----------|----------------|--------------|---------------|
| function  | global/window  |global        |               |
| ctor method | ctor function/object | ctor function/object| ctor function/object |
| object method   | object         | object       | object        |
| arrow function  | window |{}        |    undefined           |
| arrow ctor method | ctor function/object | ctor function/object| ctor function/object |
| arrow object method   | window       | {}       | undefined        |