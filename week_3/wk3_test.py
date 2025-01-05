from pyswip import Prolog

# Initialize Prolog
prolog = Prolog()

# Define Knowledge Base
prolog.assertz("animal(lion)")
prolog.assertz("animal(tiger)")
prolog.assertz("animal(elephant)")
prolog.assertz("animal(crocodile)")
prolog.assertz("animal(shark)")
prolog.assertz("animal(parrot)")
prolog.assertz("animal(eagle)")
prolog.assertz("animal(dolphin)")
prolog.assertz("animal(whale)")
prolog.assertz("animal(frog)")

prolog.assertz("mammal(lion)")
prolog.assertz("mammal(tiger)")
prolog.assertz("mammal(elephant)")
prolog.assertz("mammal(dolphin)")
prolog.assertz("mammal(whale)")

prolog.assertz("bird(parrot)")
prolog.assertz("bird(eagle)")

prolog.assertz("reptile(crocodile)")
prolog.assertz("amphibian(frog)")
prolog.assertz("fish(shark)")

prolog.assertz("is_mammal(X) :- mammal(X), animal(X)")

# Run Queries
print("Query: is_mammal(lion)")
print(list(prolog.query("is_mammal(lion)")))  # Expect: [{}] (True)

print("\nQuery: is_mammal(X)")
print(list(prolog.query("is_mammal(X)")))  # Expect: [{'X': 'lion'}, {'X': 'tiger'}, ...]

print("\nQuery: bird(X)")
print(list(prolog.query("bird(X)")))  # Expect: [{'X': 'parrot'}, {'X': 'eagle'}]
