# One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago. Each day thereafter, you go out double the number of bills. How long does it take for the stack of bills to exceed the height of the tower?
# Height of tower (to tip): 442m (527m)
# Dollar bill thickness: 0.11mm = 0.00011m
# assuming additive doubling (ie. adding twice as much to the pile each day):

def main(additive):
    bill_height = 0.11 * 0.001 # mm converted to metres
    target_height = 442 # in metres
    bill_count = 0
    current_pile_height = 0
    number_of_days = 0

    while(current_pile_height <= target_height):
        if additive:
            bill_count += pow(2, number_of_days)
        else:
            bill_count = pow(2, number_of_days)

        current_pile_height = bill_height * bill_count
        number_of_days += 1
        print(f"Day {number_of_days}: {bill_count} bills, {current_pile_height}m")

    return number_of_days

print(main(False))
