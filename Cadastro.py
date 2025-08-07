#Declaração de variáveis
#Lista pacientes
pacientes = []

#Função início
def inicio():
    print("============================")
    print('===Sistema Clínica Vida+===')
    print('1. Cadastrar Paciente')
    print('2. Ver Estatísticas')
    print('3. Buscar Paciente')
    print('4. Listar todos os pacientes')
    print('5. Sair')
    print("============================")

#Função cadastro
def cadastro():
        print("\n")
        nome = input("Digite o nome do paciente: ")
        while True:
            idade = input("Digite a idade do paciente: ")
            if idade.isdigit():
                idade = int(idade)
                break
            else:
                print("Erro! Digite apenas números inteiros")
        while True:
            telefone = input("Digite o numero do telefone do paciente: ")
            if telefone.isdigit():

                break
            else:
                print("Erro! Digite apenas números inteiros")
        #Dicionário
        paciente = {"nome": nome, "idade": idade, "telefone": telefone}
        #Adiciona paciente a lista
        pacientes.append(paciente)
        print("\n")
        print("Paciente cadastrado com sucesso!")
        enter = input("Tecle enter para continuar")

#Função estatísticas
def estatisticas():
    if len(pacientes) == 0:
        print("\nNão há pacientes cadastrados")
        return
    total = len(pacientes)
    soma_idades = 0
    novo = pacientes[0]
    velho = pacientes[0]
    for p in pacientes:
        soma_idades = soma_idades + p["idade"]
        if p["idade"] < novo["idade"]:
            novo = p
        if p["idade"] > velho["idade"]:
            velho = p
    media=soma_idades/total
    print("\n====================Estatisticas====================")
    print("Total de pacientes: ", total)
    print("Idade média: ", media)
    print("Paciente mais novo: ", novo["nome"], novo["idade"]," anos")
    print("Pacienta mais velho: ", velho["nome"], velho["idade"]," anos")
    print("======================================================")
    enter = input("Tecle enter para continuar")

#Função buscar
def buscar():
    nome_busca = input("\nDigite o nome do paciente: ").lower()
    encontrado = False
    for p in pacientes:
        if p["nome"].lower() == nome_busca:
            print("\n====================Paciente encontrado====================")
            print("Nome", p["nome"], "Idade", p["idade"], "Telefone", p["telefone"] )
            print("===========================================================")
            encontrado = True
            break
    if not encontrado:
        print("Paciente não encontrado")
    enter = input("Tecle enter para continuar")

#Função lista
def listapacientes():
    print("\n")
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado")

    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. Nome: {p['nome']}, Idade: {p['idade']}, Telefone {p['telefone']}")
    enter = input("Tecle enter para continuar")

#Programa principal
while True:
    inicio()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        cadastro()
    elif escolha == "2":
        estatisticas()
    elif escolha == "3":
        buscar()
    elif escolha == "4":
        listapacientes()
    elif escolha == "5":
        break
    else:
        print("Opção invalida")




