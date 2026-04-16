from rich import inspect
from classes import Pessoa,Aluno,Professor,Funcionario
def main():
    a1 = Aluno("Arthur",16,"Informática","INFO2V")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    inspect(a1,methods=True)
    p1 = Professor("Léo",38,"Eng.Software","Doutor")
    p1.fazer_aniversario()
    p1.dar_aula()
    inspect(p1)
    f1 = Funcionario("George",16,"Porteiro","Portaria")
    f1.fazer_aniversario()
    f1.bater_ponto()
    inspect(f1)
    # x = Pessoa("Rafaela",17)
    # x.fazer_aniversario() 
    # inspect(x,methods=True)
    a1.estudar()
    p1.estudar()
    f1.estudar()
if __name__ == "__main__":
    main()