# the ',' creates a space, and prints in the same line
def create_first_half():
    print "+ - - - -",

def create_middle_half():
    print "|        ",

# for the three support horizontal lines
def create_support_horizontal():
    create_first_half()
    create_first_half()
    print "+"

# for all the other horizontal lines
def create_middle_horizontal():
    create_middle_half()
    create_middle_half()
    print "|"

# to draw the grid
for horizontal in range(11):
    if horizontal == 0:
        create_support_horizontal()
    elif horizontal % 5 == 0:
        create_support_horizontal()
    else:
        create_middle_horizontal()
