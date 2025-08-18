print("=== 🎬 Movie Ticket Booking System 🎬 ===")
print("==================================================")

movie_list = ["Inception", "Avatar", "Interstellar", "The Dark Knight", "Titanic"]
ticket_prices = [300, 350, 400, 280, 250]
seats = [50, 60, 40, 20, 10]

total_Chosen_data = {}
choice = 0
final_total = 0

while choice != 4:
    print("\n\t=== 📝 Movies List 📝 ===\n")  
    print("--------------------------------------------------")
    print("{:<12}{:<20}{:<12}{:<12}".format("Movie ID", "Movie", "Price", "Seats"))
    print("--------------------------------------------------")
    for i in range(len(movie_list)):
        print("{:<12}{:<20}{:<12}{:<12}".format(i, movie_list[i], ticket_prices[i], seats[i]))
    print("--------------------------------------------------")
    
    print(
          "1. Choose Movie\n" +
          "2. Tickets Left\n" +
          "3. Show Bill\n" +
          "4. Exit\n"
    )
    choice = int(input("Choose any Option:"))
    
    if choice == 1:
        movie_choice = int(input("Choose a Movie(0 - 4):"))
        
        if movie_choice < 0 or movie_choice >= len(movie_list):
            print("Invalid Movie Choice! Please choose a valid movie ID.")
            continue    

        elif seats[movie_choice] == 0:
            print(f"Sorry!! Seats for {movie_list[movie_choice]} has been booked.")
            continue
            
        else:
            chosen_movie = movie_list[movie_choice] 
            if chosen_movie in total_Chosen_data:
                pass
            else:
                total_Chosen_data.update({chosen_movie : 0}) # for list of all selected movies
            
            ticket_choice = int(input("How many Tickets you want:"))
            if chosen_movie in total_Chosen_data:
                total_Chosen_data[chosen_movie] += ticket_choice
            else:
                total_Chosen_data.update({chosen_movie : ticket_choice}) # for list of all Bought Tickets
            
            if ticket_choice > seats[movie_choice]:
                print(f"Sorry!! Only {seats[movie_choice]} Tickets are Left")
                continue
            else:
                seats[movie_choice] -= ticket_choice     
                total_amount = ticket_prices[movie_choice] * ticket_choice 
                
                # Displaying the booking summary
                print("\n=== 📝 Booking Summary 📝 ===")
                print("Seats Booked:", ticket_choice)
                print("Movie Chosen:", movie_list[movie_choice])
                
                # Discount Calculation
                if ticket_choice >= 5:
                    print(f"Total Before Discount: Rs.{total_amount:.2f}")
                    discounted_price = (10/100) * total_amount
                    total_amount -= discounted_price     
                    final_total += total_amount  # For Final Total Bill
                    print("Discount Applied: 10%")
                    print(f"Total After Discount: Rs.{total_amount:.2f}")
                else:
                    discounted_price = 0
                    print("No Discount Applied")
                    print(f"Total Amount: Rs.{total_amount:.2f}")
                    final_total += total_amount  # For Final Total Bill
                
                print("===============================================\n")
                
    elif choice == 2:
        print("\n\t=== 📝 Tickets Left 📝 ===\n")  
        print("--------------------------------------------------")

        print("{:<12}{:<20}{:<12}".format("Movie ID", "Movie", "Left Tickets"))

        print("--------------------------------------------------")

        for i in range(len(movie_list)):
            print("{:<12}{:<20}{:<12}".format(i, movie_list[i], seats[i]))

        print("--------------------------------------------------")
    
    elif choice == 3:
        print("\n\t=== 📝 User Selected Data 📝 ===\n")  
        print("--------------------------------------------------")

        print("{:<20}{:<12}".format("Seleted Movies", "Bought Tickets"))

        print("--------------------------------------------------")

        for key, value in total_Chosen_data.items():
            print("{:<20}{:<12}".format(key, value))    

        print("--------------------------------------------------")

        print(f"Total Selected Movies: {len(total_Chosen_data)}")
        print(f"Total Bought Tickets: {sum(total_Chosen_data.values())}")
        print(f"Your Final Bill: {final_total}")

        print("===================================================")
        
    elif choice == 4:
        print("Thank you for your arrival! 👋")
        exit()
        
    else:

        print("Invalid Choice!!")    
