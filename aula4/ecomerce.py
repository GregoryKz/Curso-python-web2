
class Produto:
    """
    Classe que representa um produto disponível para compra.
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CadastroProdutos:
    """
    Classe responsável por cadastrar e listar os produtos.
    """
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, nome, preco):
        produto = Produto(nome, preco)
        self.produtos.append(produto)
        print("Produto cadastrado com sucesso.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        print("\nPRODUTOS DISPONÍVEIS")
        for i, produto in enumerate(self.produtos):
            print(f"{i + 1} - {produto.nome} | R$ {produto.preco:.2f}")

    def obter_produto(self, indice):
        if 0 <= indice < len(self.produtos):
            return self.produtos[indice]
        return None


class ListaCompras:
    """
    Classe responsável pela lista de compras do cliente.
    """
    def __init__(self, limite):
        self.itens = []
        self.limite = limite

    def adicionar_item(self, produto):
        self.itens.append(produto)
        print(f"{produto.nome} adicionado à lista de compras.")

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def verificar_limite(self):
        if self.calcular_total() > self.limite:
            print("Atenção: limite de gastos ultrapassado.")
        else:
            print("Total dentro do limite.")

    def mostrar_relatorio(self):
        print("\nRELATÓRIO DE COMPRAS")

        if not self.itens:
            print("Nenhum item comprado.")
            return

        for item in self.itens:
            print(f"{item.nome} - R$ {item.preco:.2f}")

        print(f"\nTotal gasto: R$ {self.calcular_total():.2f}")
        print(f"Limite: R$ {self.limite:.2f}")
        self.verificar_limite()


# MENU DO ADMINISTRADOR
def menu_admin(cadastro):
    while True:
        print("\nMENU ADMINISTRADOR")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$ "))
            cadastro.cadastrar_produto(nome, preco)

        elif opcao == "2":
            cadastro.listar_produtos()

        elif opcao == "3":
            print("Saindo do menu administrador.")
            break

        else:
            print("Opção inválida.")


# MENU DO CLIENTE
def menu_cliente(cadastro):
    limite = float(input("Informe o limite de gastos: R$ "))
    lista = ListaCompras(limite)

    while True:
        print("\nMENU CLIENTE")
        print("1 - Comprar produto")
        print("2 - Ver relatório")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro.listar_produtos()

            if not cadastro.produtos:
                continue

            escolha = int(input("Digite o número do produto: ")) - 1
            produto = cadastro.obter_produto(escolha)

            if produto:
                lista.adicionar_item(produto)
            else:
                print("Produto inválido.")

        elif opcao == "2":
            lista.mostrar_relatorio()

        elif opcao == "3":
            print("Saindo do menu cliente.")
            break

        else:
            print("Opção inválida.")


# FUNÇÃO PRINCIPAL COM LOGIN
def main():
    cadastro = CadastroProdutos()

    # Adicionar produtos padrão de auto peças
    cadastro.cadastrar_produto("Óleo de Motor", 50.00)
    cadastro.cadastrar_produto("Filtro de Ar", 30.00)
    cadastro.cadastrar_produto("Velas de Ignição", 20.00)
    cadastro.cadastrar_produto("Pastilhas de Freio", 80.00)
    cadastro.cadastrar_produto("Bateria de Carro", 150.00)

    print("SISTEMA DE COMPRAS")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "admin123":
        print("Login de administrador realizado.")
        menu_admin(cadastro)
    else:
        print("Login de cliente realizado.")
        menu_cliente(cadastro)


# EXECUÇÃO DO PROGRAMA
main()