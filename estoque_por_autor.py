livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "em_estoque": 4},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "em_estoque": 0},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "em_estoque": 2},
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "em_estoque": 0},
]


def estoque_por_autor(livros):
    store_dict={}
    for i in livros:
        autor=i["autor"]
        if autor in store_dict:
            store_dict[autor]+=i["em_estoque"]
        else:
            store_dict[autor]=i["em_estoque"]
    print(store_dict)

estoque_por_autor(livros)