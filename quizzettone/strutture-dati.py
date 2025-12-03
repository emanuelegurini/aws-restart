stringhe: list[str] = ["Pippo"]

stringhe.append("Pluto")

stringhe.append("Minnie")

deleted_values: list[str] = [] 

value_to_check_and_delete: str = "Pluto"

is_value_in_the_list: bool = value_to_check_and_delete in stringhe

if is_value_in_the_list == True:
    index_value_to_delete = stringhe.index(value_to_check_and_delete) 
    deleted_value = stringhe.pop(index_value_to_delete)
    deleted_values.append(deleted_value)
else:
    print(f"{value_to_check_and_delete} non esiste nella lista {stringhe}")

print("*"*30)
print(stringhe)
print(deleted_values)



