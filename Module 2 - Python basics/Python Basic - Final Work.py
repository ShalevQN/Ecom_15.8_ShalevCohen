# EX 1 V
print('EX 1: ')
for x in range(12, 25):
    print(x, end=" ")
print('')

# EX 2 V
print('EX 2: ')
for x in range(7, 32):
    if x % 2 != 0:
        print(x, end=" ")
print('')

# EX 3 V
print('EX 3: ')
for x in range(10, -21, -1):
    if x % 2 == 0:
        print(x, end=" ")
print('')

# EX 4 V
print('EX 4: ')
for x in range(1, 46):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz", end=" ")
    elif x % 3 == 0:
        print("Fizz", end=" ")
    elif x % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(x, end=" ")
print('')

# EX 5 V
print('EX 5: ')
def sum_up(nums: list[int]):
    sum_return = 0
    if len(nums) > 0:
        for num in nums:
            sum_return += num
    return sum_return
print(sum_up([1,13,22,123,49,34,5,24,57,45]))

# EX 6 V
print('EX 6: ')
students = [
    {"id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 20,
        "country": "USA",
        "city": "New York"},
    {"id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 22,
        "country": "Canada",
        "city": "Toronto"},
    {"id": 3,
        "first_name": "Emily",
        "last_name": "Johnson",
        "age": 19,
        "country": "UK",
        "city": "London"}]
def delete_one_property_from_all_students(student_list: list[dict] , delete_property: "str"): # 1
    for s in student_list:
        if delete_property in s:
            s.pop(delete_property)
    return student_list
delete_one_property_from_all_students(students , "id")

def print_all_students(student_list: list[dict]): # 2
    for s in student_list:
        print(s["first_name"], end=":")
        for student_property in s.items():
            print(f"{student_property[0]}: {student_property[1]}")
#print_all_students(students)
def sort_students_by_age(student_list: list[dict]): # 3
    return sorted(student_list, key=lambda s: s['age'])
print("sorted students by age:", sort_students_by_age(students))

# EX 7 V
print('EX 7: ')
our_pets = [
 {"animal_type": "cat",
 "names": ["Meowzer",
 "Fluffy",
 "Kit-Cat"]},
 {"animal_type": "dog",
 "names": ["Spot",
 "Bowser",
 "Frankie"]}]

def print_animal_type_cat(pet_list_of_dict: list[dict]): # 1
    for pet in pet_list_of_dict:
        if pet["animal_type"] == "cat":
            print(f"animalType: {pet['animal_type']}")
print_animal_type_cat(our_pets)

def print_all_pet_names(pet_list_of_dict: list[dict], pet_chosen): # 2
    for pet in pet_list_of_dict:
        if pet["animal_type"] == pet_chosen:
            print(f"Animal: {pet['animal_type']}")
            print("Names:", ", ".join(pet["names"]))
print_all_pet_names(our_pets,"dog")

def add_name_to_all_types(pet_list_of_dict: list[dict], name_chosen): # 3
    for pet in pet_list_of_dict:
        if not name_chosen in pet["names"]:
            pet["names"].append(name_chosen)
add_name_to_all_types(our_pets, "Spot")
#print(our_pets)

# EX 8 V
print('EX 8: ')
student = {
 'name': 'John',
 'age': 20,
 'hobbies': ['reading', 'games', 'coding'],
}
def print_all_data_of_student(student_dict): # 1
    for item in student_dict.items():
        print(item)
def add_hobby_to_student(student_dict, hobby): # 2
    if not hobby in student_dict["hobbies"]:
        student_dict["hobbies"].append(hobby)
    else:
        print("Already exist.")

add_hobby_to_student(student, "netflix") # input("Enter a hobby: ")
print_all_data_of_student(student) # 3

def remove_hobby_from_student(student_dict, hobby): # 4
    if hobby in student_dict["hobbies"]:
        student_dict["hobbies"].remove(hobby)
    else:
        print("This hobby is not one of the student's hobbies.")
remove_hobby_from_student(student, "reading")
print_all_data_of_student(student) # 5

student["family_name"] = "Smith"
#print_all_data_of_student(student)

# EX 9 V
print('EX 9: ')
matrix =[
 [1, 2],
 [3, 4],
 [5, 6]
]
def print_matrix(matrix_list: list[list[int]]):
    for list_x in matrix_list:
        for num in list_x:
            print(num, end=" ")
print_matrix(matrix) # → Should print: 1 2 3 4 5 6
print('')

# EX 10 V
print('EX 10: ')
matrix =[
 [0,1,1],
 [0,1,0],
 [1,0,0]
]
def zero_count(matrix_list: list[list]):
    count_zero = 0
    for x_list in matrix_list:
        for num in x_list:
            if num == 0:
                count_zero += 1
    return count_zero
print("Zero count in matrix:", zero_count(matrix)) # → Should print: 5

# EX 11 V
print('EX 11: ')
arr = [4,2,34,4,1,12,1,4]
def find_dup(dup_num_list: list[int]):
    duped_num_return_list = []
    for num in set(dup_num_list):
        if dup_num_list.count(num) > 1:
            duped_num_return_list.append(num)
    return duped_num_return_list
print("Duplicates in array:", find_dup(arr)) # Should print: [4, 1]

# EX 12 V
print('EX 12: ')
def return_list_reversed(reversible_list):
    #return reversible_list[::-1]
    reversed_list = []
    for i in range(len(reversible_list)-1, -1, -1):
        reversed_list.append(reversible_list[i])
    return reversed_list
arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
print("Reversed array:", return_list_reversed(arr))

# EX 13 V
print('EX 13: ')
first_array = [4, 6, 7]
second_array = [8, 1, 9]
def adding_in_pairs_of_lists(x_list: list[int], y_list: list[int]):
    result_list = []
    for i in range(len(x_list)):
        result_list.append(x_list[i] + y_list[i])
    return result_list
print("Added pair of list:", adding_in_pairs_of_lists(first_array, second_array))

# EX 14 V
print('EX 14: ')
first_str = "racecar"
second_str = "Java"
def check_palindrome_two_string(str1: str, str2: str):
    return {str1: str1.strip() == str1.strip()[::-1], str2: str2.strip() == str2.strip()[::-1]}
print("Checking Palindrome:", check_palindrome_two_string(first_str, second_str))


# EX 15 V
print('EX 15: ')
counter = 1
while counter < 100:
    print(counter, end=" ")
    counter *= 2
print('')

# EX 16 V
print('EX 16: ')
counter = 900000
while counter > 50:
    print(counter, end= " ")
    counter /= 2
print('')

# EX 17 V
print('EX 17: ')
# from iteration_utilities import duplicates ? :)
def find_dupes_str_from_list(list_of_strings: list[str]):
    string_dup_array, string_seen_array = [], []
    counter_i = len(list_of_strings)
    while counter_i > 0:
        counter_i -= 1
        current_string = list_of_strings[counter_i]
        if current_string in string_seen_array:
            if current_string in string_dup_array:
                continue
            else:
                string_dup_array.append(current_string)
        else:
            string_seen_array.append(current_string)
    return string_dup_array
print(find_dupes_str_from_list(["d", "dog","a", "b", "b", "c", "c", "d", "e", "a","car", "e", "e", "e", "e", "unicorn"]))

# EX 18 V
print('EX 18: ')
names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
def remove_duplicate_in_order_string_from_list(x_list: list[str]):
    string_no_dup_array = []
    counter_i = 0
    while counter_i < len(x_list):
        current_string = x_list[counter_i]
        counter_i += 1
        if not current_string in string_no_dup_array:
            string_no_dup_array.append(current_string)
        else:
            continue
    return string_no_dup_array
print(remove_duplicate_in_order_string_from_list(names))

# EX 19 V
print('EX 19: ')
names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
def remove_duplicate_in_order_string_from_list_and_remove_one_value(x_list: list[str], value):
    string_no_dup_array = []
    counter_i = 0
    while counter_i < len(x_list):
        current_string = x_list[counter_i]
        counter_i += 1
        if current_string == value:
            continue
        if not current_string in string_no_dup_array:
            string_no_dup_array.append(current_string)
        else:
            continue
    return string_no_dup_array
print(remove_duplicate_in_order_string_from_list_and_remove_one_value(names, "Pete"))

# EX 20 V
print('EX 20: ')
array= [True, True, True, False, True, True]
def successive_check(bool_list):
    for i in range(1, len(bool_list)):
        if bool_list[i] == bool_list[i - 1]:
            return i
    return -1
print("Successive Check: ", successive_check(array))

# EX 21 V
def inputting_details() -> list:
    return_list = []
    name = input("Enter you full name: ")
    while not (len(name.split()) == 2 and all(part.isalpha() for part in name.split())):
        print("try again...")
        name = (input("Enter you name: "))
    return_list.append(name)
    while True:
        age = int(input("Enter age: "))
        if 1 <= age <= 120:
            break
        else:
            print("try again...")
    return_list.append(age)
    while True:
        email = input("Enter your Email: ")
        if not "@" in email:
            print("try again...")
        else:
            break
    return_list.append(email)
    return return_list
#print(inputting_details())