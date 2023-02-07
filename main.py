def CalcularIMC(peso,altura):
    return peso/(altura **2)
peso = float(input('Digite seu peso:'))
altura = float(input('Digite altura:'))
print(CalcularIMC(peso,altura))