class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

my_dog = Dog('buddy', 13)

print( my_dog.get_age() )

class Diablo :
    def __init__(self,name,job,skill):
        self.name = name
        self.job = job
        self.skill = skill


    def hunt(self):
        print (' {}은 {}이기 때문에 {}로 디아블로를 사냥합니다.' .format(self.name, self.job , self.skill) )

a = Diablo ('티리얼', '바라리안', '휠윈드')

print(a)

a.hunt()