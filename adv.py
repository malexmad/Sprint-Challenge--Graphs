from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# # map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

print(len(room_graph))

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

#######################################################################################################################
# Fill this out with directions to walk
traversal_path = []
visited = {}
bs = []
retrace = {"n":"s", "s":"n", "w":"e", "e":"w"}
pp = []
o_path = [[]]
short_path = [i for i in range(0,1100)]

# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and
# logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end
# (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

# add the starting room with all possible exits
visited[0]=player.current_room.get_exits()

# while loop until all room is explored
while len(visited) != len(room_graph)-1:

    # if player current room has not benn visited, add all exits except for the direction it came from
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()
        visited[player.current_room.id].remove(bs[-1])

    # while current room has no more room to explore retrace step from popping direction from bs list, add to path
    while len(visited[player.current_room.id]) == 0:
        # get the last direction(reverse) in the backstep list
        # print(player.current_room.id, bs)
        rs = bs.pop()
        player.travel(rs)
        traversal_path.append(rs)
        # print(player.current_room.id)

    # explore available room , add to path
    not_explored = visited[player.current_room.id].pop(random.randint(-1, 0))
    player.travel(not_explored)
    traversal_path.append(not_explored)
    # print(player.current_room.id)
    # add reverse step in list
    bs.append(retrace[not_explored])


# i_room = 0
#
# s = Stack()
#
# s.push((player.current_room, []))
#
# while s.size() > 0:
#
#     room, path = s.pop()
#
#     if room.id not in visited:
#
#         o_path.append(path)
#         visited[room.id] = set()
#
#         if len(path) <= len(o_path[-2]):
#             print(room.id, o_path[-2])
#             for i in o_path[-2]:
#                 if player.current_room.get_room_in_direction(i).id in [num for num in range(0,500)]:
#                     bs.append(i)
#                     visited[player.current_room.id].add(player.current_room.get_room_in_direction(i).id)
#                     player.travel(i)
#
#             # print(player.current_room)
#             for x in player.current_room.get_exits():
#                 if player.current_room.get_room_in_direction(x).id == 0 and len(player.current_room.get_exits()) < 3:
#                     print("no",x)
#                     bs.append(x)
#                     visited[player.current_room.id].add(player.current_room.get_room_in_direction(x).id)
#                     player.travel(x)
#
#
#             if player.current_room.id != i_room:
#                 i = len(o_path[-2]) - 1
#                 while i >= 0:
#
#                     if player.current_room.get_room_in_direction(retrace[o_path[-2][i]]).id  not in visited[player.current_room.id]:
#                         visited[player.current_room.id].add(player.current_room.get_room_in_direction(retrace[o_path[-2][i]]).id)
#                         bs.append(retrace[o_path[-2][i]])
#                         player.travel(retrace[o_path[-2][i]])
#                         i -= 1
#                     else:
#                         i -= 1
#
#         for room_exit in room.get_exits():
#
#             n_path = path.copy()
#             n_path.append(room_exit)
#             s.push((room.get_room_in_direction(room_exit), n_path))
#
#
# for i in o_path[-1]:
#     bs.append(i)
# traversal_path = bs
#
#
# print("bs",len(bs), bs)
# print("ddd",o_path)


#                                        #
#      017       002       014           #
#       |         |         |            #
#       |         |         |            #
#      016--015--001--012--013           #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#       |         |                      #
#       |         |                      # 24
#      009       005                     #
#       |         |                      #
#       |         |                      #
#      010--011--006                     #
#                                        #

# traversal_path = bs
# print(visited)

print(player.current_room.get_exits())
print(len(room_graph),"-----",len(traversal_path), traversal_path)
print("visited",visited)
#######################################################################################################################
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
