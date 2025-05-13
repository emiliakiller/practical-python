# One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. Each day thereafter, you go out double the number of bills. How long does it take for the stack of bills to exceed the height of the tower?
# Height of tower (to tip): 442m (527m)
# Dollar bill thickness: 0.11mm = 0.00011m
# assuming additive doubling (ie. adding twice as much to the pile each day):

def main():
    item_height = 0.00011 # in metres
    target_height = 442 # in metres
    current_pile_height = 0
    number_of_days = 0

    while(current_pile_height <= target_height):
        current_pile_height += item_height * pow(2, number_of_days)
        number_of_days += 1

    return number_of_days

print(main())
