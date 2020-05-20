
print("Calculadora - 2.0")

sair = False

while sair == False:

	valor1 = float (input("Digite o primeiro número: "))
	operador = input("Digite a operação: ")
	valor2 = float (input("Digite o segundo número: "))

	if operador == "+":
		resultado = valor1 + valor2
	if operador == "-":
		resultado = valor1 - valor2
	if operador == "*":
		resultado = valor1 * valor2
	if (valor2 != 0):
		if operador == "/":
			resultado = valor1 / valor2
	else:
		resultado = 0
	if operador == "**":
		resultado = valor1 ** valor2
	if operador == "%":
		resultado = valor1 % valor2

	print("resultado: ")
	print(resultado)
	if (resultado % 2) == 0:
		print("É par")
	else:
		print("É ímpar")

	teste = input("Deseja continuar (s/n): ")
	if teste == "n":
		sair = True