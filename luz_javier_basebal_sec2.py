from dp_sec2 import read_players, write_players
from datetime import date, time, datetime, timedelta


#date
def display_date():
    try:
        
        now = datetime.now()
        date_format = "%Y - %m - %d"
        current_date = datetime(now.year, now.month, now.day)
        print(f"CURRENT DATE: {current_date.strftime(date_format)}")
        game_date_str  = input("GAME DATE: ")

        game_date = datetime.strptime(game_date_str, "%Y - %m - %d")
        until_game = (game_date - current_date)

        if current_date > game_date:
            print("DAYS UNTIL GAME: \n")
        else:
            print(f"DAYS UNTIL GAME: {until_game.days}")
            print()
    except ValueError:
        print("DAYS UNTIL GAME: \n")
    

def display_menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    

def display_lineup(lineup):
   print("        Player          POS     AB     H       AVG")
   print("-" * 64)

   if len(lineup) == 0:
       print("There is no players on the list.")
       return
   else:
       i = 1
       for player in lineup:
           #print(f"{str(i)}       {player['name']}             {player['position']}       {str(player['at_bats'])}      {str(player['hits'])}       {player['average']:.3f}")
           print(f"{str(i)}       {player['name']:<15} {player['position']:<7} {str(player['at_bats']):<6} {str(player['hits']):<7} {player['average']:.3f}")
           i += 1
       print()
        
                       

def add_player(lineup, positions):
   name = input("Name: ")
   while True:
       try:
           position = input("Position: ").upper()
           if position not in positions:
               print("Invalid position. Please enter a valid position.")
               continue

           at_bats = int(input("At bats: "))
           hits = int(input("Hits: "))
           average = round(hits / at_bats, 3) if at_bats > 0 else 0.0

           new_player = {'name': name,
               'position': position,
               'at_bats': at_bats,
               'hits': hits,
               'average': average}
           lineup.append(new_player)
           print(f"{name} was added.\n")
           
           
           break

       except ValueError:
           print("Input is not an int. Please try again.")
                       
    
    

def remove_player(lineup):
    number = int(input("Number: "))
    if number < 1 or number > len(lineup):
        print("Invalid player number. Please try again.")
    else:
        player = lineup.pop(number - 1)
        print(f"{player['name']} was deleted.\n")
            
    

def move_player(lineup):
    while True:
        try:
            number = int(input("Lineup number: "))
            if number < 1 or number > len(lineup):
                print("Invalid lineup number.Please try again.")
            else:
                player = lineup.pop(number - 1)
                print(f"{player['name']} was selected.")
            while True:
                new_number = int(input("new lineup number: "))
                if new_number < 1 or new_number > len(lineup):
                    print("Invalid lineup number. Please try again.")
                else:
                    lineup.insert(new_number - 1, player)
                    print(f"{player['name']} was moved.\n")
                    return
                    

            

        except ValueError:
            print("Invalid integer. Please try again.")
        except IndexError:
            print("Invalid index.Please try again.")
                             
          
    
def edit_position(lineup, positions):
    while True:
        try:
            number = int(input("Lineup number: "))
            if number < 1 or number > len(lineup):
                print("Invalid lineup number.Please try again.")
        
            else:
                player_index = number - 1
                player = lineup.pop(player_index)
                print(f"You selected {player['name']} POS = {player['position']}")
                
            while True:
                new_position = input("Position: ").upper()
                if new_position not in positions:
                    print("Invalid position. Please enter a valid position.")
                else:
                    player['position'] = new_position
                    lineup.insert(player_index, player)
                    print(f"{player['name']} was updated.\n")
                    return new_position

                
        except ValueError:
            print("Invalid integer. Please try again.")
        except IndexError:
            print("Invalid index.Please try again.")
            

                   


def edit_stats(lineup):
    while True:
        try:
            number = int(input("Lineup number: "))
            if number < 1 or number > len(lineup):
                print("Invalid lineup number. Please try again.")
                continue
            else:
                player_index = number - 1
                player = lineup[player_index]
                print(f"You selected {player['name']} POS = {player['position']}")

                while True:
                    at_bats = int(input("New at bats: "))
                    if at_bats < 0:
                        print("Number of at-bats cannot be negative. Please try again.")
                        continue
                    else:
                        break

                while True:
                    hits = int(input("New hits: "))
                    if hits < 0:
                        print("Number of hits cannot be negative. Please try again.")
                        continue
                    elif hits > at_bats:
                        print("Number of hits cannot be greater than at-bats. Please try again.")
                        continue
                    else:
                        break

                if at_bats == 0:
                    average = 0.0
                else:
                    average = round(hits/at_bats, 3)

                player['at_bats'] = at_bats
                player['hits'] = hits
                player['average'] = average

                print(f"{player['name']} stats were updated.\n")
                return player

        except ValueError:
            print("Invalid integer. Please try again.")
        except IndexError:
            print("Invalid index. Please try again.")

        
        
        

def main():
    filename = "players.csv"
    lineup = read_players(filename)
   
    
    

    
    print("=" * 64)
    print("=" * 64)
    print("\t\t\tBaseball Team Manager\t\t\t\t")
    
    display_date()
    display_menu()

    positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P") #tuple
    (one, two, three, four, five, six, seven, eight, nine) = positions
    
    print("POSITIONS")
    #processing the tuple of valid positions
    print(f"{one}, {two}, {three}, {four}, {five}, {six}, {seven}, {eight}, {nine}")
    print("=" * 64)

    if not lineup:
        lineup = [
        {'name': "Tommy", 'position': "3B", 'at_bats': 1316, 'hits':360, 'average':0.274},
        {'name':"Mike", 'position': "RF", 'at_bats': 563, 'hits': 360, 'average': 0.275},
        {'name':"Donovan", 'position': "2B", 'at_bats':1473, 'hits': 407, 'average': 0.276},
        {'name': "Buster", 'position': "C", 'at_bats': 4575, 'hits': 1380, 'average': 0.302},
        {'name': "Brandon", 'position': "1B", 'at_bats': 3811, 'hits': 1003, 'average':0.263},
        {'name': "Brandon", 'position': "SS", 'at_bats': 4402, 'hits': 1099, 'average':0.25},
        {'name': "Alex", 'position': "LF", 'at_bats': 586, 'hits': 160, 'average':0.273},
        {'name': "Austin", 'position': "CF", 'at_bats': 569, 'hits': 147, 'average': 0.258},
        {'name': "Kevin", 'position': "P", 'at_bats': 56, 'hits': 2, 'average': 0.036}]
    
    
    while True:
        option = int(input("Menu option: "))

        if option == 1:
            display_lineup(lineup)
        elif option == 2:
            add_player(lineup, positions)
        elif option == 3:
            remove_player(lineup)
        elif option == 4:
            move_player(lineup)
        elif option == 5:
            edit_position(lineup, positions)
        elif option == 6:
            edit_stats(lineup)
        elif option == 7:
            write_players(filename, lineup)
            break
        else:
            print("Error. Not a valid option. Please try again.\n")
            display_menu()
    print("Bye!")
            
            
        
if __name__ == "__main__":
    main()

