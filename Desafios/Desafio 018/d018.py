class Churrasco:
    def __init__(self, titulo, pessoas, consumo_por_pessoa=0.4, preco_kg=82.40):
        self.titulo = titulo
        self.pessoas = pessoas
        self.consumo_por_pessoa = consumo_por_pessoa
        self.preco_kg = preco_kg
    def analisar(self,totalcusto=0,preco = 0):
        print(f"Analisando {self.titulo} com {self.pessoas} convidados")
        print(f"Cada participante comerá 0.4kg e cada kg custa R$82.40")
        print(f"Recomendo comprar {(self.pessoas *self.consumo_por_pessoa):.3f}KG")
        custo = (self.pessoas * self.consumo_por_pessoa) * 82.40
        print(f"o Custo total será de R${custo:.2f}")
        preco = custo/self.pessoas
        print(f"cada pessoa pagará R${preco:.2f} para participar")
c1 = Churrasco("Churras dos Amigos",15)
c1.analisar()