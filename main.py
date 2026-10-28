

def mostrar_menu():
    print("===== GERENCIADOR DE TAREFAS =====")
    print()
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Editar tarefa")
    print("5 - Sair")
    print()

def adicionar_tarefa(lista):
    while True:
        print()
        print("===== ADICIONAR TAREFAS ===== ")
        print()

        escolha_usuario = (input("Tarefa: "))


        resultado = cadastrar_tarefa(lista, escolha_usuario)

        if resultado == False: # if not resultado
            print("Valor Digitado Inválido!")
        else:
            print("Tarefa Cadastrada com Sucesso!", escolha_usuario.strip())
            print()
            print("======================================")
            break

def cadastrar_tarefa(lista: list[dict], descricao: str, id: int) -> bool:
    descricao = descricao.strip()

    nova_tarefa = {
        "id": id,
        "descricao": descricao,
        "concluida": False
    }

    if descricao == "":
        return False
    else:
        lista.append(nova_tarefa)
        return True

def remover_tarefa(lista: list[str]) -> None:
    if len(lista) == 0:
        print("====== NENHUMA TAREFA CADASTRADA! =====")
        print()
    else:
        cont = 0
        print()
        print("===== REMOVER TAREFAS ===== ")
        print()

        for i in lista:
            print(f"{cont} -", i)
            cont += 1

        print()

        while True:
            try:
                escolha_remover = int(input("Escolha uma opção para Remover:  "))

                if 0 <= escolha_remover < len(lista):
                    tarefa_removida = lista[escolha_remover]

                resultado = excluir_tarefa(lista, escolha_remover)

                if resultado:
                    print("Tarefa removida =", tarefa_removida)
                    break
                else:
                    print("======================================")
                    print()
                    print("Escolha inválida!")
                    print("Selecione novamente")
                print()
                print("======================================")

            except ValueError:
                print("Valor Incorreto: Digite novamente")
                print()
                print("======================================")
                continue

def excluir_tarefa(lista: list[dict], id: int)-> bool:

    for x in lista:
        if x["id"] == id:
            lista.remove(x)
            return True

    return False

def listar_tarefas(lista: list[dict]):
    print()
    print("===== LISTA DE TAREFAS =====")
    print()
    for i in lista:
        print(f"Tarefa: {i.get('descricao')}")
    print()
    print("======================================")

def editar_tarefa(lista: list[dict], id: int, nova_descricao):

    verificador = nova_descricao.strip()
    if verificador == "":
        return False

    for tarefa in lista:
        if tarefa["id"] == id:
            tarefa["descricao"] = verificador
            return True
    return False





def fim_programa():
    print("======================================")
    print("=========== FIM DO PROGRAMA ==========")
    print("======================================")

def main():
    tarefas = []

    while True:
        mostrar_menu()

        try:
            escolha = int(input("Escolha uma opcao: "))
            print("======================================")
            print()
            if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
                print("====== ESCOLHA INVALIDA =====")
                print("====== ESCOLHA OUTRO VALOR =====")
                print()
                print("======================================")
        except ValueError:
            print("====== ESCOLHA INVALIDA =====")
            print("====== ESCOLHA OUTRO VALOR =====")
            print()
            print("======================================")
            continue

        if escolha == 1:
            adicionar_tarefa(tarefas)

        elif escolha == 2:
            remover_tarefa(tarefas)

        elif escolha == 3:
            listar_tarefas(tarefas)

        elif escolha == 4:
            editar_tarefa(tarefas)

        elif escolha == 5:
            fim_programa()
            break

# -----------------------------------------------------------------

if __name__ == "__main__":
    main()






