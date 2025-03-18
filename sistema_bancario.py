menu = """
-------- Menu --------
/                    /
/   [1] Depositar    /
/   [2] Sacar        /
/   [3] Extrato      /
/   [0] Sair         /
/                    /
----------------------    

=> """

saldo = 0
limite = 500
extrato = ""
num_saq = 0
LIM_SAQ = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\n=================== Depositar ===================")
        valor_dep = int(input("Qual o valor desejado para o deposito? R$  "))
        saldo += valor_dep
        print(f"Deposito de R$ {valor_dep:.2f} realizado com sucesso.")
        extrato += f"Deposito: R$ {valor_dep:.2f}\n"
        print("=================================================")

    elif opcao == "2":
        print("\n=================== Sacar ===================")

        if num_saq >= LIM_SAQ:
            print(f"Limite de {LIM_SAQ} saques diários atingido.")
            
        else: 
            valor_saq = int(input("Qual o valor desejado para saque: R$  "))
        
            if valor_saq > saldo:
                print("Saldo insulficiente para esta operaçao.")

            elif valor_saq > limite:
                print(f"O valor do saque excede o limite de R$ {limite:.2f} por operação.")

            else:
                saldo -= valor_saq
                extrato += f"Saque: R$ {valor_saq:.2f}\n"
                num_saq += 1
                print(f"Saque de R$ {valor_saq:.2f} realizado com sucesso.")
                print(f"Saques restantes hoje: {LIM_SAQ - num_saq}")
                print("=============================================")

    elif opcao == "3":
        print("\n============== Extrato ==============")

        if extrato == "":
                print("Não foram realizadas movimentações.")
        else:
                print(extrato)
                print(f"Saldo atual: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opcao Invalida, por favor selecione novamente a operacao desejada.")