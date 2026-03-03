from rich import print
from rich.panel import Panel
class Churrasco:
    consumo_por_pessoa=0.4
    preco_kg=82.40
    def __init__(self, titulo, pessoas,):
        self.titulo = titulo
        self.pessoas = pessoas

    def analisar(self,):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/]"
        conteudo +=f"\nCada participante comerá 0.4kg e cada kg custa R$82.40"
        conteudo += f"\nRecomendo comprar {(self.pessoas *Churrasco.consumo_por_pessoa):.3f}KG"
        custo = (self.pessoas * __class__.consumo_por_pessoa) * 82.40
        conteudo +=f"\nO Custo total será de R${custo:.2f}"
        preco = custo/self.pessoas
        conteudo += f"\nCada pessoa pagará R${preco:.2f} para participar"
        panel = Panel(conteudo,title = self.titulo)
        print(panel)
c1 = Churrasco("Churras dos Amigos",15)
c1.analisar()