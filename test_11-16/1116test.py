class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name}\n Age:{self.age}"    

    def myfunc(self):
        print("Hallo my name is :"+self.name)


p1 = person("Elsa",269)
p1.myfunc

print(p1.name)
print(p1.age)

print(p1)
