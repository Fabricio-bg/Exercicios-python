menu = """

Selecione qaul tipo de temperatura eseja utilizar:


Para Celsius digite: { C }.

Para Kelvin digite: { K }.

Para Fahrenheit digite: { F }

"""
print(menu)
tipo = input("Digite aqui o tipo desejado: ")

if tipo == "C":
    valor =float(input("Digite o valor em celsius: "))
    celsius_kelvin = valor + 273
    celsius_fahrenheit = (valor * 9/5) + 32
    print(f"Este valor convertido em kelvin seria de: {celsius_kelvin :.2f}K .\n")
    print(f"Este vaolr convertido em fahrenheit seria de: {celsius_fahrenheit :.2f}F .")
elif tipo == "K":
     valor =float(input("Digite o valor em kelvin: "))
     kelvin_celsius = valor - 273
     kelvin_fahrenheit = (valor * 9/5) - 459
     print(f"Este valor convertido em celsius seria de: {kelvin_celsius :.2f}C .\n")
     print(f"Este vaolr convertido em fahrenheit seria de: {kelvin_fahrenheit :.2f}F .")
elif tipo == "F":
     valor =float(input("Digite o valor em fahrenheit: "))
     fahreinheit_celsius = (valor - 32) * 5/9
     fahreinheit_kelvin = (valor + 459) * 5/9
     print(f"Eset valor cnvertido em celsius seria de: {fahreinheit_celsius:.2f}C .\n")
     print(f"Este valor convertido em kelvin seria de: {fahreinheit_kelvin :.2f}K .")