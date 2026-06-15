import matplotlib.pyplot as plt
with open('/home/hani/Desktop/EPRO/Serie11/data.txt', 'r') as f:
    text = f.read()
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

plt.bar(sorted_freq.keys(), sorted_freq.values())



plt.xlabel('Zeichen')
plt.ylabel('Häufigkeit')
plt.title('Zeichenhäufigkeit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(freq)