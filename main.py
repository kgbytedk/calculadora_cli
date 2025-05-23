import os

def console_clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        print("Erro: divisão por zero não é permitida.")
        return None
    return x / y

def executaroperaçao(opçao):
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: por favor, digite apenas números válidos.")
        return

    if opçao == 1:
        total = add(num1, num2)
        print(f"Resultado: {num1} + {num2} = {total}")
    elif opçao == 2:
        total = sub(num1, num2)
        print(f"Resultado: {num1} - {num2} = {total}")
    elif opçao == 3:
        total = mult(num1, num2)
        print(f"Resultado: {num1} * {num2} = {total}")
    elif opçao == 4:
        total = div(num1, num2)
        print(f"Resultado: {num1} / {num2} = {total}")
    elif opçao == 5:
        return main()


def main():
    while(True):
        print("""
        ==============================
             CALCULADORA SIMPLES
        ==============================

        Escolha a operação:
        1 - Adição
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        5 - Sair
        """)

        try:
            input_user = int(input("Digite a opção: "))
            if input_user == 5:
                exit()
            executaroperaçao(input_user)
            input_user = str(input("Deseja fazer outra operação? (s/n): "))
            if input_user.lower != "s":
                console_clear()
                continue
            else:
                break
        except ValueError:
            print("Erro: por favor, digite apenas números válidos.")
            break


if __name__ == "__main__":
    main()
