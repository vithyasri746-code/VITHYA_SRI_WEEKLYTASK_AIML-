# ---------------- MAIN MENU ----------------

def main_menu():

    print("\n****** SMARTBUS ******")
    print("1. View Buses")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")


# ---------------- BUS INFORMATION ----------------

def bus_information():

    buses = {
        1: {
            "number": "SB101",
            "from": "Chennai",
            "to": "Bangalore",
            "time": "09:00 AM",
            "type": "AC Sleeper",
            "fare": 800
        },
        2: {
            "number": "SB102",
            "from": "Chennai",
            "to": "Madurai",
            "time": "10:00 AM",
            "type": "AC Seater",
            "fare": 600
        },
        3: {
            "number": "SB103",
            "from": "Chennai",
            "to": "Coimbatore",
            "time": "08:00 AM",
            "type": "Non-AC",
            "fare": 500
        },
        4: {
            "number": "SB104",
            "from": "Chennai",
            "to": "Trichy",
            "time": "07:30 AM",
            "type": "AC Seater",
            "fare": 550
        },
        5: {
            "number": "SB105",
            "from": "Chennai",
            "to": "Salem",
            "time": "11:00 AM",
            "type": "Non-AC",
            "fare": 450
        },
        6: {
            "number": "SB106",
            "from": "Chennai",
            "to": "Pondicherry",
            "time": "06:30 AM",
            "type": "AC Seater",
            "fare": 400
        },
        7: {
            "number": "SB107",
            "from": "Chennai",
            "to": "Tirunelveli",
            "time": "09:30 PM",
            "type": "AC Sleeper",
            "fare": 900
        },
        8: {
            "number": "SB108",
            "from": "Chennai",
            "to": "Kanyakumari",
            "time": "08:30 PM",
            "type": "AC Sleeper",
            "fare": 1000
        }
    }

    print("\n===== AVAILABLE BUSES =====")

    for key, bus in buses.items():

        print(
            key,
            "-",
            bus["number"],
            "-",
            bus["from"],
            "to",
            bus["to"],
            "-",
            bus["time"],
            "-",
            bus["type"],
            "- Rs.",
            bus["fare"]
        )

    return buses


# ---------------- BUS SELECTION ----------------

def bus_selection(buses):

    print("\n===== BUS SELECTION =====")

    for key, bus in buses.items():

        print(key, "-", bus["number"])

    while True:

        choice = int(input("Enter bus choice: "))

        if choice in buses:

            print("Selected Bus:", buses[choice]["number"])

            return buses[choice]

        else:

            print("Oops.. Invalid choice! Try again")


# ---------------- SEAT MANAGEMENT ----------------

def seat_management():

    booked_seat = []
    r = 0

    seat = [
        'a1','a2','a3','a4','a5',
        'a6','a7','a8','a9','a10',
        's1','s2','s3','s4','s5'
    ]

    print("\nSeat's display:")
    print("    Seater  Sleeper")
    print("    a1  a2       s1")
    print("    a3  a4       s2")
    print("    a5  a6       s3")
    print("    a7  a8       s4")
    print("    a9  a10      s5")

    n = int(input("Enter number of seats: "))

    while True:

        selected_seat = input("Enter your seat: ").lower()

        if selected_seat in seat and selected_seat not in booked_seat:

            print("Seat is available")
            booked_seat.append(selected_seat)
            r = r + 1

        elif selected_seat in booked_seat:

            print("Already Booked. Please try again!")

        else:

            print("Invalid seat. Please try again!")

        if r == n:

            print("Your seats are booked now :)")
            break

    return booked_seat


# ---------------- PASSENGER DETAILS ----------------

def passenger_details():

    print("----- Passenger Details -----")

    name = input("Enter Passenger Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    phone = input("Enter Phone Number: ")
    passenger_id = input("Enter Passenger ID: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    print("\n----- Passenger Information -----")

    print("Passenger Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Phone Number:", phone)
    print("Passenger ID:", passenger_id)
    print("Source:", source)
    print("Destination:", destination)

    return name, age, gender, phone, passenger_id, source, destination


# ---------------- BOOKING ----------------

bookings = []


def booking(name, age, gender, phone, passenger_id,
            source, destination, selected_seats):

    booking_id = "SB" + str(len(bookings) + 1).zfill(3)

    booking_data = {

        "booking_id": booking_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "passenger_id": passenger_id,
        "source": source,
        "destination": destination,
        "seat": selected_seats,
        "status": "CONFIRMED"
    }

    bookings.append(booking_data)

    print("\n--- Booking Successful ---")

    print("Booking ID:", booking_id)
    print("Passenger:", name)
    print("Age:", age)
    print("Phone:", phone)
    print("Status:", booking_data["status"])

    return booking_data


# ---------------- FARE CALCULATION ----------------

def fare_calculation(basic_fare, number_of_seats):

    extra_charge = 0

    total_fare = basic_fare * number_of_seats

    discount = total_fare * 0.10

    total_amount = total_fare + extra_charge - discount

    print("\n===== FARE CALCULATION =====")

    print("Basic Fare   : ₹", basic_fare)
    print("Extra Charge : ₹", extra_charge)
    print("Discount     : ₹", discount)
    print("Total Amount : ₹", total_amount)

    return total_amount


# ---------------- PAYMENT ----------------

def payment(amount):

    print("\n===== PAYMENT =====")

    print("Total Amount: ₹", amount)

    print("1.UPI")
    print("2.Card")
    print("3.Cash")

    choice = input("Choose payment method(enter number):")

    if choice == "1":

        method = "UPI"

    elif choice == "2":

        method = "Card"

    elif choice == "3":

        method = "Cash"

    else:

        print("Invalid choice")
        return None, "FAILED"

    payment_status = "Successful"

    print("Payment Method:", method)
    print("Payment Status:", payment_status)

    return method, payment_status


# ---------------- TICKET DISPLAY ----------------

def ticket_display(booking_data, total_amount,
                   payment_method, payment_status):

    print("\n====================================")
    print("          SMARTBUS E-TICKET")
    print("====================================")

    print("\nBOOKING DETAILS")

    print("Booking ID   :", booking_data["booking_id"])
    print("Passenger ID :", booking_data["passenger_id"])
    print("Name         :", booking_data["name"])
    print("Age          :", booking_data["age"])
    print("Gender       :", booking_data["gender"])
    print("Phone        :", booking_data["phone"])

    print("\nJOURNEY")

    print("Seat         :", booking_data["seat"])
    print("Route        :", booking_data["source"],
          "→", booking_data["destination"])

    print("\nPAYMENT")

    print("Amount       : ₹", total_amount)
    print("Method       :", payment_method)
    print("Status       :", payment_status)

    print("\n*** BOOKING CONFIRMED ***")

    print("Thank you for choosing SmartBus!")
    print("Have a safe journey!")


# ---------------- CANCELLATION ----------------

def cancellation():

    print("\n      CANCELLATION      ")

    booking_id = input("Enter Booking ID(check the booking to find your booking id): ")

    found = False

    for booking_data in bookings:

        if booking_data["booking_id"] == booking_id:

            found = True

            print("Passenger:", booking_data["name"])
            print("Seat:", booking_data["seat"])
            print("Fare:", booking_data["fare"])

            while True:

                choice = input(
                    "Do you want to cancel? (Yes/No): "
                )

                if choice == "Yes" or choice=="y":

                    cancellation_charge = 100

                    refund = booking_data["fare"] - cancellation_charge

                    booking_data["status"] = "CANCELLED"

                    print("Booking Cancelled")
                    print("Cancellation Charge:",
                          cancellation_charge)
                    print("Refund Amount:", refund)

                    break

                elif choice == "No" or choice=="n":

                    print("Cancellation Stopped.")

                    break

                else:

                    print("Invalid choice! Please enter Yes or No.")

            break

    if found == False:

        print("Booking ID not found!")


# ================= MAIN FLOW =================

while True:

    main_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        buses = bus_information()

    elif choice == "2":

        buses = bus_information()

        selected_bus = bus_selection(buses)

        selected_seats = seat_management()

        name, age, gender, phone, passenger_id, source, destination = passenger_details()

        booking_data = booking(
            name,
            age,
            gender,
            phone,
            passenger_id,
            source,
            destination,
            selected_seats
        )

        total_amount = fare_calculation(
            selected_bus["fare"],
            len(selected_seats)
        )

        payment_method, payment_status = payment(total_amount)

        if payment_status == "Successful":

            booking_data["fare"] = total_amount

            ticket_display(
                booking_data,
                total_amount,
                payment_method,
                payment_status
            )

    elif choice == "3":

        cancellation()

    elif choice == "4":

        print("Thank you for using SmartBus!")

        break

    else:
        print("Invalid choice! Please try again.")
