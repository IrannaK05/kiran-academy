import random

def run_cab_chatbot():
    # Predefined Cab Rates per km
    cab_rates = {
        1: ("Auto", 12),
        2: ("Sedan", 18),
        3: ("SUV", 25)
    }

    # Predefined Routes (Route No. -> Source, Destination, Distance)
    routes = {
        1: ("Pune Station", "Shivajinagar", 5),
        2: ("Swargate", "Kothrud", 8),
        3: ("Hinjawadi", "Wakad", 10)
    }

    print("==================================================")
    print("      WELCOME TO KIRAN ACADEMY CAB BOOKING       ")
    print("==================================================")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Book Ride")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            # Step 2: Choose Cab Type
            print("\n--- CHOOSE CAB TYPE ---")
            print("1. Auto (₹12/km)")
            print("2. Sedan (₹18/km)")
            print("3. SUV (₹25/km)")
            
            try:
                cab_choice = int(input("Select cab type (1-3): "))
                if cab_choice not in cab_rates:
                    print("❌ Invalid cab choice! Returning to Main Menu.")
                    continue
            except ValueError:
                print("❌ Invalid input! Please enter a number between 1 and 3.")
                continue

            cab_name, rate_per_km = cab_rates[cab_choice]

            # Step 3: Choose Route
            print("\n--- CHOOSE ROUTE ---")
            for r_no, (src, dest, dist) in routes.items():
                print(f"{r_no}. {src} to {dest} ({dist} km)")

            try:
                route_choice = int(input("Select route number (1-3): "))
                if route_choice not in routes:
                    print("❌ Invalid route choice! Returning to Main Menu.")
                    continue
            except ValueError:
                print("❌ Invalid input! Please enter a valid route number.")
                continue

            source, destination, distance = routes[route_choice]

            # Step 4: Calculate Fare
            total_fare = rate_per_km * distance

            print("\n----------------- RIDE SUMMARY -----------------")
            print(f"Cab Type    : {cab_name} (₹{rate_per_km}/km)")
            print(f"Route       : {source} -> {destination}")
            print(f"Distance    : {distance} km")
            print(f"Total Fare  : ₹{total_fare}")
            print("--------------------------------------------------")

            # Step 5: Cancellation Before OTP
            print("\n--- CONFIRMATION ---")
            print("1. Confirm & Share OTP")
            print("2. Cancel Ride")
            
            confirm_choice = input("Enter your choice (1 or 2): ").strip()

            if confirm_choice == '2':
                print("\n❌ Ride cancelled successfully before OTP generation. Returning to Main Menu.")
                continue
            elif confirm_choice != '1':
                print("\n❌ Invalid choice! Defaulting to ride cancellation for safety. Returning to Main Menu.")
                continue

            # Step 6: OTP and Ride Lock
            otp = random.randint(1000, 9999)
            print(("\n🔒 Your 4-digit OTP is: **{}**").format(otp))
            print("ℹ️  Rule: Once the OTP has been shared, the ride cannot be cancelled.")
            print("✅ Booking confirmed! Thank you for booking with us.")

        elif choice == '2':
            print("\nThank you for using Kiran Academy Cab Booking Chatbot. Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid menu choice! Please enter 1 to Book Ride or 2 to Exit.")

if __name__ == "__main__":
    run_cab_chatbot()