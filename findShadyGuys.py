filename = 'data'

total_shady_guys_found = 0
current_checking_line = 0

last_station_id = ""
last_station_owner = ""

shadyguy_station_list = []


with open(filename, 'r') as file:
    for line in file:
        current_checking_line += 1
        
        # Check if the string '<component class="statio' is in the line 
        if '<component class="statio' in line:
            # In this line, find the characters after code=" up until the next "
            last_station_id = line[line.find('code="') + 6:line.find('"', line.find('code="') + 6)]

            # In this line, find the characters after owner=" up until the next "
            last_station_owner = line[line.find('owner="') + 7:line.find('"', line.find('owner="') + 7)]

        # Check if the string 'shady' is in the line
        if '<post id="shadyguy" component="[' in line:
            print('Found shady guy on line', current_checking_line)
            total_shady_guys_found += 1
            shadyguy_station_list.append([last_station_id,last_station_owner, current_checking_line])


print('Total shady guys found:', total_shady_guys_found)

# Sort the list of shady guys alphabetically by station owner (second element in the list)
shadyguy_station_list.sort(key=lambda x: x[1])

# Print the list of shady guys
print('\nList of shady guys:')
for i in range(len(shadyguy_station_list)):
    print(shadyguy_station_list[i])