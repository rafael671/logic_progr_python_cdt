###Criando uma lista


##Ivan, # Gustavo, 
# Tarso, Gabriel, 
# Vitor, Fabricio, e Rafael.


#Quais seriam os prints e 
# input para pedir os nomes?

print ("*** Lista de Nomes ***\n")

nomes = input("Digite os nomes separados por vírgula: ").split(", ")

print(nomes)

#nomes = input ("Wolverine, Vampira, Jean Grey, Tempestade, Jubileu, Gambit, Fera, Ciclope e Magneto")

print("\n Quais operações você quer fazer:")
print("1 - Adicionar um nome")
print("2 - Remover um nome")
print("3 - Listar nomes")
print("4 - Sair")

while True:
    opcao = int(input("\nDigite a opção desejada (1-4): "))
    if opcao == "1":
        print(f" foi adicionado à lista.")

        elif opcao == "2":
print(f" foi removido da lista.")

elif opcao == "3":
print(f"Lista de Nomes:")

