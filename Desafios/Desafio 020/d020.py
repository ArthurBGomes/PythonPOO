from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nick,):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def addfavoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos,key=str.lower)

    def ficha(self):
        conteudo = f"Nome:[black on blue] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for num,game in enumerate(self.favoritos):
            conteudo += f"\n:video_game:[blue]{game}[/]"
        panel = Panel(conteudo,title=f"Jogador: <{self.nick}>")
        print(panel)

g1 = Gamer("Arthur", "Pedok",)
g1.addfavoritos("Minecraft")
g1.addfavoritos("Valorant")
g1.addfavoritos("League of Legends")
g1.ficha()
g2 = Gamer("Léo", "LeoGamer")
g2.addfavoritos("GTA V")
g2.addfavoritos("FIFA 22")
g2.ficha()