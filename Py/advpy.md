###### Adv py

dataclasses:
    similar to record in high-level prog languages.
    dataclasses provide a convenient way to define classes with automatically generated methods like __init__,__repr__ etc
    - The @dataclass decorator generates an __init__ method that looks like this:
    ```
    def __init__(self, name: str, age: int, city: str):
        pass
    ```

    - Post-Initialization: For additional initialization tasks, you can use the __post_init__ method, which is called after the __init__ method.


class var
when an instance modifies the class variable, it creates its own copy, which leads to a different behavior.
