class Vehicle:
    # If we create attributes in this way every single instance will have the same value
    # top_speed = 100
    # warnings = []
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        # This a convention of private attribute, you can change the attribute if you want
        self.__warnings = []

    # This method always will run every time you use the class
    def __repr__(self):
        print("Printing...")
        return 'Top: {}, Warnings: {}'.format(self.top_speed, len(self.__warnings))

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def get_warnings(self):
        return self.__warnings

    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))
