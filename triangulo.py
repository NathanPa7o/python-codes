#triangulos
print("Qual é o triângulo2.0?")

sair = False

while sair == False:

	valor1 = float (input("Digite o valor do primeiro lado do triângulo: "))
	valor2 = float (input("Digite o valor do segundo lado do triângulo: "))
	valor3 = float (input("Digite o valor do terceiro lado do triângulo: "))

	if valor1 == valor2 == valor3:
		print("O triângulo é Equilátero")

	elif valor1 != valor2 != valor3:
		print("O triângulo é Escaleno")

	else:
		print("O triângulo é Retângulo")

	teste = input("Deseja continuar (s/n): ")
	if teste == "n":
		sair = True