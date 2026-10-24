

tarefas = []

while True:
    print("===== GERENCIADOR DE TAREFAS =====")
    print()
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")

    print()

    escolha = int(input("Escolha uma opcao: "))
    print("======================================")
    print()

    if escolha == 1:
        print()
        print("===== ADICIONAR TAREFAS ===== ")
        print()

        tarefas.append(input("Tarefa: "))
        print()
        print("======================================")


    elif escolha == 2:
            if len(tarefas) == 0:
                print("====== NENHUMA TAREFA CADASTRADA! =====")
                print()
            else:
                cont = 0
                print()
                print("===== REMOVER TAREFAS ===== ")
                print()

                for i in tarefas:
                    print(f"{cont} -", i)
                    cont += 1

                print()
                while True:
                    escolha_remover = int(input("Escolha uma opção para Remover:  "))

                    if 0 <= escolha_remover < len(tarefas):
                       print("Tarefa removida =", tarefas[escolha_remover])
                       tarefas.pop(escolha_remover)
                       break
                    else:
                       print("======================================")
                       print()
                       print("Escolha inválida!")
                       print("Selecione novamente")

                    print()
                    print("======================================")



    elif escolha == 3:
        print()
        print("===== LISTA DE TAREFAS =====")
        print()
        for i in tarefas:
            print(f"Tarefa: {i}")
        print()
        print("======================================")


    elif escolha == 4:
        print("======================================")
        print("=========== FIM DO PROGRAMA ==========")
        print("======================================")
        break

    else:
        print("====== ESCOLHA INVALIDA =====")
        print("====== ESCOLHA OUTRO VALOR =====")
        print()
        print("======================================")





