#declaração de Classe
class Gafanhoto:
    def __init__(self): #Método Construtor,self é como se referimos a um objeto,significa ele mesmo
        # Atributos de instância
        self.nome = "" # o nome dele mesmo é igual a ""
        self.idade = 0 # a idade dele mesmo é igual a 0
# self é substituido pelo nome do objeto
    # Métodos de instância
    def aniversario(self):
        self.idade = self.idade +1 # a idade dele mesmo aumenta em um 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

#declaração de Objeto    
g1 = Gafanhoto() # instanciação,criação do objeto
g1.nome = "Maria" # atributo
g1.idade = 16    # atributo
g1.aniversario() # note que por ser método é acompanhado por parenteses diferente dos atributos
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Arthur"
g2.idade = 16
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = "Caio"
g3.idade = 14
print(g3.mensagem())