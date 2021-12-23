import time
import Car
import LicensePlateRecognition
import ParkingLot

# PLEASE edit these variables according to the usage

# All images are stored in the 'Images' folder
# If someone add more images in the 'Images' folder, please add the same images in the cars list in the same manner as given below
cars = ["Images/image_1.jpg", "Images/image_2.jpg", "Images/image_3.jpg", "Images/image_5.jpg"]
# Time before next photo should be displayed
time_delay = 1
# Details of the parking lot
parking_lot_capacity = 10
fixed_cost_for_an_hour = 50
cost_per_half_hour_interval = 25

# Create a parking lot
parking_lot = ParkingLot.Parking_Lot(parking_lot_capacity, fixed_cost_for_an_hour, cost_per_half_hour_interval)

# Get the car images and add cars to the parking lot if not present, if car is already present then remove it and print its receipt
for each_car_image in cars:
    # Obtain the car license from each car image
    license_plate_recognition = LicensePlateRecognition.LicensePlateRecognition(each_car_image)
    car_license = license_plate_recognition.get_license_number()

    # Create a car to add to the parking_lot
    car = Car.Car(car_license)

    # Add the car to the parking_lot
    parking_lot.scan_car(car)

    # Display the parking lot
    parking_lot.display_parking_lot()

    # Wait for some time
    time.sleep(time_delay)
    
    #code by: BHAVYA SEHGAL
