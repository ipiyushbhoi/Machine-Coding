import random


class RideSharing():

    def __init__(self):
        self.in_memory_db = []

    def add_user(self, name, gender, age):
        dict = {
            "name": name,
            "user_info":
                {
                    "gender": gender,
                    "age": age
                }
        }
        for element in self.in_memory_db:
            if element['name'] == name:
                print(f'User {name} already exists')
                return 1

        self.in_memory_db.append(dict)
        print(f'User {name} added successfully')
        return 0

    def add_vehicle(self, name, car, car_number):

        dict = {
            "vehicle_details":
                {
                    "car": [],
                    "car_number": []
                }
        }
        for element in self.in_memory_db:
            if element['name'] == name:
                if "vehicle_details" in element.keys():
                    car_list = element["vehicle_details"]["car"]
                    car_number_list = element["vehicle_details"]["car_number"]
                    car_list.append(car)
                    car_number_list.append(car_number)
                    element["vehicle_details"]["car"] = car_list
                    element["vehicle_details"]["car_number"] = car_number_list
                else:
                    dict["vehicle_details"]["car"] = car
                    dict["vehicle_details"]["car_number"] = car_number
                    element.update(dict)
                print(f'Car details added successfully')
                return 0
        print(f'User {name} does not exist')
        return 1

    def offer_ride(self, name, Origin=None, Available_seats=None, Vehicle=None, Car_number=None, Destination=None):
        dict = {
            "ride_details":
                {
                    "origin": [],
                    "available_seats": [],
                    "vehicle": [],
                    "car_number": [],
                    "destination": []
                }
        }

        for element in self.in_memory_db:
            if Vehicle not in element["vehicle_details"]["car"] and Car_number not in element["vehicle_details"]["car_number"]:
                print(f'Car {Vehicle} with number {Car_number} is not assigned to {name}')
                return 1
        for element in self.in_memory_db:
            if element['name'] == name:
                if "ride_details" in element.keys():
                    origin_list = self.in_memory_db["name"]["ride_details"]["origin"],
                    available_seats_list = self.in_memory_db["name"]["ride_details"]["available_seats"],
                    vehicle_list = self.in_memory_db["name"]["ride_details"]["vehicle"],
                    car_number_list = self.in_memory_db["name"]["ride_details"]["car_number"],
                    destination = self.in_memory_db["name"]["ride_details"]["destination"]

                    if Vehicle in vehicle_list and Car_number in car_number_list:
                        print(f'Car {Vehicle} with number {Car_number} is already booked for different route.')
                        return 1

                    origin_list.append(Origin)
                    available_seats_list.append(Available_seats)
                    vehicle_list.append(Vehicle)
                    car_number_list.append(Car_number)
                    destination.append(Destination)

                    element["name"]["ride_details"]["origin"] = origin_list,
                    element["name"]["ride_details"]["available_seats"] = available_seats_list,
                    element["name"]["ride_details"]["vehicle"] = vehicle_list,
                    element["name"]["ride_details"]["car_number"] = car_number_list,
                    element["name"]["ride_details"]["destination"] = destination
                else:
                    dict["name"]["ride_details"]["origin"] = Origin,
                    dict["name"]["ride_details"]["available_seats"] = Available_seats,
                    dict["name"]["ride_details"]["vehicle"] = Vehicle,
                    dict["name"]["ride_details"]["car_number"] = Car_number,
                    dict["name"]["ride_details"]["destination"] = Destination
                    dict.update(dict)
                print(f'Ride details added successfully')
                return 0
        print(f'User {name} does not exist')
        return 1

if __name__ == "__main__":
    obj1 = RideSharing()
    obj1.add_user('Rohan', 'M', 36)
    obj1.add_vehicle('Rohan', 'Swift', 'KA-01-12345')

    print(obj1.in_memory_db)