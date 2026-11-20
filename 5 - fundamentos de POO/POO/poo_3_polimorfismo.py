# Polimorfismo: dependen diretamente do processo de herança. Por meio dele um método pode ser executado de diferentes formas

# Perceba que não foi utilizado método construtor, pois não existe atrinuto na classe Colaborador
class Colaborador:
    def contratar_novo_colaborador(self):
        pass

# Perceba que as duas classes herdam o método "contratar_novo_colaborador" de Colaborador, mas se comportam de maneira diferente. Trata-se da subclasse Estagiario e da subclasse Diretor (Colaborador é a superclasse)
class Estagiario(Colaborador):
    def contratar_novo_colaborador(self):
        return "3 etapas"

class Diretor(Colaborador):
    def contratar_novo_colaborador(self):
        return "5 etapas"

colaboradores = [Estagiario(), Diretor()]
for colaborador in colaboradores:
    print(colaborador.contratar_novo_colaborador())