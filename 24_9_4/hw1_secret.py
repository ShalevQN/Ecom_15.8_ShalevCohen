#Previous question

### Yeah, well I was kind of bored...........................


hw1 = []

def questions_asking(): # Input that needs to be sorted.
    id_input: int = int(input("What is your ID? "))
    first_name_input = input("What is your first name? ")
    last_name_input = input("What is your last name? ")
    age_input: int = int(input("What is your age? "))
    height_input: float = float(input("What is your height? "))
    year_of_birth_input: int = int(input("What year were you born?: "))
    format_sorter(id_input, first_name_input, last_name_input, age_input, height_input, year_of_birth_input)

def format_sorter(id_input, first_name_input, last_name_input, age_input, height_input, year_of_birth_input):
    person = {"id" : str(id_input), "last name" : last_name_input.capitalize(), "first name" : first_name_input.capitalize(), "age": str(age_input), "height" : str(height_input), "year-of-birth" : str(year_of_birth_input)}
    hw1.append(person)
    print_all_library()


# Print the information for each person in the library
def print_all_library():
    print("\nHW1 Library:")
    for person in hw1:
        print("\nID:", person['id'])
        print("\nName:", person['last name'], person["first name"])
        print("\nAge:", person['age'])
        print("\nHeight:", person['height'])
        print("\nYear of birth:", person['year-of-birth'])
        print("\n-------------------------")

while True:
    questions_asking()