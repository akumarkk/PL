import abc
class Bmw(abc.ABC):
    def __init__(self, make):
        self.make=make

    @abc.abstractmethod
    def start(self):
        # print("engine started")
        pass

    @abc.abstractmethod
    def stop(self):
        # print("engine stopped")
        pass

    @abc.abstractmethod
    def drive(self):
        pass

class ThreeSeries(Bmw):
    def __init__(self, make):
        super().__init__(make)

    # def drive(self):
    #     print("three series...")


c = ThreeSeries(2021)
    
    