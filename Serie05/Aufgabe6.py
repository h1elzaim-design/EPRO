"""
Aufgabe 6: spring_time mit Dictionaries
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
def let_it_be_spring_dict(animals_dict):
    """Aktualisiert die Anzahlen im Dictionary gemäß spring_time."""
    new_dict = {}
    for animal, count in animals_dict.items():
        factor = len(spring_time(animal))  # Vermehrungsfaktor aus spring_time
        if factor > 0:
            new_dict[animal] = count * factor
        # factor == 0 → Tier verschwindet
    return new_dict


# b) Mehrfach anwenden
if __name__ == "__main__":
    # a) Beispiel
    test_dict = {"cat": 2, "rabbit": 2, "physicist": 2}
    print(f"let_it_be_spring_dict({test_dict})")
    print(f"  = {let_it_be_spring_dict(test_dict)}")
    print()

    # b) Iterationen
    animals_dict = {"cat": 1, "rabbit": 1, "physicist": 1}
    print(f"Start: {animals_dict}  –  Gesamt: {sum(animals_dict.values())}")

    for i in range(1, 200):
        animals_dict = let_it_be_spring_dict(animals_dict)
        total = sum(animals_dict.values())
        print(f"Iteration {i}: {animals_dict}  –  Gesamt: {total}")
        if total > 10**50:
            print("Abbruch – Zahlen sehr groß (aber kein Speicherproblem!)")
            break
