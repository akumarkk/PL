##### dataclasses
- class vars are initailized in the order of declaration
```
>>> from dataclasses import dataclass
>>> @dataclass
... class test:
...   name:str
...   age:int

t = test(10, 'Tarak')
>>> t
test(name=10, age='Tarak')

```