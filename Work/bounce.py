# bounce.py
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program that prints a table showing the height of the first 10 bounces.
# Exercise 1.5

def main(starting_height, retained_height, number_of_bounces):
    count = 0
    current_height = starting_height

    while count < number_of_bounces:
        count += 1
        current_height *= retained_height
        print(f"Bounce {count}: {current_height:.4g}m ")

main(100, 0.6, 10)
