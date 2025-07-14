##MVC
#Model
### organização e estética.

#View
### expressão de resultado.

#Controller
### função de tudo.


def mostrar_menu():
    print("\n---Calculadora---")
    print("1. Adição")
    print("2. Subtração")
    print("5. Sair")
    print("-----------------")

    def obter_numeros():
        while True:
            try:
                numl = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                return numl, num2
            except ValueError:
                print("Entrada inválida. Por favor, " \ 
                      "digite números válidos")