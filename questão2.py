
#### Questão 02
###Cálculo do Índice de Massa Corporal (IMC)**  
###Habilidade Cobrada:* Aplicação de fórmulas matemáticas usando entrada de dados e exibição de resultados condicionais.


peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))


imc = peso / (altura ** 2)


print(f"Seu IMC é {imc:.1f}.")


categoria = ""
if imc < 18.5:
    categoria = "abaixo do peso"
elif 18.5 <= imc < 24.9:
    categoria = "com o peso normal"
elif 24.9 <= imc < 29.9:
    categoria = "com sobrepeso"
elif 29.9 <= imc < 34.9:
    categoria = "com obesidade grau I"
elif 34.9 <= imc < 39.9:
    categoria = "com obesidade grau II"
else:
    categoria = "com obesidade grau III"


print(f"Você está {categoria}.")