import flet as ft

# Definição das classes
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
            return None

    def cancelar_reserva(self, reserva: Reserva):
        reserva.quarto_reservado.disponivel = True
        reserva.status_reserva = "Cancelada"
        self.reservas.remove(reserva)

    def listar_reservas(self):
        return [
            f"Reserva de {reserva.dono_reserva.nome} - Quarto {reserva.quarto_reservado.numero_quarto}, "
            f"Check-in: {reserva.checkin}, Check-out: {reserva.checkout}, Status: {reserva.status_reserva}"
            for reserva in self.reservas
        ]


# Função principal para gerar a interface
def main(page: ft.Page):
    # Criando o gerenciador e alguns dados fictícios
    gerenciador = GerenciadorDeReservas()

    # Adicionando quartos fictícios
    quarto1 = Quarto(101, "Single", 100)
    quarto2 = Quarto(102, "Double", 150)
    quarto3 = Quarto(103, "Suite", 300)
    gerenciador.adicionar_quarto(quarto1)
    gerenciador.adicionar_quarto(quarto2)
    gerenciador.adicionar_quarto(quarto3)

    # Adicionando clientes fictícios
    cliente1 = Cliente("João", "123456789", "joao@example.com", 1)
    cliente2 = Cliente("Maria", "987654321", "maria@example.com", 2)
    cliente3 = Cliente("Lucas", "291285912", "lucas@example.com", 3)
    gerenciador.clientes.append(cliente1)
    gerenciador.clientes.append(cliente2)
    gerenciador.clientes.append(cliente3)

    # Tela Inicial - Exibe lista de quartos e suas disponibilidades
    def tela_inicial(e):
        page.controls.clear()
        page.add(ft.Text("Tela Inicial - Gerenciador de Reservas", size=30))

        # Lista de quartos disponíveis
        quartos_disponiveis = gerenciador.verificar_disponibilidade()
        for quarto in quartos_disponiveis:
            page.add(ft.Text(str(quarto)))

        page.add(ft.ElevatedButton("Fazer Reserva", on_click=fazer_reserva))
        page.add(ft.ElevatedButton("Consultar Clientes", on_click=consultar_clientes))
        page.add(ft.ElevatedButton("Gerenciar Reservas", on_click=gerenciar_reservas))

    # Tela de Formulário de Reserva
    def fazer_reserva(e):
        page.controls.clear()
        page.add(ft.Text("Formulário de Reserva", size=30))

        # Seleção do cliente
        cliente_input = ft.Dropdown(label="Selecione o Cliente", options=[
            ft.dropdown.Option(cliente.nome) for cliente in gerenciador.clientes
        ])
        
        # Seleção do quarto
        quarto_input = ft.Dropdown(label="Selecione o Quarto", options=[
            ft.dropdown.Option(f"Quarto {quarto.numero_quarto} ({quarto.tipo_quarto})") for quarto in gerenciador.quartos
            if quarto.disponivel
        ])

        # Entradas de datas
        checkin_input = ft.TextField(label="Data de Check-in (yyyy-mm-dd)")
        checkout_input = ft.TextField(label="Data de Check-out (yyyy-mm-dd)")

        def confirmar_reserva(e):
            cliente_nome = cliente_input.value
            quarto_numero = int(quarto_input.value.split()[1])  # Extraindo o número do quarto
            checkin = checkin_input.value
            checkout = checkout_input.value

            cliente = next((c for c in gerenciador.clientes if c.nome == cliente_nome), None)
            quarto = next((q for q in gerenciador.quartos if q.numero_quarto == quarto_numero), None)

            if cliente and quarto:
                reserva = gerenciador.criar_reserva(quarto, cliente, checkin, checkout)
                if reserva:
                    page.add(ft.Text(f"Reserva Confirmada para o Quarto {quarto.numero_quarto}."))
                else:
                    page.add(ft.Text(f"O quarto {quarto.numero_quarto} não está disponível."))
            else:
                page.add(ft.Text("Erro ao criar a reserva."))

        page.add(cliente_input, quarto_input, checkin_input, checkout_input)
        page.add(ft.ElevatedButton("Confirmar Reserva", on_click=confirmar_reserva))
        page.add(ft.ElevatedButton("Voltar", on_click=tela_inicial))

    # Tela para Consultar Clientes
    def consultar_clientes(e):
        page.controls.clear()
        page.add(ft.Text("Gerenciamento de Clientes", size=30))
        
        for cliente in gerenciador.clientes:
            page.add(ft.Text(f"{cliente.nome} - {cliente.telefone} - {cliente.email}"))

        page.add(ft.ElevatedButton("Voltar", on_click=tela_inicial))

    # Tela de Gerenciamento de Reservas
    def gerenciar_reservas(e):
        page.controls.clear()
        page.add(ft.Text("Gerenciamento de Reservas", size=30))

        reservas = gerenciador.listar_reservas()
        for reserva in reservas:
            page.add(ft.Text(reserva))

        def cancelar_reserva(e):
            quarto_numero = int(quarto_cancelar_input.value)
            reserva = next((r for r in gerenciador.reservas if r.quarto_reservado.numero_quarto == quarto_numero), None)
            if reserva:
                gerenciador.cancelar_reserva(reserva)
                page.add(ft.Text(f"Reserva para o quarto {quarto_numero} cancelada."))
            else:
                page.add(ft.Text(f"Erro: Nenhuma reserva encontrada para o quarto {quarto_numero}."))

        quarto_cancelar_input = ft.TextField(label="Número do Quarto para Cancelar")
        page.add(quarto_cancelar_input)
        page.add(ft.ElevatedButton("Cancelar Reserva", on_click=cancelar_reserva))
        page.add(ft.ElevatedButton("Voltar", on_click=tela_inicial))

    # Inicializa a Tela Inicial
    tela_inicial(None)

# Executando a aplicação Flet
ft.app(target=main)
