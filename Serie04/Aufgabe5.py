words = ["Apfel", "Banane", "Kirsche", "Dattel", "Feige", "Traube", "Kiwi", "Mango", "Orange", "Papaya", "Pfirsich", "Zitrone"]
good_chars = list(input("Good chars: "))

print([word for word in words if any(char in word for char in good_chars)]) 



