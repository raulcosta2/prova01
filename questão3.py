
### Questão 03
##Manipulação Avançada de Strings e Conversão de Datatypes**  
##Habilidade Cobrada:* Transformar e manipular datatypes, utilizando métodos de strings e outras conversões.


data = input("Digite uma data no formato DD/MM/YYYY: ")
dia, mes, ano = map(int, data.split('/'))
texto = input("Digite um texto: ")
num_caracteres = len(texto)
texto_maiusculo = texto.upper()
lista_palavras = texto.split()
numero_decimal = float(input("Digite um número decimal: "))
numero_string = str(numero_decimal).replace('.', ',')
print(f'Dia: {dia}, Mês: {mes:02d}, Ano: {ano}')
print(f'O texto possui {num_caracteres} caracteres.')
print(f'Texto em maiusculo é: {texto_maiusculo}')
print(f'Lista de palavras: {lista_palavras}')
print(f'O número em formato string com vírgula: "{numero_string}"')