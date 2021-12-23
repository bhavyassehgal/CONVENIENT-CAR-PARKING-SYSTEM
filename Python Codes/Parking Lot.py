from datetime import datetime
from datetime import timedelta

import Colors

class Parking_Lot:

    # Constructor to declare initialize data members of the class. Following are the data members of the Parking_Lot class:

    # private:
    # _CONST_CAPACITY stores the maximum number of cars that can be parked in the parking lot
    # _car_count stores the current number of cars parked in the parking lot
    # _cost_per_minute stores the cost per minute of staying in the parking lot
    # _car is a dictionary that associates car license number to its arrival time
    # _fixed_cost_for_an_hour is the fixed price that the car must pay for hour or less than an hour stay
    # _cost_per_half_hour_interval is the price that the car must pay per half hour interval after it has stayed for one hour
    def __init__(self, capacity, fixed_cost_for_an_hour, cost_per_half_hour_interval):

        # initialize the variables
        self._CONST_CAPACITY = capacity
        self._car_count = 0
        self._fixed_cost_for_an_hour = fixed_cost_for_an_hour
        self._cost_per_half_hour_interval = cost_per_half_hour_interval
        self._car_lot = {}

        # get the formatted colors
        format_colors = Colors.colors

        # print the initial statistics about the parking
        print(format_colors.BOLD + format_colors.LIGHT_RED + "PARKING LOT STATISTICS: " + format_colors.RESET)
        print(format_colors.BLUE + "-" * 31)
        print('%-27s: %d' % ("Car capacity", self._CONST_CAPACITY))
        print('%-27s: %d' % ("Fixed cost for an hour", self._fixed_cost_for_an_hour))
        print('%-27s: %d' % ("Cost per half hour interval", self._cost_per_half_hour_interval))
        print("-" * 31 + format_colors.RESET)

        # add a new line
        print()

    # private method to add car in the car lot
    def _add_car(self, car):
        self._car_lot[car.get_license_number()] = datetime.time(datetime.now())

    # private method to check if there is parking space available in parking lot
    def _check_parking_space(self):

        # if no space is there, return false
        if self._car_count == self._CONST_CAPACITY:
            return False

        # if space is there, return true
        return True

    # private method to remove car from the parking lot
    def _remove_car(self, car):

        # print the cost of the car before exit
        self._print_cost(car)

        # exit the car, that is, remove it from parking lot
        self._car_lot.pop(car.get_license_number())

    # private method to print the total cost of stay in the parking lot
    def _print_cost(self, car):

        # get the entry and exit time
        entry_time = self._car_lot[car.get_license_number()]
        exit_time = datetime.time(datetime.now())

        # make time delta objects from entry and exit time
        entry_time_delta = timedelta(hours=entry_time.hour, minutes=entry_time.minute, seconds=entry_time.second)
        exit_time_delta = timedelta(hours=exit_time.hour, minutes=exit_time.minute, seconds=exit_time.second)

        # get the time difference
        time_difference = exit_time_delta - entry_time_delta

        # calculate the cost
        cost = self._fixed_cost_for_an_hour
        # if time spent by car is more than 1 hour then add additional charges
        if time_difference.total_seconds() > 3600:
            cost += self._cost_per_half_hour_interval*(time_difference.total_seconds()-3600)/1800

        # get the formatted colors
        format_colors = Colors.colors

        # print the receipt
        print (format_colors.YELLOW + "RECEIPT: " + format_colors.RESET)
        print(format_colors.PINK + "-" * 40)
        print('%-13s\t%-10s\t%-10s\t%-10s' % ("LICENSE", "ENTRY TIME", "EXIT TIME", "COST"))
        print('%-13s\t%-10s\t%-10s\t%-10s' % (car.get_license_number(),  entry_time_delta, exit_time_delta, int(cost)))
        print("-" * 40 + format_colors.RESET)

        # add new line
        print()

    # private method to check if car is present in the parking lot or not
    def _is_present(self, car):

        if car.get_license_number() in self._car_lot:
            return True
        else:
            return False

    # public method that scans a car in the parking lot
    # if the car is already present, then it is removed else it is added in the parking lot
    def scan_car(self, car):

        # Check if car is present in parking lot
        # If its present, then remove it
        if self._is_present(car):
            self._remove_car(car)
        # If its not present, then add it to the parking lot if there is space
        elif self._check_parking_space():
            self._add_car(car)
        # If there is no space, then raise ValueError
        else:
            raise ValueError("No space available in the parking lot!")

    # public method to display cars in the parking lot
    def display_parking_lot(self):

        # get the formatted colors
        format_colors = Colors.colors

        # print the parking lot
        print (format_colors.BOLD + format_colors.RED + "PARKING LOT: " + format_colors.RESET)
        print(format_colors.GREEN + "-"*20)
        print('%-13s\t%-8s' % ("LICENSE", "TIME"))
        for each_car in self._car_lot:
            print('%-13s\t%-8s' % (each_car, self._car_lot[each_car].strftime("%X")))
        print("-" * 20 + format_colors.RESET)

        # add a new line
        print()
