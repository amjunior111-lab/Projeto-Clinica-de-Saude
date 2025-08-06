#Declaração de variáveis
escolha = 1
cadastro = 0
idademedia = 0
somaidade = 0
novo = 'novo'
velho = 'velho'
nome=[]
idade=[]
telefone=[]
#Executa o programa até o usuário digitar 5
while True:
    #Se escolha é igual a 5 o programa fechará
    if escolha == 5:
        break
    #Se escolha está entre 1 e 5 o sistema é executado
    if escolha>=1 and escolha<=5:
        print('===Sistema Clínica Vida+===')
        print('1. Cadastrar Paciente')
        print('2. Ver Estatísticas')
        print('3. Buscar Paciente')
        print('4. Listar todos os pacientes')
        print('5. Sair')
        escolha=int(input('Escolha uma opção: '))
        print('Voce escolheu o numero',escolha)
        #Se escolha é igual a 1 o cliente será cadastrado
        if escolha == 1:
            for i in range (1):
                cadastro = cadastro + 1
                nomeentrada=input('Nome do Paciente: ')
                nome.append(nomeentrada)
                idadeentrada=int(input("Idade do paciente (Digite apenas números inteiros): "))
                idade.append(idadeentrada)
                telefoneentrada=int(input('Telefone do Paciente (Digite apenas números inteiros):'))
                telefone.append(telefoneentrada)
                print('Paciente cadastrado com sucesso!')
                enter=input('Tecle enter para continuar')
        if escolha==2:
            i=0

            print(idade[cadastro])
            print('Número de pacientes cadastrados:',cadastro)
            print('Idade média dos pacientes: ', idademedia)
            print('Paciente mais velho: ', velho)
            print('Paciente mais novo: ', novo)
    else:
        print('===Sistema Clínica Vida+===')
        print('1. Cadastrar Paciente')
        print('2. Ver Estatísticas')
        print('3. Buscar Paciente')
        print('4. Listar todos os pacientes')
        print('5. Sair')
        print('Erro! Digite um número válido')
        escolha = int(input('Escolha uma opção: '))


