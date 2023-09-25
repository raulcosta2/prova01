### Questão 05 
##Contagem de Vogais em um Texto
##Habilidade Cobrada: Manipulação de strings e uso de estruturas de controle para contagem.


texto = input("Digite um texto: ")
texto = texto.lower()
contagem_a = 0
contagem_e = 0
contagem_i = 0
contagem_o = 0
contagem_u = 0
for caractere in texto:
    if caractere == 'a':
        contagem_a += 1
    elif caractere == 'e':
        contagem_e += 1
    elif caractere == 'i':
        contagem_i += 1
    elif caractere == 'o':
        contagem_o += 1
    elif caractere == 'u':
        contagem_u += 1

print(f'a: {contagem_a}')
print(f'e: {contagem_e}')
print(f'i: {contagem_i}')
print(f'o: {contagem_o}')
print(f'u: {contagem_u}')