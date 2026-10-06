def exercicio4():
    print("\nExercicio 4")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = (n1 + n2 + n3) / 3

    print("Media:", round(media, 2))

    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperacao")
    else:
        print("Reprovado")