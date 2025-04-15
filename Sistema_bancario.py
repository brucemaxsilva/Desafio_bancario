menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Função para realizar depósito
def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
      print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar saque
def sacar (saldo, limite, numero_saques, LIMITE_SAQUES, extrato):
    valor = float(input("informe o valor do saque: "))
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques diários excedidos.")
    elif valor > 0:
        saldo -= valor #atualiza o saldo descontando o valor do saque.
        extrato += f"Saque: R$ {valor:.2f}\n" #Adiciona o saque ao extrato.
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operacão falhou! O valor informado é inválido.")
    return saldo, numero_saques, extrato

# Função para exibir extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}") #Vai exibir o saldo atual.
    print("==========================================")
    

# Loop principal para manter o programa em execução
while True:

    opcao = input(menu)

    # Chama a função de depósito
    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
        
    # Chama a função de saque
    elif opcao == "s":
        saldo, numero_saques, extrato = sacar(saldo, limite, numero_saques, LIMITE_SAQUES, extrato)
    
    # Chama a função de exibir o extrato
    elif opcao == "e":
        exibir_extrato(saldo,extrato)
        
    # Finaliza o programa
    elif opcao == "q":
        print("Obrigado por usar o sistema bancário!")
        break


    # Trata de entradas inválidas    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")