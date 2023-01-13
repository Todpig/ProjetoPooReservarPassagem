from datetime import datetime
from abc import abstractmethod


class ManipularReservaMixin():

    @abstractmethod
    def criar_reserva():
        pass
    
    @abstractmethod
    def cancelar_reserva():
        pass


class Reserva():


    def __init__(self, id: int, passageiro):
         self.__id = id
         self.__passageiro = passageiro
         self.__situacao = False


    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, nova_situacao):
        self.__situacao = nova_situacao

    @property
    def passageiro(self):
        return self.__passageiro

    @passageiro.setter
    def passageiro(self, novo_passageiro):
        self.__passageiro = novo_passageiro

    def __str__(self) -> str:
         return f'Reserva concluida com sucesso para o passageiro com Id: {self.passageiro}'



class Operadores(ManipularReservaMixin):

    def criar_reserva(id, passageiro, *args,**kwargs):
        return Reserva(id=id, passageiro=passageiro)

    def cancelar_reserva(self, voo, id_reserva):
       del voo.reservas[id_reserva - 1]

class Passageiro(ManipularReservaMixin):


    def criar_reserva(id, passageiro, *args,**kwargs):
        return Operadores.criar_reserva(id, passageiro)

    def pagar_reserva(self, voo, reserva):
        reserva.situacao = True
        if len(voo.reservas) <= voo.assentos:
            voo.reservas.append(reserva)
        else:
            raise ValueError('Limite atingido.')

    def cancelar_reserva(self, operador, voo, id_reserva):
        operador.cancelar_reserva(voo, id_reserva)


class Aeroporto():
    

    def __init__(self, cidade, capacidade, nome) -> None:
        self.__cidade = cidade
        self.__capacidade = capacidade
        self.__nome = nome
    

    '''Getters e Setters'''

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, nova_cidade):
        self.__capacidade = nova_cidade
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, nova_capacidade):
        self.__capacidade = nova_capacidade
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def __str__(self) -> str:
        return self.nome


class Voo():


    def __init__(self, codigo, destino, aeroporto, assentos,  hora = datetime.time ,data = datetime.today()):
        self.__codigo = codigo
        self.__hora = hora
        self.__data = data
        self.__destino = destino
        self.__aeroporto = aeroporto
        self.__voo_internacional = False
        self.__reservas = []
        self.__assentos = assentos
    
    '''Getters e Setters'''

    @property
    def assentos(self):
        return self.__assentos

    @assentos.setter
    def assentos(self, nova_capacidade):
        self.__assentos = nova_capacidade

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, nova_hora):
        self.__hora = nova_hora
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, novo_destino):
        self.__destino = novo_destino
    
    @property
    def aeroporto(self):
        return self.__aeroporto
    
    @aeroporto.setter
    def aeroporto(self, novo_aeroporto):
        self.__aeroporto = novo_aeroporto

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data: datetime):
        self.__data = nova_data
    
    @property
    def reservas(self):
        return self.__reservas
    
    @reservas.setter
    def reservas(self, nova_reserva):
        pass

    @property
    def voo_internacional(self):
        return self.__voo_internacional
    
    @voo_internacional.setter
    def voo_internacional(self, mudar_voo: bool):
        self.__voo_internacional = mudar_voo


    def __str__(self) -> str:
        return self.reservas

        
    '''Métodos da Classe'''

    def assentos_livres(self):
        assentos_livres = self.assentos - len(self.reservas) 
        return assentos_livres 