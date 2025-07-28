# Define o nome do arquivo onde os desejos serão armazenados.
NOME_ARQUIVO = "meus_desejos.txt"
# Inicializa uma lista vazia para armazenar os desejos.
desejos = []

# --- Funções do Aplicativo ---

def carregar_desejos():
    """
    Carrega os desejos do arquivo de texto para a lista 'desejos'.
    Cria o arquivo se ele não existir.
    """
    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                desejos.append(linha.strip()) # Adiciona cada linha como um desejo, removendo espaços e quebras de linha.
        print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}'!\n")
    except FileNotFoundError:
        print("Parece que é a sua primeira vez! Vamos criar sua lista de desejos!\n")
        # Cria o arquivo vazio para uso futuro
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
            pass # Apenas cria o arquivo e não escreve nada ainda
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os desejos: {e}\n")

def salvar_desejos(lista_de_desejos):
    """
    Salva a lista atual de desejos no arquivo de texto.
    """
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
            for desejo in lista_de_desejos:
                arquivo.write(desejo + "\n") # Escreve cada desejo em uma nova linha.
        print("\nSeus desejos foram salvos com sucesso!")
    except Exception as e:
        print(f"\nErro ao salvar os desejos: {e}")

def exibir_desejos():
    """
    Exibe todos os desejos atualmente na lista, numerados.
    """
    if not desejos:
        print("Ainda não há desejos na sua lista. Que tal adicionar um?")
        return False # Indica que a lista está vazia
    print("\n--- Seus Desejos Atuais ---")
    for i, desejo in enumerate(desejos):
        print(f"{i+1} - {desejo}")
    print("----------------------------")
    return True # Indica que a lista não está vazia

# --- Lógica Principal do Programa ---

print("Minha Lista de Desejos para o Futuro\n")

# Carrega os desejos ao iniciar o programa
carregar_desejos()

while True:
    print("\n--- O que você gostaria de fazer? ---")
    print("1 - Adicionar um desejo")
    print("2 - Excluir um desejo")
    print("3 - Salvar e sair")

    opcao = input("Digite sua opção (1, 2 ou 3): ")

    if opcao == "1":
        novo_desejo = input("Qual é o seu novo desejo para o futuro? ")
        if novo_desejo.strip(): # Verifica se o desejo não está vazio após remover espaços
            desejos.append(novo_desejo.strip())
            salvar_desejos(desejos)
        else:
            print("Desejo não pode ser vazio! Tente novamente.")
    elif opcao == "2":
        if exibir_desejos(): # Exibe os desejos e verifica se há algum para excluir
            try:
                indice_para_excluir = int(input("Digite o número do desejo que deseja excluir: ")) - 1
                if 0 <= indice_para_excluir < len(desejos):
                    desejo_removido = desejos.pop(indice_para_excluir)
                    print(f"'{desejo_removido}' foi removido da sua lista.")
                    salvar_desejos(desejos)
                else:
                    print("Número inválido. Por favor, digite um número da lista.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    elif opcao == "3":
        salvar_desejos(desejos) # Garante que os desejos sejam salvos antes de sair
        print("Até a próxima! Continue sonhando alto!")
        break # Sai do loop e encerra o programa
    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")
