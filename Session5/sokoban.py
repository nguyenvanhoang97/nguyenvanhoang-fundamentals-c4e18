map_sokoban = {
    "size_x": 5,
    "size_y": 5
}

player = {
    "x":4,
    "y":0
}

boxes = [
    {"x":1 , "y":1},
    {"x":2 , "y":2},
    {"x":3 , "y":3}
]

distinations = [
    {"x":2 , "y":1},
    {"x":3 , "y":2},
    {"x":4 , "y":3}
]
######################### ve map

playing = True
while True:
    for x in range(map_sokoban["size_y"]):
        for y in range(map_sokoban["size_x"]):

            box_is_here = False
            for box in boxes:
                if box["y"] == x and box["x"] == y:
                    box_is_here = True

            dis_is_here = False
            for dis in distinations:
                if dis["y"] == x and dis["x"] == y:
                    dis_is_here = True
            
            player_is_here = False
            if x == player["y"] and y == player["x"]:
                player_is_here = True
            
            if player_is_here == True:
                print("P" , end = "  ")
            elif box_is_here == True:
                print("B" , end = "  ")
            elif dis_is_here == True:
                print("D" , end = "  ")
            else:
                print("-" , end = "  ")
        print()

#check box
    win = True
    for box in boxes:
        if box not in distinations:
            win = False
    if win == True:
        print("you win!!")
        break

    move = input("your move:  ").upper()

    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        break

#     if 0 <= player["x"] + dx < map_soko["size_x"] \
#         and 0 <= player["y"] + dy < map_soko["size_y"]:
#         player["x"] += dx
#         player["y"] += dy
# # move box
#     for box in boxes:
#         if box["x"] == player["x"] and box["y"] == player["y"]:
#             box["x"] += dx
#             box["y"] += dy
    move_on = True
    if 0 <= player["x"] + dx < map_sokoban["size_x"] \
        and  0 <= player["y"] + dy < map_sokoban["size_y"]:

        #box move
        for box in boxes:
                  
            if player["x"] + dx == box["x"] and player["y"] + dy == box["y"]:
                if  0 <= (box["x"] + dx) < map_sokoban["size_x"]\
                and  0 <= (box["y"]) + dy < map_sokoban["size_y"]:
                    move_on = True
                else:
                    move_on = False

                for box2 in boxes:
                    if box["x"] + dx == box2["x"] and box["y"] + dy == box2["y"]:
                        move_on = False

                if move_on == True :
                    box["x"] += dx
                    box["y"] += dy

        if move_on == True:
            player["x"]  += dx
            player["y"] += dy