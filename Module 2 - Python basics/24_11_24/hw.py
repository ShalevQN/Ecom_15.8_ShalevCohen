oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}


oscar_winners.add("Emma Watson") # a

oscar_winners_copy = oscar_winners.copy() # b
oscar_winners_copy.remove("Meryl Streep")
#print(oscar_winners_copy)
oscar_winners_copy.clear()
#print(oscar_winners_copy)


# set operation dictionary:
set_oper_dict = {"intersection": lambda set1, set2: set1 & set2, "union": lambda set1, set2: set1 | set2,
                 "symmetric_diff": lambda set1, set2: set1 ^ set2, "difference": lambda set1, set2: set1 - set2,
                 "issubset": lambda set1, set2: set1 <= set2}

print("Intersection between titanic actors and dark knight actors: ", set_oper_dict["intersection"](titanic_actors, dark_knight_actors)) # c

print("Intersection between iron man actors and avengers actors: ", set_oper_dict["intersection"](iron_man_actors, avengers_actors)) # d

print("If all elements from 'actor_list' are in 'oscar_winners': ", set_oper_dict["issubset"](actor_list, oscar_winners)) # e

print("If all elements from 'actor_list' are in 'avengers_actors': ", set_oper_dict["issubset"](actor_list, avengers_actors)) # f

print("Deleted with pop(): ", movie_cast.pop()) # g

try:
    movie_cast.remove("Matt Damon") # h
except KeyError:
    #print("Matt Damon was removed from movie_cast at the last question.")
    pass

print("titanic actors that did not win an oscar: ", set_oper_dict["difference"](titanic_actors, oscar_winners)) # i

print("Actors that only played one movie from the dark knight and titanic: ", set_oper_dict["symmetric_diff"](dark_knight_actors, titanic_actors)) # j

oscar_winners.update(["Cate Blanchett", "Daniel Day-Lewis"]) # k
#print(oscar_winners)

print("Union between titanic actors and dark knight actors: ", set_oper_dict["union"](titanic_actors, dark_knight_actors)) # l