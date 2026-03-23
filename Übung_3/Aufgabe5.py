D = int(input("Tag: "))
M = int(input("Monat: "))

tage_pro_monat = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if M < 1 or M > 12:
    print("Kein sinnvolles Datum")
elif D < 1 or D > tage_pro_monat[M - 1]:
    print("Kein sinnvolles Datum")
else:
    print("Sinnvolles Datum")