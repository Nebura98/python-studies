from vehicle import Vehicle


# In the parenthesis you can add the inherent
class Car(Vehicle):
    def brag(self):
        print('Look how cool my car is!')


car = Car()
car.drive()
# car.__warnings.append('New warning')
# __dict__ convert our class attributes into a dictionary
# print(car.__dict__)
print(car.add_warning('New warning'))
print(car.get_warnings())

car2 = Car(200)
car2.drive()
