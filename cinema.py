
class Star_Cinema:
    _hall_list = []  

    def __init__(self, name):
        self.__name = name  
    def entry_hall(self, hall_no, row, col):
        hall = Hall(hall_no, row, col)
        Star_Cinema._hall_list.append(hall)  

    @classmethod
    def get_hall_list(cls):
        return cls._hall_list  

class Hall:
    def __init__(self, hall_no, row, col):
        self.__hall_no = hall_no  
        self.__row = row  
        self.__col = col  
        self.__show_list = []  
        self.__seats = {}  

    def __repr__(self):
        return f'Hall Number: {self.__hall_no}\n'

    

    def entry_show(self, show_id, movie_name, time):
        show = (show_id, movie_name, time)
        self.__show_list.append(show)

        
        seat_allocation = [[["0" for _ in range(self.__col)]] for _ in range(self.__row)]

        
        self.__seats[show_id] = seat_allocation

    def book_seats(self, show_id, r, c):
        if show_id in self.__seats:
            if 0 <= r < self.__row and 0 <= c < self.__col:
                seat_allocation = self.__seats[show_id]
                if seat_allocation[r][c] == "0":
                    seat_allocation[r][c] = "1"
                    print(f"Seat ({r},{c}) booked for show ID {show_id}.")
                else:
                    print(f"Seat ({r},{c}) is already booked.")
            else:
                print("Invalid seat. Please select a valid row and column.")
        else:
            print("No show found with this ID, please select another one.")

    def view_show_list(self):
        for sh in self.__show_list:
            print(f"Show ID: {sh[0]}, Movie Name: {sh[1]}, Time: {sh[2]}")

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            seat_arrangement = self.__seats[show_id]
            for row in seat_arrangement:
                print(" ".join(row))
        else:
            print("No seat arrangement found for this show ID.")



star_cine = Star_Cinema('star_cine')
star_cine.entry_hall(110, 5, 5)
star_cine.entry_hall(112, 5, 5)
star_cine.entry_hall(111, 5, 5)


hall_list = Star_Cinema.get_hall_list()

hall1 = hall_list[0]
hall1.entry_show(1, "Inception", "17-9-24 15:00")
hall1.entry_show(2, "Spiderman", "17-9-24 18:00")
hall1.entry_show(3, "Tufan", "17-9-24 21:00")
hall2 = hall_list[1]
hall2.entry_show(1, "Poran", "17-9-24 15:00")
hall2.entry_show(2, "Godfather", "17-9-24 18:00")
hall2.entry_show(3, "Moner", "17-9-24 21:00")
hall3 = hall_list[2]
hall3.entry_show(1, "Don", "17-9-24 15:00")
hall3.entry_show(2, "Jurassic", "17-9-24 18:00")
hall3.entry_show(3, "Superman", "17-9-24 21:00")

print("\n---------WELCOME TO STAR CINEPLEX------------")
start = True

while start:
    print("\nChoose an option:\n")
    print("1. Show Hall List")
    print("2. Select hall")
    print("3. Exit")
    op = input('Enter an option: \n')
    
    if op == '1':
        print("Available Halls:", [hall.get_hall_no() for hall in Star_Cinema.get_hall_list()])

    elif op == '2':
        valid_hall = False
        while not valid_hall:
            hall_no = int(input('Enter Hall Number: \n'))
            for hall in Star_Cinema.get_hall_list():
                if hall.get_hall_no() == hall_no:
                    cur_hall = hall
                    valid_hall = True
                    break
            else:
                print('Invalid Hall Number! Please try again.\n')

        hall_menu = True
        while hall_menu:
            print(f"\nHall Number: {cur_hall.get_hall_no()}\n")
            print("Choose an option:\n")
            print("1. View All Shows Today")
            print("2. View Available Seats for a Show")
            print("3. Book Ticket")
            print("4. Back to Main Menu \n")
            option = input('Enter an option: ')

            if option == '1':
                cur_hall.view_show_list()

            elif option == '2':
                show_id = int(input('Enter Show ID: '))
                cur_hall.view_available_seats(show_id)

            elif option == '3':
                show_id = int(input('Enter Show ID: '))
                row = int(input('Enter Row: '))
                col = int(input('Enter Column: '))
                cur_hall.book_seats(show_id, row, col)

            elif option == '4':
                hall_menu = False

            else:
                print('Invalid Option! Please choose again.')

    elif op == '3':
        start = False

    else:
        print('Invalid Option! Please try again.')
