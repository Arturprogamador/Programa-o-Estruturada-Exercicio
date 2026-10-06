def exercicio8():
    print("\nExercicio 8")
    peso = float(input("Digite o peso em kg: ").replace(",", "."))
    altura = float(input("Digite a altura em metros: ").replace(",", "."))

    imc = peso / (altura * altura)

    print("IMC:", round(imc, 2))
