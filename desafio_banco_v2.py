def main():
  
  MENU = """
  ==========================
  [1] - Depositar
  [2] - Sacar
  [3] - Extrato
  [4] - Cadastrar Cliente
  [5] - Criar Conta
  [6] - Listar Clientes
  [7] - Sair
  ==========================
  
  ==> Escolha uma opção: """

  LIMITE_DE_SAQUES = 3
  VALOR_MAXIMO_SAQUE = 500

  numero_de_saques = 0
  saldo = 500.00
  movimentacao = ""
  
  clientes = {}
  contas = {}
  
  numero_da_conta = 1
  
  
  
  while True:
    opcao = input(MENU)
    
    match opcao:
      case "1":
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor <= 0:
          print("Valor inválido")
          continue
        
        saldo = depositar(saldo, valor)
        movimentacao += f"Depósito de R$ {valor:.2f}\n"
        
      case "2":
        if numero_de_saques >= LIMITE_DE_SAQUES:
          print("Limite de saques atingido")
          continue
        
        valor = float(input("Digite o valor a ser sacado: "))
        
        if valor > VALOR_MAXIMO_SAQUE:
          print("Valor acima do limite permitido")
          continue
        
        if saldo < valor:
          print("Saldo insuficiente")
          continue
        
        saldo = sacar(saldo = saldo, valor = valor)
        
        movimentacao += f"Saque de R$ {valor:.2f}\n"
        numero_de_saques += 1 
        
      case "3":
        if not movimentacao:
          print("Nenhuma movimentação realizada")
          continue
        
        extrato(saldo, movimentacao = movimentacao)
        
      case "4":
        criar_usuario(clientes)
        
      case "5":
        criar_conta(clientes, contas, numero_da_conta)
        numero_da_conta += 1
      case "6":
        if not clientes:
          print("Nenhum cliente cadastrado")
          continue
        
        print(clientes)

      case "7":
        print("Saindo...")
        break
      


 
def depositar(saldo, valor):
  saldo += valor
  print(f"Depósito de R$ {valor:.2f} realizado com sucesso")
  print(f"Saldo: R$ {saldo:.2f}")
  return saldo

def sacar(saldo, valor):
  saldo -= valor
  print(f"Saque de R$ {valor:.2f} realizado com sucesso")
  print(f"Saldo: R$ {saldo:.2f}")
  return saldo

def extrato(saldo, movimentacao):
  print("Movimentação:")
  print(movimentacao)
  print(f"Saldo: R$ {saldo:.2f}")
  
  
  
  
def criar_usuario(clientes):
  cpf = input("Digite o CPF para cadastro (somente números): ")
  
  if cpf in clientes:
    print("Cliente já cadastrado")
    return
  
  if not cpf.isdigit() or len(cpf) != 11:
    print("CPF inválido")
    return
  
  clientes[cpf] = {}
  clientes[cpf]["Nome"] = input("Digite o nome do cliente: ")
  
  nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
  clientes[cpf]["Data de nascimento"] = nascimento

  
  logradouro = input("Digite o nome da rua: ")
  numero = input("Digite o número: ")
  
  if not numero.isdigit():
    print("Número inválido")
    clientes.popitem()
    return
  
  bairro = input("Digite o bairro: ")
  
  if not bairro.isalpha():
    print("Bairro inválido")
    clientes.popitem()
    return
  
  cidade = input("Digite a cidade: ")
  
  if not cidade.isalpha():
    print("Cidade inválida")
    clientes.popitem()
    return
  
  estado = input("Digite a sigla do estado: ")
  
  if not estado.isalpha() or len(estado) != 2:
    print("Estado inválido")
    clientes.popitem()
    return
  
  endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
  
  clientes[cpf]["Endereço"] = endereco
  
  
def criar_conta(clientes, contas, numero_da_conta):
  if not clientes:
    print("Nenhum cliente cadastrado")
    return
  
  cpf = input("Digite o CPF do cliente: ")
  
  if cpf not in clientes:
    print("Cliente não cadastrado")
    return

  contas[numero_da_conta] = {}
  contas[numero_da_conta]["Agência"] = "0001"
  contas[numero_da_conta]["Usuário"] = clientes[cpf]["Nome"]
  print(contas)
  

main()