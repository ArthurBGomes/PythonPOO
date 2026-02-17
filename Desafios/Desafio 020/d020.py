class Gamer:
    def __init__(self, nome, nick, jogosfavoritos=None):
        self.nome = nome
        self.nick = nick
        self.favoritos = jogosfavoritos if jogosfavoritos is not None else []

    def addfavoritos(self, jogo):
        self.favoritos.append(jogo)

    def ficha(self):
        jogos_ordenados = sorted(self.favoritos)
        print(f"Nome: {self.nome}")
        print(f"Nick: {self.nick}")
        print(f"Jogos favoritos: {', '.join(jogos_ordenados)}")

g1 = Gamer("Arthur", "Pedok", ["Minecraft", "Valorant"])
g1.addfavoritos("League of Legends")
g1.ficha()
g2 = Gamer("Léo", "LeoGamer")
g2.addfavoritos("GTA V")
g2.addfavoritos("FIFA 22")
g2.ficha()