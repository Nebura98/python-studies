from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        # This way is how to use the inherent values
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(250)
bus1.add_warning('Test')
bus1.add_group(['Manuel', 'Maria', 'Jose'])
print(bus1.passengers)
bus1.drive()
print(bus1.get_warnings())
