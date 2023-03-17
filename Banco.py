menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
operacao = []
transacao = []
extrato = ""

while True:
    opcao = input(menu)
 
    if opcao == "d":# Fazer o deposito
 
        deposito = int(input("Favor digite o valor inteiro que deseja Depositar\n "))
        if deposito <0:# Deposito tem que ser positivo
            print("Valor invalido!\n")
        elif type(deposito) == int:# Deposito tem que ser inteiro
            saldo += deposito
            print(saldo)
        operacao.append(deposito)#Gravador de historico de deposito 
        transacao.append("Deposito")
 
    elif opcao == "s":
 
        if numero_saques < LIMITE_SAQUES:
            saque = (float(input("Favor digite o valor que deseja Sacar\n")))
            if saque <= 500 and saque <= saldo:
                saldo -= saque

            else:
                print("Valor limite invalido, limite de saque é 500\n")
        else:
            print("Limite de saques diarios atingidos!\n")
        numero_saques += 1
        operacao.append(-saque)#Gravador de historico de saque
        transacao.append("Saque")
 
    elif opcao == "e":
        
        for historico_trans,historico in zip(transacao,operacao):#imprimir Historico de trasação e valor
            print(f"{historico_trans} de R$ {historico}")
        #for historico in operacao:# Imprimir a historico
            #print(f"R$ {historico}")
        print(saldo)
    
    elif opcao == "q":

        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada. ")
