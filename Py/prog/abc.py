import abc
class Bmw(abc.ABC):
    def __init__(self, make):
        self.make=make

    def start(self):
        print("engine started")

    def stop(self):
        print("engine stopped")

    @abc.abstractmethod
    def drive(self):
        pass

class ThreeSeries(Bmw):
    def __init__(self, make):
        super().__init__(make)

    # def drive(self):
    #     print("three series...")


c = ThreeSeries(2021)
    
    