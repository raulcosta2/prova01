frutas = ["maçã","banana","cereja","laranja","manga"]
indice = int(input("Digite um indice (0 a 4) para obter a fruta correspondente: "))

if 0 <= indice < len(frutas):
    fruta = frutas[indice]
    print(f"A fruta no indice {indice} é {fruta}.")
else:
    print("Indice fora dos limites da lista.")