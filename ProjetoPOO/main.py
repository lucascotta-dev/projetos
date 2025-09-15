import flet as ft

class Cliente:
    def __init__(self, nome, telefone, email, id):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = id


class Reserva:
    def __init__(self, dono_reserva, quarto_reservado, checkin, checkout, status_reserva):
        self.dono_reserva = dono_reserva
        self.quarto_reservado = quarto_reservado
        self.checkin = checkin
        self.checkout = checkout
        self.status_reserva = status_reserva


class Quarto:
    def __init__(self, numero_quarto, tipo_quarto, preco_diaria):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto  # single, double ou suite
        self.preco_diaria = preco_diaria  # preço por diária
        self.disponivel = True  # Status de disponibilidade: True se disponível e False se indisponível

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Quarto {self.numero_quarto} ({self.tipo_quarto}) - {status}"


class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)  # Adiciona um novo quarto no sistema

    def verificar_disponibilidade(self):
        return [quarto for quarto in self.quartos if quarto.disponivel]

    def criar_reserva(self, quarto: Quarto, cliente: Cliente, checkin, checkout):
        if quarto.disponivel:
            reserva = Reserva(cliente, quarto, checkin, checkout, "Confirmada")
            quarto.disponivel = False
            self.reservas.append(reserva)
            return reserva
        else:
            print(f"O quarto {quarto.numero_quarto} não está disponível.")
            return None

    def cancelar_reserva(self, reserva: Reserva):
        reserva.quarto_reservado.disponivel = True
        reserva.status_reserva = "Cancelada"
        self.reservas.remove(reserva)

    def modificar_reserva(self, reserva: Reserva, novo_checkin, novo_checkout):
        reserva.checkin = novo_checkin
        reserva.checkout = novo_checkout
        reserva.status_reserva = "Modificada"

    def listar_reservas(self):
        for reserva in self.reservas:
            print(f"Reserva de {reserva.dono_reserva.nome} - Quarto {reserva.quarto_reservado.numero_quarto}, "
                  f"Check-in: {reserva.checkin}, Check-out: {reserva.checkout}, Status: {reserva.status_reserva}")

    def listar_clientes(self):
        for cliente in self.clientes:
            print(f"{cliente.nome} - {cliente.email} - {cliente.telefone}")


# Testando o sistema
gerenciador = GerenciadorDeReservas()

# Adicionando quartos
quarto1 = Quarto(101, "Single", 100)
quarto2 = Quarto(102, "Double", 150)
quarto3 = Quarto(103, "Suite", 300)

gerenciador.adicionar_quarto(quarto1)
gerenciador.adicionar_quarto(quarto2)
gerenciador.adicionar_quarto(quarto3)

# Adicionando clientes
cliente1 = Cliente("João", "123456789", "joao@example.com", 1)
cliente2 = Cliente("Maria", "987654321", "maria@example.com", 2)

gerenciador.clientes.append(cliente1)
gerenciador.clientes.append(cliente2)


# Criando reservas
reserva1 = gerenciador.criar_reserva(quarto1, cliente1, "2025-09-16", "2025-09-20")
reserva2 = gerenciador.criar_reserva(quarto2, cliente2, "2025-09-18", "2025-09-22")

# Listando reservas
gerenciador.listar_reservas()

# Cancelando reserva
gerenciador.cancelar_reserva(reserva1)

# Modificando reserva
gerenciador.modificar_reserva(reserva2, "2025-09-19", "2025-09-23")

# Listando reservas após modificações
gerenciador.listar_reservas()
    



    