from abc import ABC, abstractmethod
class Vehicle(ABC):  
    def __init__(self, number, total_seats):
        self.number = number          # Bus number
        self.total_seats = total_seats  # Total seats in the bus  
    @abstractmethod
    def calculate_fare(self):
        pass   
    def show_details(self):
        print("Bus Number = ",self.number)
        print("Total Seats = ",self.total_seats)
class LuxuryBus(Vehicle):
    def __init__(self, number, total_seats):
        super().__init__(number, total_seats)
    def calculate_fare(self):
        fare = 500
        return fare  
class OrdinaryBus(Vehicle):
    def __init__(self, number, total_seats):
        super().__init__(number, total_seats)    
    def calculate_fare(self):
        fare = 200
        return fare
class SeatManager: 
    def __init__(self, total_seats):
        self.__total_seats = total_seats   # total seats available
        self.__booked = []                  # list storing booked seat numbers 
    def book_seat(self):
        if len(self.__booked) < self.__total_seats: # New seat number = length of booked list + 1
            New_seat_number = len(self.__booked) + 1
            self.__booked.append(New_seat_number)
            return New_seat_number
        else:# Bus is full
            return None    
    def cancel_seat(self, seat_no):
        if seat_no in self.__booked:
            self.__booked.remove(seat_no)
            return "Seat Cancelled"
        else:
            return "Invalid Seat Number"  
    def available_seats(self):
        return self.__total_seats - len(self.__booked)   
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def show(self):
        print("Passenger Name: ",self.name)
        print("Passenger Age: ",self.age)
class Ticket:
    def __init__(self, passenger, bus, seat_no, fare):
        self.passenger = passenger
        self.bus = bus
        self.seat_no = seat_no
        self.fare = fare 
    def show_ticket(self):
        print("Passenger Name: ",self.passenger.name)
        print("Bus Number: ",self.bus.number)
        print("Seat Number: ",self.seat_no)
        print("Fare: Rs.",self.fare)

print("\nSelect Bus Type:")
print("1. Luxury Bus (Fare: Rs.500)")
print("2. Ordinary Bus (Fare: Rs.200)")
choice = input("Enter your choice (1/2): ")
bus_number = input("Enter Bus Number: ")
total_seats = 5  # Total seats in the bus
if choice == "1":
    bus = LuxuryBus(bus_number, total_seats)
    print("\nYou selected Luxury Bus")
else:
    bus = OrdinaryBus(bus_number, total_seats)
    print("\nYou selected Ordinary Bus")
print(f"Fare: Rs.{bus.calculate_fare()}")
seat_manager = SeatManager(total_seats)
tickets = []
while True:
    print("1. Available Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Show Tickets")
    print("5. Exit")
    option = input("Enter your choice (1-5): ")
    if option == "1":
        print(f"\nAvailable Seats: {seat_manager.available_seats()}")
    elif option == "2":
        name = input("Enter Passenger Name: ")
        age = int(input("Enter Passenger Age: "))
        seat_no = seat_manager.book_seat()           
        if seat_no is None:
            print("\nBus is Full!")
        else:
            passenger = Passenger(name, age)
            fare = bus.calculate_fare()
            ticket = Ticket(passenger, bus, seat_no, fare)
            tickets.append(ticket)               
            print(f"\nSeat Booked Successfully!")
    elif option == "3":
        seat_no = int(input("Enter Seat Number to Cancel: "))
        if seat_manager.cancel_seat(seat_no):
            print(f"\nSeat {seat_no} Cancelled Successfully!")
            for ticket in tickets:
                if ticket.seat_no == seat_no:
                    tickets.remove(ticket)
                    break
        else:
            print(f"\nInvalid Seat Number! Seat {seat_no} not found.")
    elif option == "4":
        if len(tickets) == 0:
            print("\nNo tickets booked yet!")
        else:
            print("\n--- All Booked Tickets ---")
            for ticket in tickets:
                ticket.show_ticket()
    elif option == "5":
        print("\nThank you for using Bus Ticket Booking System \nHave a safe journey")
        break        
    else:
        print("\nInvalid Choice! Please enter a number between 1-5.")