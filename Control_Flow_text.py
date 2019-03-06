# Python language basics 4
# control flow
# if statements

is_game_over = False
p_0_x_pos = 1
e_0_x_pos = 3
e_1_x_pos = 5
 
p_0_x_pos += 2    # p_0_x_pos = 2
if p_0_x_pos == e_0_x_pos:  # = False so skip code below
    is_game_over = True
elif p_0_x_pos == e_1_x_pos:  # = False so skip code below
    is_game_over = True
else:   # Carried out if all above tests fail so execute code below
    e_0_x_pos += 1
    e_1_x_pos += 1

# Only one of the two tests has to pass to execute the code
if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
    is_game_over = True
else: 
    e_0_x_pos += 1
    e_1_x_pos += 1
