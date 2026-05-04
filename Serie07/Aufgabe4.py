def move(position, direction, steps): 
    """
    Bewegt eine Position in eine Himmelsrichtung.
    Parameter: 
        position(tuple): aktuelle Position als (x, y)
        direction (str): Himmelsrichtungen.
        steps(int): Anzahl der Schritte
    Return: tuple: neue Position (x, y)
    """
    x, y = position
    if direction == "N":
        y += steps
    elif direction == "S":
        y -= steps
    elif direction == "E":
        x += steps
    elif direction == "W":
        x -= steps
    return (x, y)

print(move((0, 0), "N", 3))

