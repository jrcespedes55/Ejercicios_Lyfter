print("---- Lista para eliminar Keys ----\n")

list_of_keys = ['access_level', 'age']
employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
    }



for key in (list_of_keys):
    deleted_key = employee.pop(key)
    print(f'Deleted Key was: {key} -> {deleted_key}')


print(employee)

	