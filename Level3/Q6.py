class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

print("Single Inheritance Example:")
dog = Dog("Buddy")
dog.speak() 


class Engine:
    def start(self):
        print("Engine starts.")

class Wheels:
    def roll(self):
        print("Wheels roll.")

class Car(Engine, Wheels):
    def drive(self):
        print("Car is driving.")

print("\nMultiple Inheritance Example:")
car = Car()
car.start()
car.roll()
car.drive()


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying in grade {self.grade}.")

class Graduate(Student):
    def __init__(self, name, grade, degree):
        super().__init__(name, grade)
        self.degree = degree

    def graduate(self):
        print(f"{self.name} has graduated with a degree in {self.degree}.")

print("\nMultilevel Inheritance Example:")
graduate = Graduate("Poojan", "12th", "Computer Science")
graduate.introduce()
graduate.study()
graduate.graduate()
