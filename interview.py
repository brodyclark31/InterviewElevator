# Please provide code that simulates an elevator. 
# The result should be an executable, or script, that can be run with the following inputs. 
# You are free to use any language.  Upload to github for discussion during interview.
# Inputs: <starting floor> [list of floors to visit]  (e.g elevator start=12 floor=2,9 1,32)
# Outputs: <total travel time> [floors visited in order] (e.g 560 12,2,9,1,32)
import sys

# setting varibles for code
# starting_floor = 12
# input = [2, 9, 1, 32]

# reading the test file, checking command line input, and setting variables
try:
    with open(str(sys.argv[1])) as f:
        lines = f.readlines()
    f.close()
except (IndexError, FileNotFoundError):
    print("Invalid input file. Please enter a valid file.")
    sys.exit(0)

line_array = lines[0].split(" ")
starting_floor = int(line_array[0])
input = line_array[1].split(",")
total_travel_time = 0
current_floor = starting_floor

# looping through the floor list and computing the 
for i in input:
    i = int(i)
    # getting the difference between the current floor and the next floor and times 10 for time
    adding = abs(current_floor - i) * 10
    total_travel_time += adding
    # setting current floor to i
    current_floor = i

input.insert(0, str(starting_floor))
result = ','.join(input)

print(total_travel_time, result)