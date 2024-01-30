import matplotlib.pyplot as plt

game_name = "Quest Adventure"
print(f"Welcome to {game_name}")
#name = input("Enter Player Name: ")
name = "Snean"
print(f"Welcome {name} to {game_name}!")

#The Locations in our Adventure
locations = [
"Mills End Park",
"Hwy 26 Tunnel",
"Hillboro Stadium",
"The 7 layers of the gumdrop forest",
"Seaside",
"Hawaii",
"Taiwan",
"Mongolia"]

distance_from_start = [0, 2, 6, 10, 20, 100, 200, 250]

temperatures = [
70.0,
40.0,
85.5,
20,
65,
85,
80,
40]

def graph_temps():
    plt.title("Temperatures of Quest Adventure")
    plt.plot(distance_from_start, temperatures, color="r")
    plt.xlabel("location index")
    plt.ylabel("Temperature (F)")
    plt.show()

player_location = 0

answer = ""

def print_the_stuff_i_want():
    current_temp = temperatures[player_location]
    current_location = locations[player_location]
    current_dist = distance_from_start[player_location]
    print(f"the temperature is {current_temp}")
    print(f"You are {current_dist} miles from home")
    local_answer = input(f"You are at {current_location}. which way would you like to go (L/R)?")
    print(f"you entered {local_answer}")
    return local_answer

def move_player(answer, player_location):
    if "l" in answer.lower():
        print("you want to go left")
        #player_location = player_location + 1
        player_location += 1
    elif "r" in answer.lower():
        print("you want to go right")
        player_location -= 1
    else:
        print("Not Left or Right so i'm confused like MUSC")

    if player_location < 0:
        print("nice try :P")
        player_location = 0

    return player_location

def chill(player_location):
    temperatures[player_location] = temperatures[player_location] - 50


while player_location < len(locations)-1: #"l" not in answer.lower() and "r" not in answer.lower():

    answer = print_the_stuff_i_want()

    if "c" in answer.lower():
        chill(player_location)
    if "v" in answer.lower():
        graph_temps()
    else:
        player_location = move_player(answer, player_location)

print("YOU WIN")
