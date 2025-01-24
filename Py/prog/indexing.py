class Car:
    def __init__(self, **kwargs):
        self.data = kwargs

    # method is called when you use the [] operator to access attributes.
    def __getitem__(self, keys):
        if isinstance(keys, list):
            return {key: self.data[key] for key in keys if key in self.data}
        elif isinstance(keys, str):
            return self.data.get(keys, None) 
        else:
            raise KeyError(f"Invalid key: {keys}")

# Example Usage:
my_car = Car(color='red', model='Tesla', year=2023, speed=120)

# Select multiple attributes
selected_attributes = my_car[['color', 'model']] 
print(selected_attributes)  # Output: {'color': 'red', 'model': 'Tesla'}

# Select a single attribute
car_color = my_car['color']
print(car_color)  # Output: 'red'