import csv


def read_players(filename):
   lineup = []

   try:
       with open(filename, newline='') as file:
           reader = csv.DictReader(file)
           lineup = [
               {
                   'name': row['Name'],
                   'position': row['Position'],
                   'at_bats': int(row['At Bats']),
                   'hits': int(row['Hits']),
                   'average': float(row['Average'])
               }
               for row in reader
           ]
   except FileNotFoundError:
       print(f"File '{filename}' not found. Creating a new file.")
   except Exception as e:
       print(f"Error reading from '{filename}': {e}")

   return lineup



def write_players(filename, lineup):
   try:
       with open(filename, 'w', newline='') as file:
           fieldnames = ['name', 'position', 'at_bats', 'hits', 'average']
           writer = csv.DictWriter(file, fieldnames=fieldnames)
           writer.writeheader()
           writer.writerows(lineup)
   except Exception as e:
       print(f"Error writing to '{filename}': {e}")


