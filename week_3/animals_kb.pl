% Facts
animal(lion).
animal(tiger).
animal(elephant).
animal(crocodile).
animal(shark).
animal(parrot).
animal(eagle).
animal(dolphin).
animal(whale).
animal(frog).

mammal(lion).
mammal(tiger).
mammal(elephant).
mammal(dolphin).
mammal(whale).

bird(parrot).
bird(eagle).

reptile(crocodile).
amphibian(frog).
fish(shark).

% Rule
is_mammal(X) :- mammal(X), animal(X).
