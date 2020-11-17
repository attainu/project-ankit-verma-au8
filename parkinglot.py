import sys


class Car:
    def __init__(self, reg_no, colour):
        self.reg_no = reg_no
        self.colour = colour

    def getcolour(self):
        print("My colour is", self.colour)

    def getregnumber(self):
        print("My registered number is", self.reg_no)


class Parkinglot:
    def __init__(self, noofslot):
        self.noofslot = noofslot
        self.slots = [0 for i in range(self.noofslot)]
        print("Created Parking lot of Capacity", self.noofslot)

    def park(self, vehicle):
        if len(vehicle.reg_no) != 13:
            print("Not a valid reg.no, Please enter a valid reg. no.")
        else:
            for i in range(len(self.slots)):
                if self.slots[i] == 0:
                    self.slots[i] = vehicle
                    print("Allocated slot number", i+1)
                    break
            else:
                print("Sorry! No slots avialable.")
                print("If need more slots, use command: 'add_slot N'")

    def addslot(self, N):
        for i in range(N):
            self.slots.append(0)
        print(N, "slots added in parking lot.")

    def leave(self, slotnumber):
        self.slots[slotnumber - 1] = 0
        print("Slot number", slotnumber, "is free")

    def status(self):
        print("Slot No. ", end="")
        print("Reg. No. ", end="")
        print("Colour ")
        for i in range(len(self.slots)):
            if self.slots[i] != 0:
                print(i+1, end="        ")
                target_car = self.slots[i]
                print(target_car.reg_no, end="     ")
                print(target_car.colour)
            else:
                print("Slot number", i+1, "is free")

    def find_reg_no_by_colour(self, colour):
        car_found = []
        for i in range(len(self.slots)):
            if self.slots[i] != 0 and self.slots[i].colour == colour:
                target_car = self.slots[i]
                car_found.append(target_car)
        if len(car_found) == 0:
            print("Sorry! No car of this colour is present in parking Lot.")
        else:
            for car in car_found:
                print(car.reg_no, end=" ")
            print("")

    def find_car_by_reg_no(self, reg_no):
        for i in range(len(self.slots)):
            if self.slots[i] != 0 and self.slots[i].reg_no == reg_no:
                print(i+1)
                break
        else:
            print("This car is not in parking lot")

    def find_slots_by_colour(self, colour):
        car_found = []
        for i in range(len(self.slots)):
            if self.slots[i] != 0 and self.slots[i].colour == colour:
                car_found.append(i+1)
        if len(car_found) == 0:
            print("Sorry! No car of this colour is present in parking Lot.")
        else:
            for j in car_found:
                print(j, end=" ")
            print("")


def main():
    print("")
    print("Welcome to our Parking Lot!")
    print("These are some commands that we accept.")
    print("")
    print("Create a parking lot of capacity N: 'create_parking_lot N'")
    print("To park the car: 'park KA-01-HH-1234 White'")
    print("To take your car: 'leave 4'")
    print("To check status of parking Lot: 'status'")
    print("reg_nos of clrs:'registration_numbers_for_cars_with_colour White'")
    print("car by reg_no: 'slot_number_for_registration_number KA-01-HH-3141'")
    print("slots by colour: 'slot_numbers_for_cars_with_colour White'")
    print("")

    while True:
        input_cmd = input("Please enter your command:")
        if "create_parking_lot" in input_cmd:
            cmd, cap_string = input_cmd.split()
            capacity = int(cap_string)
            parking_lot = Parkinglot(capacity)
        elif "park" in input_cmd:
            cmd, reg_str, colour = input_cmd.split()
            vehicle = Car(reg_str, colour)
            parking_lot.park(vehicle)
        elif "status" in input_cmd:
            parking_lot.status()
        elif "leave" in input_cmd:
            cmd, slot_no = input_cmd.split()
            parking_lot.leave(int(slot_no))
        elif "add_slot" in input_cmd:
            cmd, noofslots_str = input_cmd.split()
            noofslots = int(noofslots_str)
            parking_lot.addslot(noofslots)
        elif "registration_numbers_for_cars_with_colour" in input_cmd:
            cmd, colour = input_cmd.split()
            parking_lot.find_reg_no_by_colour(colour)
        elif "slot_number_for_registration_number" in input_cmd:
            cmd, reg_str = input_cmd.split()
            parking_lot.find_car_by_reg_no(reg_str)
        elif "slot_numbers_for_cars_with_colour" in input_cmd:
            cmd, colour = input_cmd.split()
            parking_lot.find_slots_by_colour(colour)
        elif "exit" in input_cmd:
            break
        else:
            print("Please enter a correct command")


if __name__ == "__main__":

    # if file name is not prtovided in the argument
    if len(sys.argv) == 1:
        main()
    # if file name is provided in the provided
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            for line in f:
                input_cmd = line
                if "create_parking_lot" in input_cmd:
                    cmd, cap_string = input_cmd.split()
                    capacity = int(cap_string)
                    parking_lot = Parkinglot(capacity)
                elif "park" in input_cmd:
                    cmd, reg_str, colour = input_cmd.split()
                    vehicle = Car(reg_str, colour)
                    parking_lot.park(vehicle)
                elif "status" in input_cmd:
                    parking_lot.status()
                elif "leave" in input_cmd:
                    cmd, slot_no = input_cmd.split()
                    parking_lot.leave(int(slot_no))
                elif "registration_numbers_for_cars_with_colour" in input_cmd:
                    cmd, colour = input_cmd.split()
                    parking_lot.find_reg_no_by_colour(colour)
                elif "slot_number_for_registration_number" in input_cmd:
                    cmd, reg_str = input_cmd.split()
                    parking_lot.find_car_by_reg_no(reg_str)
                elif "slot_numbers_for_cars_with_colour" in input_cmd:
                    cmd, colour = input_cmd.split()
                    parking_lot.find_slots_by_colour(colour)
                else:
                    print("Please enter a correct command")
    # if arguments are more than two
    else:
        print("Sorry! Not a valid command!")
        exit
