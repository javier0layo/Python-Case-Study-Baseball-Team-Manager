import csv


def read_players(filename):
   lineup = []

   try:
       with open(filename, newline='') as file:
           reader = csv.reader(file)
           next(reader)  # Skip the header if present

           lineup = [[name, position, int(at_bats), int(hits), float(average)] for name, position, at_bats, hits, average in reader]
   except FileNotFoundError:
       print(f"File '{filename}' not found. Creating a new file.")
   except Exception as e:
       print(f"Error reading from '{filename}': {e}")

   return lineup



def write_players(filename, lineup):
    header = ["Name", "Position", "At Bats", "Hits", "Average"]

    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(header)

            # Write the player data
            writer.writerows(lineup)
    except Exception as e:
        print(f"Error writing to '{filename}': {e}")
