def exercicio2():
    print("\nExercicio 2")
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))

    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")

    op = int(input("Escolha: "))

    if op == 1:
        print("Resultado:", n1 + n2)
    elif op == 2:
        print("Resultado:", n1 - n2)
    elif op == 3:
        print("Resultado:", n1 * n2)
    elif op == 4:
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Nao pode dividir por zero.")
    else:
        print("Opcao invalida.")