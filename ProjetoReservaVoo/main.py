from SistemasDeReservas import *

while True:

    print(f'Crie o aeroporto: ')
    cidade = input('cidade: ')
    capacidade_voos = input('Qual a capacidade de voos? ')
    destino = input('Qual nome do aeroporto? ')
    aeroporto = Aeroporto(cidade, capacidade_voos, destino)
    passageiro = Passageiro()
    operador = Operadores()
    print(f'Sobre o voo: ')
    codigo = int(input('código: '))
    destino = input('destino: ')
    assentos = int(input('quantidade de assentos: '))
    opcao_hora_data = int(input('Você deseja agendar o voo?\n[1] Sim\n[2] Não\n'))
    while opcao_hora_data == 1:
        hora = input('Digite a hora:\nExemplo -> 14:45\n')
        data = input('Digite a data:\nExemplo -> 11/09/2001\n')
        voo = Voo(codigo, destino, aeroporto, assentos, hora, data)
        break
    else:
        voo = Voo(codigo, destino, aeroporto, assentos)

    menu = 0 
    while menu == 0:
        menu = int(input(f'O que você deseja fazer agora?\n[1] Fazer uma reserva\n[2] Cancelar uma reserva\n'))
        
        while menu == 1:                       
            reserva = passageiro.criar_reserva(1, passageiro)
            confirmacao_compra = int(input('Você fez uma reserva, agora deseja fazer o pagamento?\n[1]Confirmar\n[2]Negar\n'))
            if confirmacao_compra == 1:
                passageiro.pagar_reserva(voo, reserva)
                print(f'Reserva concluida, restam {voo.assentos_livres()} assento(s) livre(s)')

            menu = int(input('Deseja fazer outra?\n[1] Sim\n[2] Não\n'))
            if menu == 2:
                menu = 0 

        while menu == 2:
            id_cancelar = int(input("Qual o id que da reserva que você deseja cancelar?\n"))
            operador.cancelar_reserva(voo, id_cancelar)
            print(f'Reserva cancelada, restam {voo.assentos_livres()} assento(s) livre(s)')
            menu = 0