print("---- Cinco palabras y palabras de más de 4 letras ----\n")

my_list = []
new_list = []
counter = 1
word = ""

while(counter <= 5):
	word = str(input(f"Digite la palabra #{counter}  \n"))
	counter = counter + 1
	my_list.append(word)

for record in my_list:
	if(len(record) > 4): 
		new_list.append(record)


print(f'Estas son tus palabras: {my_list}\n')
print(f'Esta es una nueva lista con palabras de más de 4 letras: {new_list}\n')
