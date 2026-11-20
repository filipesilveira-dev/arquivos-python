# Classe Livro com seus atributos e métodos: descreve o livro e calcula o valor em estoque (preço*quantidade)
class Livro:
    def __init__(self, titulo, autor, preco, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.quantidade = quantidade

    def valor_em_estoque(self):
        return self.preco * self.quantidade

# Classe Estoque que não HERDA de Livro, mas faz COMPOSIÇÃO com objetos Livro, pois Estoque não é um tipo de livro ("é um"), e sim contém livros ("tem um").
class Estoque:
    def __init__(self):
        # Crie aqui o atributo self.livros com uma lista vazia
        self.livros = []

    # Método de adicionar um livro: adiciona ao final de self.livros o livro passado como argumento
    def adicionar(self, livro):
        # Coloque o livro no final da lista self.livros
        self.livros.append(livro)
        # Retorna uma lista com os livros
        return self.livros
        
    # Método de calcular o valor total no estoque: utiliza o método de Livro para receber o valor total daquele livro em estoque. Percorre o array self.livros somando o valor em estoque de cada livro e armazendando em total
    def valor_total(self):
        # Some o valor_em_estoque() de cada livro da lista
        total=0
        for livro in self.livros:
            total+=livro.valor_em_estoque()
        # Retorna o valor total em estoque
        return total

# Método que retorna uma lista com os títulos dos livros esgotados: percorre a lista self.livros e verifica o livro.quantidade. Caso seja igual a zero, o título do livro é adicionado à lista esgotados
    def titulos_esgotados(self):
        # Devolva a lista com os títulos dos livros com quantidade igual a 0
        esgotados = []
        for livro in self.livros:
            if livro.quantidade == 0:
                esgotados.append(livro.titulo)
        return esgotados


# Teste a sua classe com outros valores:
# Loja é uma instância de Estoque
loja = Estoque()
# Utiliza o método "adicionar()" de Estoque para adicionar um livro
loja.adicionar(Livro("Dom Casmurro", "Machado de Assis", 29.9, 4))
loja.adicionar(Livro("A Hora da Estrela", "Clarice Lispector", 32.0, 0))
# Mostra o retorno de valor_total(), método de Estoque
print(loja.valor_total())
print(loja.titulos_esgotados())
print(loja.livros)