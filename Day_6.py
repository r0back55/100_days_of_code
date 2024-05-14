### Section 6 ###
# https://cglearning.udemy.com/course/100-days-of-code/learn/lecture/19115662#overview

# ################## #
#   Reeborg's World  #
# ################## #
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def sequence():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()    
#     turn_left()

# for step in range(6):
#     sequence()



# ############################# #
#   Reeborg's World - Hurdle 3  #
# ############################# #
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()    
#     turn_left()
    
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#          move()




# ############################# #
#   Reeborg's World - Hurdle 4  #
# ############################# #
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     while wall_on_right() and front_is_clear():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#          move()





# ######################### #
#   Reeborg's World - Maze  #
# ######################### #
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
   