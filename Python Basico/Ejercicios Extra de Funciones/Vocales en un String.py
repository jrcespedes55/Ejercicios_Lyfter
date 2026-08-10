print("---- Cuantas vocales contiene un String----\n")

text = "Hola mundo"
text2 = "Abecedario"

def vowels_string(word):
    counter = 0
    for char in word:
        if char == 'A' or char == 'a' or char == 'E' or char == 'e' or char == 'I' or char == 'i' or char == 'O' or char == 'o' or char == 'U' or char == 'u':
            counter += 1
    return counter

vowels = vowels_string(text)
print(f"La palabra '{text}' tiene {vowels} vocales.")