class sports():
    def __init__(self,name):
        self.name = name
    
    @property
    def sports_name(self):
        return self.name
    @sports_name.setter
    def sports_name(self,value):
        self.name = value
    def practice(self):
        print("Doing sport practice")

class Landsports(sports):
    def __init__(self,name,field):
        super().__init__(name)
        self.field = field

    @property
    def Landsports_field(self):
        return self.field
    
    def practice(self):
        print("Doing Land Sport pratice")


class Watersports(sports):
    def __init__(self,name,activity):
        super().__init__(name)
        self.activity = activity

    @property
    def Watersports_activity(self):
        return self.activity

    def practice(self):
        print("Doing Water Sport pratice")

# Example of usage
if __name__ =="__main__":

    baseball = Landsports("baseball","baseball fild")
    print(baseball.sports_name)
    print(baseball.Landsports_field)
    print(baseball.practice())

    water_skiing = Watersports("water skiing","strap on your skis  and")
    print(water_skiing.sports_name)
    print(water_skiing.Watersports_activity)
    print(water_skiing.practice())