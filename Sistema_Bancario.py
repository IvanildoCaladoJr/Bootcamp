menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

print(menu)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    # com o upper o usuário pode digitar tanto em minúsculo ou maiúsculo que vai funcionar
    # o retorno vai vir sempre maiúsculo
    opcao = input(menu).upper()
    
    if opcao == "Q":
       break
    
    elif opcao == 'D':
       valor = float(input("informe o valor do depósito: "))
       
       if valor > 0:
          saldo += valor
          extrato += f"Depósito: +R$ {valor:.2f}\n"
       else:
          print("Valor informado inválido, informe novamente." )

    elif opcao == 'S':
       valor = float(input("informe o valor do Saque: "))
       
       if numero_saques >= 5: # se superou o limites de 5 saques
          print( "Operação Inválida: Número de saques superou o limite de 5 saques!!")
       elif valor > saldo: # se superou o saldo do momento
          print( "Operação Inválida: Saque maior que o Saldo disponível !!")  
       elif valor > limite: # se superou o limite de R$ 500 para cada saque
          print( "Operação Inválida: Valor do saque maior que o limite de R$ 500 !!")  
       elif valor < 0:
          print("Operação Inválida: Valor negativo, digite novo valor!!" )
       else:
          saldo -= valor
          numero_saques += 1  
          extrato += f"Saque...: -R$ {valor:.2f}\n"    
          print (numero_saques)
    elif opcao == 'E':
       print("\n======= E X T R A T O ========")
       print (extrato)
       print(f"\nSaldo R$ {saldo:.2f}")
    else:
        print (f"Opção {opcao} invalida ,selecione novamete a opção correta:")


        
