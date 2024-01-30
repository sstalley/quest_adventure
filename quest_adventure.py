
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

temperatures = [
70.0,
40.0,
85.5,
20,
65,
85,
80,
40]

player_location = 0

answer = ""

print("The locations are:")
for location in locations:
    pass

while player_location < len(locations)-1: #"l" not in answer.lower() and "r" not in answer.lower():

    current_temp = temperatures[player_location]
    current_location = locations[player_location]
    print(f"the temperature is {current_temp}")
    answer = input(f"You are at {current_location}. which way would you like to go (L/R)?")
    print(f"you entered {answer}")

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

print("YOU WIN")




#if yes then go to show and have a good time

#if not then be bored
