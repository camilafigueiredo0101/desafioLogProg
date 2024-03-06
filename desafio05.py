def inverter_string(string):
    inverted_string = ""
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

# Exemplo de utilização
texto = input("Digite uma string para inverter: ")
string_invertida = inverter_string(texto)
print("String original:", texto)
print("String invertida:", string_invertida)
