# num : int = int(input("Number: "))
                         #append # for                  #if
# list_num_comp: list[int] = [i for i in range(1, 20 +1) if i != num]
# print(list_num_comp)


# list_ran_comp: list[int] = [i for i in range(-50, 50 + 1)]
# list_ran_comp_even: list[int] = [i for i in list_ran_comp if i % 2 == 0]
# list_ran_comp_positive: list[int] = [i for i in list_ran_comp if i > 0]
# print(list_ran_comp_positive)

float_number: float = 0

while not 1.4 < float_number < 3.0:
    try:
        float_number = float(input("Enter a float height: "))
    except:
        print("Incorrect height")