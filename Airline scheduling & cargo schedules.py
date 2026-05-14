# Expert System - Airline and Cargo Scheduling

def airline_system():

    print("=== Airline Expert System ===")

    name = input("Enter Customer Name: ")
    travel_type = input("Passenger or Cargo: ").lower()
    destination = input("Enter Destination: ")

    # Passenger Service
    if travel_type == "passenger":

        luggage = int(input("Enter Luggage Weight (kg): "))

        if destination.lower() in ["mumbai", "delhi", "pune"]:
            flight = "Domestic Flight"
            price = 5000
        else:
            flight = "International Flight"
            price = 25000

        # Extra luggage charge
        if luggage > 20:
            extra = (luggage - 20) * 100
        else:
            extra = 0

        total = price + extra

        print("\n=== Passenger Details ===")
        print("Name :", name)
        print("Destination :", destination)
        print("Flight :", flight)
        print("Ticket Price : ₹", price)
        print("Extra Charge : ₹", extra)
        print("Total Amount : ₹", total)

    # Cargo Service
    elif travel_type == "cargo":

        weight = int(input("Enter Cargo Weight (kg): "))

        if weight <= 50:
            charge = 2000
            service = "Light Cargo"
        elif weight <= 200:
            charge = 5000
            service = "Medium Cargo"
        else:
            charge = 10000
            service = "Heavy Cargo"

        print("\n=== Cargo Details ===")
        print("Name :", name)
        print("Destination :", destination)
        print("Cargo Service :", service)
        print("Shipping Charge : ₹", charge)

    else:
        print("Invalid Input")

if __name__ == "__main__":
    airline_system()



#INPUT

#Enter Customer Name: Diya
#Passenger or Cargo: passenger
#Enter Destination: Mumbai
#Enter Luggage Weight (kg): 25
