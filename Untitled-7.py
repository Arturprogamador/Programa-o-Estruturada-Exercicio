def exercicio7():
    print("\nExercicio 7")
    valor = float(input("Digite o valor: "))
    taxa = float(input("Digite a taxa de juros anual (%): "))
    tempo = float(input("Digite o tempo em anos: "))

    juros = valor * (taxa / 100) * tempo
    total = valor + juros

    print("Juros:", round(juros, 2))
    print("Valor total:", round(total, 2))
