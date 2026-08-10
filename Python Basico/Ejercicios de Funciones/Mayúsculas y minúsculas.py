print("Mayúsculas y Minúsculas Respectivamente:")

text = "I love Nación Sushi"

def count_case_letters(text):
    uppercase = 0
    lowercase = 0
    
    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
            
    return uppercase, lowercase

print(count_case_letters(text))
