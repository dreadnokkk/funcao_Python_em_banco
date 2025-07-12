#%%
def menu():
    menu = """\n
    ======== MENU ========
    [d]\tDepositar
    [s]\tSacar
    [nc]\tExtrato
    [lc]\tNova Conta
    [nu]\tListar contas
    [q]\tSair
    """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor: .2f}\n'
        print('\n==== Depósito realizado com êxito ====')
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n@@@ Operação Falhou! Saldo insuficiente. @@@')

    elif excedeu_limite:
        print('\n@@@ Operação falhou! Saque além o limite. @@@')
    
    elif excedeu_saques:
        print('\n@@@ Operação falhou! Número máximo de saques exceido @@@')

    elif valor > 0:
        salo -= valor
        extrato += f'Saque\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Operação realizada com êxito! ===')

    else:
        print('\n@@@ Operação falhou! Valor informado não é válido. @@@')
    
    return saldo, extrato
   
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("  =========================================")

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe uma conta com este CPF! @@@')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço: ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})

    print('==== Usuário criado com êxito! ====')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuarios['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o CPF do usuário ao lado: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n ==== Conta criadda com sucesso! ====')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n@@@ Usuário não encontrado, favor reveja os dados inseridos! @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t\t{conta['usuario']['nome']}
"""
        print('=' * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito desejado: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Digite o valor do saque desejado: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)    

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break        
        
main()
# %%