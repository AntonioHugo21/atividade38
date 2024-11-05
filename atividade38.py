"""Inicialize uma lista de 20 números inteiros. Armazene
os números pares em uma lista PAR e os números
ímpares em uma lista IMPAR. Imprima as listas PAR
e IMPAR."""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

par = []
impar = []

for l in lista:
    if l % 2 == 0:
        par.append(l)
    else:
        impar.append(l)
    
print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')
