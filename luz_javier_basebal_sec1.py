from dp_sec1 import read_players, write_players

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
    print("        Player          POS     AB      H        AVG")
    print("-" * 64)

    if len(lineup) == 0:
        print("There is no players on the list.")
        return
    else:
        i = 1
        for row in lineup:
           print(f"{str(i)}\t{row[0]}\t\t{row[1]}\t{str(row[2])}\t{str(row[3])}\t{str(row[4])}")
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
                
            while True:
                at_bats = int(input("At bats: "))
                if at_bats < 0:
                    print("Number of at-bats cannot be negative. Please try again.")
                    continue
                else:
                    break
                
            while True:
                hits = int(input("Hits: "))
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

            new_player = [name, position, at_bats, hits, average]
            lineup.append(new_player)
            print(f"{name} was added.\n")
            break
                       
        except ValueError:
            print("Input is not an int.Please try again.")
                       
    
    

def remove_player(lineup):
    number = int(input("Number: "))
    if number < 1 or number > len(lineup):
        print("Invalid player number. Please try again.")
    else:
        player = lineup.pop(number - 1)
        print(f"{player[0]} was deleted.\n")
            
    

def move_player(lineup):
    while True:
        try:
            number = int(input("Lineup number: "))
            if number < 1 or number > len(lineup):
                print("Invalid lineup number.Please try again.")
            else:
                player = lineup.pop(number - 1)
                print(f"{player[0]} was selected.")
            while True:
                new_number = int(input("new lineup number: "))
                if new_number < 1 or new_number > len(lineup):
                    print("Invalid lineup number. Please try again.")
                else:
                    lineup.insert(new_number - 1, player)
                    print(f"{player[0]} was moved.\n")
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
                print(f"You selected {player[0]} POS = {player[1]}")
                
            while True:
                position = input("Position: ").upper()
                if position not in positions:
                    print("Invalid position. Please enter a valid position.")
                else:
                    player[1] = position
                    lineup[player_index] = player
                    print(f"{player[0]} was updated.\n")
                    return

                
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
                print(f"You selected {player[0]} POS = {player[1]}")
                
                
                
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

        
            player[2] = at_bats
            player[3] = hits
            player[4] = average
                        
            print(f"{player[0]} stats were updated.\n")
            return
                        
                        
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
    
    display_menu()

    positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P") #tuple
    print("POSITIONS")
    print(positions[0], positions[1], positions[2], positions[3], positions [4], positions[5], positions[6], positions[7], sep = ", ")
    print("=" * 64)

    lineup = [
        ["Tommy", "3B", 1316, 360, 0.274],
        ["Mike", "RF", 563, 360, 0.275],
        ["Donovan", "2B", 1473, 407, 0.276],
        ["Buster", "C", 4575, 1380, 0.302],
        ["Brandon", "1B", 3811, 1003, 0.263],
        ["Brandon", "SS", 4402, 1099, 0.25],
        ["Alex", "LF", 586, 160, 0.273],
        ["Austin", "CF", 569, 147, 0.258],
        ["Kevin", "P", 56, 2, 0.036]]
    
    
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
