menu = """

[a] = Depositar
[b] = Sacar
[c] = Extrato
[d] = Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Digite o valor a ser depositado: "))

        saldo += valor
        extrato += f"Depósito de R$ {valor}\n"
        print("Depósito realizado com sucesso!")
    
    elif opcao == "b":

        valor = float(input("Digite o valor a ser depositado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite


        if numero_saques >=LIMITE_SAQUES:
            print("Limite de saques atingido!")
        elif excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Limite de saque excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")            
        else:
            print("Operação inválida")

    elif opcao == "c":
        print(f"O seu extrato é:{saldo}\n")	

    elif opcao == "d":
        break

    else:
        print("Opção inválida!")
    