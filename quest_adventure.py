# import matplotlib.pyplot as plt
import numpy as np

game_name = "Quest Adventure"
#print(f"Welcome to {game_name}")
#name = input("Enter Player Name: ")
name = "MUSC"
print(f"Welcome {name} to {game_name}!")

#The Locations in our Adventure
locations = [
"Park",
"Tunnel",
"Suburubs",
"Ocean"]

#temperatures = [[70.0, 40.0, 85.5],
#                [20,     65,   85],
#                [80,     40,   50]]
#
#np.save("temps.npy", temperatures)
temperatures = np.load("temps.npy")


#lmap = np.array([[0, 1, 1], [2, 2, 2],[3,3,3]])
#np.save("world.npy", lmap)
lmap = np.load("world.npy")

def graph_temps():
    pass
#     plt.title("Temperatures of Quest Adventure")
#     plt.plot(distance_from_start, temperatures, color="r")
#     plt.xlabel("location index")
#     plt.ylabel("Temperature (F)")
#     plt.show()

player_location = [0, 0]

answer = ""

def print_the_stuff_i_want():
    locx = player_location[0]
    locy = player_location[1]
    # print(f"locx:{locx} locy{locy}")
    current_temp = temperatures[locx][locy]
    current_location = locations[lmap[locx][locy]]
    #current_dist = distance_from_start[locx][locy]
    print(f"the temperature is {current_temp}")
    #print(f"You are {current_dist} miles from home")
    local_answer = input(f"You are at {current_location}. which way would you like to go (L/R/U/D)?")
    print(f"you entered {local_answer}")

    return local_answer

def move_player(answer, player_location):
    if "l" in answer.lower():
        print("you want to go left")
        #player_location = player_location + 1
        player_location[0] += 1
    elif "r" in answer.lower():
        print("you want to go right")
        player_location[0] -= 1
    elif "u" in answer.lower():
        print("you want to go up")
        #player_location = player_location + 1
        player_location[1] += 1
    elif "d" in answer.lower():
        print("you want to go down")
        player_location[1] -= 1

    if player_location[0] < 0:
        print("Collision: REDGE")
        player_location[0] = 0

    if player_location[1] < 0:
        print("Collision: DEDGE")
        player_location[1] = 0

    if player_location[0] >= lmap.shape[0]:
        print("Collision: LEDGE")
        player_location[0] = lmap.shape[0] - 1

    if player_location[1] >= lmap.shape[1]:
        print("Collision: UEDGE")
        player_location[1] = lmap.shape[1] - 1

    return player_location

def chill(player_location):
    temperatures[player_location[0]][player_location[1]] = temperatures[player_location[0]][player_location[1]] - 50

while "x" not in answer.lower(): #"l" not in answer.lower() and "r" not in answer.lower():

    answer = print_the_stuff_i_want()

    if "c" in answer.lower():
        chill(player_location)
    elif "v" in answer.lower():
        graph_temps()
    else:
        player_location = move_player(answer, player_location)

print("YOU WIN")

temp_mean = np.mean(temperatures)
print(f"AVG_TEMP: {temp_mean:.1f} F")
std_dev = np.std(temperatures)
print(f"STD_DEV: {std_dev:.1f} F")
