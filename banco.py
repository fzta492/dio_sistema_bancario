import pandas as pd

saldo = 0
contagem_saques = 0  # Máximo 3 saques diários
historico = pd.DataFrame(columns=["Tipo", "Valor"])

def menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    try:
        return int(input(
            """
            ====== Operação ======

            1 - Sacar
            2 - Depositar
            3 - Visualizar Extrato
            4 - Sair

            ======================
            """
        ))
    except ValueError:
        print("Entrada inválida\n")
        return None

def sacar():
    """Realiza a operação de saque."""
    global saldo, contagem_saques
    if contagem_saques >= 3:
        print("Limite de saques diários atingido\n")
        return

    try:
        valor = float(input("Digite o valor para sacar: "))
    except ValueError:
        print("Valor inválido\n")
        return

    if valor <= 0:
        print("O valor do saque deve ser positivo.\n")
        return

    if valor > 500:
        print("Ultrapassou o limite de R$500,00 por saque.\n")
        return

    if valor > saldo:
        print("Saldo insuficiente\n")
    else:
        saldo -= valor
        contagem_saques += 1
        historico.loc[len(historico)] = ["Saque", -valor]
        print(f"Saque de R$ {valor:.2f} realizado com sucesso\n")

def depositar():
    """Realiza a operação de depósito."""
    global saldo
    try:
        valor = float(input("Digite o valor para depositar: "))
    except ValueError:
        print("Valor inválido\n")
        return

    if valor <= 0:
        print("O valor do depósito deve ser positivo.\n")
        return

    saldo += valor
    historico.loc[len(historico)] = ["Depósito", valor]
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso\n")
    print(f"Saldo atual: R$ {saldo:.2f}\n")

def visualizar_extrato():
    """Exibe o extrato bancário."""
    print("\n=========== Extrato Bancário ============")
    print(f"Saldo atual: R$ {saldo:.2f}\n")
    if not historico.empty:
        print(historico)
    else:
        print("Não houve movimentações.\n")
    print("=======================================\n")

def executar():
    """Função principal para executar o programa."""
    while True:
        opcao = menu()
        if opcao is None:
            continue
        elif opcao == 1:
            sacar()
        elif opcao == 2:
            depositar()
        elif opcao == 3:
            visualizar_extrato()
        elif opcao == 4:
            print("Saindo do sistema...\n")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções do menu.\n")

executar()
