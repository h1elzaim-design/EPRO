def top3_products(products):
    def netto(p):
        name, cost, taxes = p # Tupel entpacken
        return cost * (1 + taxes / 100) #Netto berechnen

    sortiert = sorted(products, key=netto, reverse=True)
    return sortiert[:3] #Top 3 Produkte zurückgeben

products = [("Laptop", 1000, 19), 
            ("Mouse", 25, 19), 
            ("Keyboard", 75, 19), 
            ("Monitor", 300, 19),
            ("Headphones", 150, 19),
            ("Webcam", 50, 19),
            ("Printer", 200, 19),
            ("Speakers", 100, 19)]

print(top3_products(products))
 