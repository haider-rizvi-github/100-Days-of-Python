# we use nested lists and dictionaries when we want to store more complex data structures.
# For example, if we want to store information about multiple countries and their capitals, we can use a dictionary of dictionaries.

# in this i can not store the multiple cities in my dictionary, so i will use a nested dictionary to store the cities and their populations.
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a dictionary and a list

travel_log = {
    "Italy": ["Rome", "Milan", "Florence"],
    "France": ["Paris", "Lyon", "Nice"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "Pakistan": ["Karachi", "Lahore", "Islamabad"],
}

# how to get values in a nested dictionary example get the second city in Italy
print(travel_log["Italy"][1])

# Nested list
nested_list = ["a", "b", ["c", "d"]]

print(nested_list[2][1])

# we can also nest dictionary into dictionary

travelling_log = {
    "Italy": {"cities_visited": ["Rome", "Milan", "Florence"], "total_visits": 3},
    "France": {"cities_visited": ["Paris", "Lyon", "Nice"], "total_visits": 3},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Munich"], "total_visits": 3},
    "Pakistan": {
        "cities_visited": ["Karachi", "Lahore", "Islamabad"],
        "total_visits": 3,
    },
}

# how to get the total visits in Italy
print(travelling_log["Italy"]["total_visits"])
print(
    f"In {travelling_log['Italy']['cities_visited'][-1]} i visited {travelling_log['Italy']['total_visits']} times"
)
