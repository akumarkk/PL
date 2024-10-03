class BMW:
    def __init__(self, make):
        print("BMW")
        pass
    
    def start(self):
        print("starting...")
    
class ThreeSeries(BMW):
    def __init__(self, make, coup):
        #super().__init__(make)
        #BMW.__init__(make)
        print("ThreeSeries")

    def start(self):
        print("starting threeseries...")


t1 = ThreeSeries(2000, True)
t1.start()
