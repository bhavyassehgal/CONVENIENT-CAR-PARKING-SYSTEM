class Car:
    # Constructor to declare initialize data members of the class. Following are the data members of the Car class:

    # private:
    # CONST_LICENSE_NUMBER stores car's license number
    def __init__(self, license_number):

        # initialize the variables
        self._CONST_LICENSE_NUMBER = license_number

    # method to get the car's license number
    def get_license_number(self):
        return self._CONST_LICENSE_NUMBER
