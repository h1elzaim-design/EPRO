"""
Aufgabe 5: spring_time mit Listen
"""

def spring_time(animal):
    if animal == "cat":
        return ["cat", "cat"]
    elif animal == "rabbit":
        return ["rabbit"] * 10
    elif animal == "physicist":
        return ["physicist"]
    else:
        return []


# a)
def let_it_be_spring_list(animals_list):
    """Wendet spring_time auf jedes Element an und gibt eine flache Liste zurück."""
    result = []
    for animal in animals_list:
        result.extend(spring_time(animal))
    return result


# b) Mehrfach anwenden
if __name__ == "__main__":
    # a) Beispiel
    test = ["cat", "rabbit", "physicist"]
    print(f"let_it_be_spring_list({test})")
    print(f"  = {let_it_be_spring_list(test)}")
    print()

    # b) Iterationen
    animals_list = ["cat", "rabbit", "physicist"]
    print(f"Start: {len(animals_list)} Tiere")

    for i in range(1, 30):
        animals_list = let_it_be_spring_list(animals_list)
        count = len(animals_list)
        print(f"Iteration {i}: {count} Tiere")
        if count > 10_000_000:
            print("Abbruch – Liste zu groß!")
            break
