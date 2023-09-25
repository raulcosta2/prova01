# Questão 10. For loops e While loops.
##Habilidade Cobrada: Utilização de diferentes tipos de loops.
##Projeto: Use um loop for para exibir números de 1 a 5 e um loop while para exibir números de 6 a 10.
##Exemplo:
##Output: 1 2 3 4 5 6 7 8 9 10

print("Usando um loop for:")
for numero in range(1, 6):
    print(numero, end=' ')
    
print("\nUsando um loop while:")
numero = 6
while numero <= 10:
    print(numero, end=' ')
    numero += 1
