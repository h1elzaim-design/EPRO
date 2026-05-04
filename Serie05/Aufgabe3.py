"""
Aufgabe 3: Caesar-Verschlüsselung (ROT13)
"""

def encrypt(s):
    """Verschlüsselt einen String aus Großbuchstaben A-Z mit Caesar-13."""
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += ch
    return result


def decrypt(s):
    """Entschlüsselt einen Caesar-13-verschlüsselten String.
    
    Da 13 + 13 = 26, ist die Entschlüsselung identisch
    zur Verschlüsselung (ROT13 ist seine eigene Umkehrung).
    """
    return encrypt(s)


if __name__ == "__main__":
    text = "HALLO"
    enc = encrypt(text)
    dec = decrypt(enc)
    print(f"Original:       {text}")
    print(f"Verschlüsselt:  {enc}")
    print(f"Entschlüsselt:  {dec}")

    # Bonus
    bonus = "ZVPUNRYSRVFPUYUNFTERNGUNVE"
    print(f"\nBonus: {bonus}")
    print(f"  →    {decrypt(bonus)}")
