# Inicialização da variável de controle do primeiro loop 
is_running = True
# Inicialização da variável de controle do segundo loop aninhado
is_continuing = True

# Laço de repetição "while": executará o código no seu escopo ENQUANTO "is_running" for true
while(is_running):
    # Variável de controle do segundo loop: caso o usuário deseje realizar outra operação, é necessário atribuir novamente o valor da variável "is_continuing", pois, para sair do segundo loop, seu valor foi alterado para "false"
    is_continuing = True
    
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Variável que recebe a escolha do usuário 
    opcao = input("\nDigite o número da operação desejada: ")

# Verifica se a opção escolhida está na lista. Caso NÃO esteja, o loop é reiniciado
    if opcao not in ["1", "2", "3", "4"]:
        print("\n### Inválido! Digite uma opção válida ###")
        # Faz o loop voltar ao início
        continue
 
# Variáveis que recebem os dois números inseridos pelo usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

# O "input" retorna uma string que é comparada nas condicionais
    if opcao == "1":
        print("\nResultado:", num1 + num2)
    elif opcao == "2":
        print("\nResultado:", num1 - num2)
    elif opcao == "3":
        print("\nResultado:", num1 * num2)
    elif opcao == "4":
        if num2 == 0: 
            # Na ocasião de escolha pela divisão, caso o segundo número seja "0", a mensagem de "erro" será exibida
            print("\n### Erro: não existe número dividido por zero ###")
        else:
            print("\nResultado:", num1 / num2)
    
    # Segundo loop dentro do primeiro loop: previne que qualquer valor diferente de "2" funcione como continuação. O usuário precisará digitar um valor válido para continuar ou sair do programa
    while(is_continuing):  
        # Pergunta se o usuário deseja  fazer mais alguma operação
        print("\nDeseja realizar outra operação?")
        print("1 - Sim | 2 - Não")
        
        # Salva a escolha do usuário na variável "continuar"
        continuar = input("\nDigite a opção desejada:")
        
        # Se "continuar" tenha um valor diferente do que está na lista, o segundo loop retorna ao começo
        if continuar not in ["1","2"]:
            print("\n### Inválido! Digite uma opção válida ###")
            # Retorna para o começo do segundo loop
            continue
        
        # Caso digite "1", o programa sai do segundo loop, atribuindo à variável de controle "false", e retorna ao início do primeiro loop
        elif continuar == "1":
            is_continuing = False
            continue
            
        # Se o usuário digitar o "2", os dois loops, e consequentemente o programa, se encerram ao atribuir às duas variáveis de controle o valor "false"
        elif continuar == "2":
            print("\nObrigado por usar a calculadora!")
            is_continuing = False
            is_running = False

