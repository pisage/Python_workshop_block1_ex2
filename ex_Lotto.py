import random
"""
LOTTO game. User picks 6 numbers from 1 to 49 and program checks if they match 6 randomly chooses
:param picked_numbers: numbers chosen by the user
:param hit_counter: how many numbers did the user hit in particular case
"""


drawn_numbers_list = random.sample(range(1, 50), 6)

list_of_picked_numbers = []
print("Choose 6 numbers from 1 to 49:")
try:
    hit_counter = 0
    for i in range(6):
        picked_numbers = int(input())
        if (picked_numbers > 49) or (picked_numbers < 1):
             print("Number ouf of range. Start again choosing numbers from 1 to 49")
             break

        else:
            if picked_numbers in list_of_picked_numbers:
                print("Doubled numbers")
                break
            else:
                list_of_picked_numbers.append(picked_numbers)


    print("Your numbers:", sorted(list_of_picked_numbers))


    for n in range(len(list_of_picked_numbers)):
        if list_of_picked_numbers[n] in drawn_numbers_list:
            hit_counter += 1
            n +=1
        else:
            pass
    print("Drawn numbers:", sorted(drawn_numbers_list))
    if hit_counter > 2:
         print("You hit: ", hit_counter, "numbers. Congratulation!")
    else:
        print("You lost")

except ValueError:
    print("Pick only numbers. Start again")



