# Inicialização da variável de controle do primeiro loop 
is_running = True
# Inicialização da variável de controle do segundo loop aninhado
is_continuing = True
# Inicialização do dicionário que receberá os livros e suas informações
estoque_acervo={}
# Inicialização do array com o histórico de empréstimos
historico_emprestimos=[]
# Funções de manipulação de livros
def cadastrar():
    # Possibilita a utilização da variável global "is_running" localmente, ou seja dentro da função
    global is_running
    # Variáveis que recebem os inputs do usuário 
    nome_item = str(input("\nDigite o nome do livro: ").lower())
    if nome_item in estoque_acervo:
        print(f"\nO produto {nome_item} já existe. Acesse o menu para atualizar")
        print('\nDeseja realizar outra consulta?')
        print('\n1 - Sim | 2 - Não')
        opcao=str(input("Digite sua opção:"))
        if opcao not in ["1","2"]:
            print("Digite um opção válida")
        elif opcao == '1':
            return
        else:
            if opcao == '2':
                print("\nObrigado por utilizar o programa!")
                print("\nFim do programa")
                is_running=False
    else:
        autor_livro=str(input("\nDigite o autor do livro: "))
        quantidade_item=int(input("\nDigite a quantidade do livro: "))

        # Adiciona o produto utilizando o nome como chave e seu valor com um dicionário aninhado
        estoque_acervo[nome_item] = {
            "autor": autor_livro,
            "quantidade": quantidade_item,
        }
        print(f"\nItem '{nome_item} | {autor_livro} | {quantidade_item} exemplar(es)' adicionado com sucesso!")
        print('\nDeseja realizar outra consulta?')
        print('\n1 - Sim | 2 - Não')
        opcao=str(input("Digite sua opção:"))
        if opcao not in ["1","2"]:
            print("Digite um opção válida")
        else:
            if opcao == '2':
                print("\nObrigado por utilizar o programa!")
                print("\nFim do programa")
                is_running=False

# Função que será chamada caso usuário deseje listar um produto
def listar():
    global is_running
    if len(estoque_de_produtos) == 0:
            print("Nenhum produto ainda foi cadastrado. Retorne ao menu para começar a adicionar.")
            print('Deseja realizar outra consulta?')
            print('\n1 - Sim | 2 - Não')
            opcao = str(input("Digite sua opção:"))
            if opcao not in ["1","2"]:
                print("Digite um opção válida")
            elif opcao == '2':
                print("\nObrigado por utilizar o programa!")
                print("\nFim do programa")
                is_running = False
            else:
                return  # Retorna ao menu se escolher '1'
    else:
        # Uso obrigatório de função "lambda" para ordenar os produtos do estoque
        ordenar_estoque=lambda estoque: sorted(estoque.items())
        # Aplica a função no estoque desordenado
        estoque_ordenado=ordenar_estoque(estoque_de_produtos)
        # Percorre o dicionário ordenado
        for produto,dados in estoque_ordenado:
            # Variável que recebe o valor da chave "quantidade"
            quantidade = dados["quantidade"]
            # Variável que recebe o valor da chave "preco"
            preco = dados["preco"]
            # Mostra em tela toda a lista de produtos
            print(f"Produto: {produto} | Quantidade: {quantidade} | Preço: R$ {preco:.2f}")
        print('Deseja realizar outra consulta?')
        print('\n1 - Sim | 2 - Não')
        opcao=str(input("Digite sua opção:"))
        if opcao not in ["1","2"]:
            print("Digite um opção válida")
        else:
            if opcao == '2':
                print("\nObrigado por utilizar o programa!")
                print("\nFim do programa")
                is_running=False

# Função que será chamada caso usuário deseje remover um produto
def remover():
    global is_running
    if len(estoque_de_produtos) == 0:
        print("Nenhum produto ainda foi cadastrado. Retorne ao menu para começar a adicionar.")
        print('Deseja realizar outra consulta?')
        print('\n1 - Sim | 2 - Não')
        opcao = str(input("Digite sua opção:"))
        if opcao not in ["1","2"]:
            print("Digite um opção válida")
        elif opcao == '2':
            print("\nObrigado por utilizar o programa!")
            print("\nFim do programa")
            is_running = False
        else:
            return  # Retorna ao menu se escolher '1'
    else:
        nome_item_deletar = str(input("\nDigite o nome do produto para remover: "))
        # Verifica se a chave (nome do produto) existe no dicionário
        if nome_item_deletar not in estoque_de_produtos:
            print("Produto inexistente. Digite um produto existente.")
            print('Deseja realizar outra consulta?')
            print('\n1 - Sim | 2 - Não')
            opcao=str(input("Digite sua opção:"))
            if opcao not in ["1","2"]:
                print("Digite um opção válida")
            else:
                if opcao == '2':
                    print("\nObrigado por utilizar o programa!")
                    print("\nFim do programa")
                    is_running=False
        else:
            print(f"Tem certeza que deseja excluir {nome_item_deletar}?")
            print('\n1 - Sim | 2 - Não')
            opcao=str(input("\nDigite sua opção:"))
            if opcao not in ["1","2"]:
                print("Digite um opção válida")
            elif opcao == '1':
                # Deleta a chave e o seu respectivo valor do dicionário
                del estoque_de_produtos[nome_item_deletar]
                print(f"Produto '{nome_item_deletar}' removido com sucesso!")
                print('Deseja realizar outra consulta?')
                print('\n1 - Sim | 2 - Não')
                opcao=str(input("Digite sua opção:"))
                if opcao not in ["1","2"]:
                    print("Digite um opção válida")
                else:
                    if opcao == '2':
                        print("\nObrigado por utilizar o programa!")
                        print("\nFim do programa")
                        is_running=False
            else:
                print("\nOperação cancelada")
                print('Deseja realizar outra consulta?')
                print('\n1 - Sim | 2 - Não')
                opcao=str(input("Digite sua opção:"))
                if opcao not in ["1","2"]:
                    print("Digite um opção válida")
                else:
                    if opcao == '2':
                        print("\nObrigado por utilizar o programa!")
                        print("\nFim do programa")
                        is_running=False

# Função que será chamada caso usuário deseje atualizar um produto
def atualizar_quantidade():
    global is_running
    no_product = True
    
    if len(estoque_de_produtos) == 0:
        print("Nenhum produto ainda foi cadastrado. Retorne ao menu para começar a adicionar.")
        print('Deseja realizar outra consulta?')
        print('\n1 - Sim | 2 - Não')
        opcao = str(input("Digite sua opção:"))
        if opcao not in ["1","2"]:
            print("Digite um opção válida")
        elif opcao == '2':
            print("\nObrigado por utilizar o programa!")
            print("\nFim do programa")
            is_running = False
        else:
            return  # Retorna ao menu se escolher '1'
            
    else:
        while(no_product):
            nome_item_atualizar = str(input("\nDigite o nome do produto que será atualizado: ").lower())
            if nome_item_atualizar not in estoque_de_produtos:
                print("\nNão existe o produto no estoque! Digite um nome válido")
                print('Deseja realizar outra consulta?')
                print('\n1 - Sim | 2 - Não')
                opcao = str(input("Digite sua opção:"))
                if opcao not in ["1","2"]:
                    print("Digite um opção válida")
                else:
                    if opcao == '2':
                        print("\nObrigado por utilizar o programa!")
                        print("\nFim do programa")
                        is_running = False
                    elif opcao == '1':
                        return  # <-- ISSO DIZ AO PYTHON: Pare a função aqui e volte para o menu!
            else:
                no_product = False
                continue # Sai do loop while e avança para a atualização de quantidade abaixo

        # O código abaixo só será executado se o produto existir (pois se não existisse, o return acima teria parado a função)
        quantidade_item_atualizada = int(input("\nDigite a quantidade do produto: "))
        # Acessa a chave (nome), a chave (quantidade) e atribui o valor atualizado
        estoque_de_produtos[nome_item_atualizar]["quantidade"] = quantidade_item_atualizada
        print(f"\nA quantidade de {nome_item_atualizar} foi atualizada para {quantidade_item_atualizada}")
        print('Deseja realizar outra consulta?')
        print('\n1 - Sim | 2 - Não')
        opcao = str(input("Digite sua opção:"))
        if opcao not in ["1","2"]:
            print("Digite um opção válida")
        else:
            if opcao == '2':
                print("\nObrigado por utilizar o programa!")
                print("\nFim do programa")
                is_running = False

def registrar_emprestimo():
    pass

def exibir_historico_emprestimo():
    pass

# Laço de repetição "while": executará o código no seu escopo ENQUANTO "is_running" for true
while(is_running):
    # Variável de controle do segundo loop: caso o usuário deseje realizar outra operação, é necessário atribuir novamente o valor da variável "is_continuing", pois, para sair do segundo loop, seu valor foi alterado para "false"
    # is_continuing = True

    opcoes=["Adicionar livro", "Listar livros", "Remover livro", "Atualizar quantidade", "Registrar empréstimo", "Exibir histórico de empréstimos", "Sair"]
    # O "enumerate" retorna sempre uma dupla de valores na ordem fixa (contador, elemento). O "start=1" indica a contagem iniciar no "1"
    menu = [f"{i} - {opcao}" for i, opcao in enumerate(opcoes, start=1)]

    print("\n### Bem-vindo ao Sistema de Gestão de Acervo ###\n")
    print("Escolha a operação:\n")
    # Percorre o array com list comprehension e exibe cada elemento
    for opcao in menu:
        print(opcao)

    # Variável que recebe a escolha do usuário 
    opcao = input("\nDigite o número da operação desejada: ")

# Verifica se a opção escolhida está na lista. Caso NÃO esteja, o loop é reiniciado
    if opcao not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\n### Inválido! Digite uma opção válida ###\n")
        # Faz o loop voltar ao início"
        continue
    elif opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao =='3':
        remover()
    elif opcao == '4':
        atualizar_quantidade()
    elif opcao == '5':
        atualizar_quantidade()
    elif opcao == '6':
        atualizar_quantidade()
    elif opcao == '7':
        print("\nObrigado por utilizar o programa!")
        print("\nFim do programa")
        is_running=False
        
   

