# Erstellen Sie eine Funktion welche eine Liste von Strings liest 
# und dann nach der Anzahl der Zeichen prüft. Kleinste zuerst.

def sorted_words(words): 
    return sorted(words, key=len)

words = ["Apfel", "Banane", "Kiwi", "Drachenfrucht", "Feige"]

print(sorted_words(words))

#BRUUUUUUUUUHHHHH Ich bin dumm !
