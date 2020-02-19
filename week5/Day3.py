import test
#TOGETHERNESS!!!!


class Writer:

    def __init__(self,name,n_books,genre):
        self.name = name
        self.n_books = n_books
        self.genre = genre

    def write(self):
        self.n_books += 1
        print(f"{self.name} wrote a book. Number of books {self.n_books}")
    @staticmethod
    def say_hi():
        print("Hi")


class Philospher(Writer):

    def __init__(self,name,n_books,genre,domain):
        super().__init__(name,n_books,genre)
        self.domain = domain

    def write_nonsense(self):
        self.n_books += 1
        print(f"{self.name} worte this nonsense")

class French:
    def __init__(self, name):
        self.name = name

    def talk_nonsense(self):
        print(f"{self,name}: bla balh bla .....some other nonsense")


class FrenchPhilosopher(Philospher,French):

    def confrence(self):
        print(f"{self.name}: some Post Modern Nonsense")


if __name__== '__main__':
    albert = Writer(name="Albert Camus", n_books = 25, genre = ["Philosophy", "Roman"])
    print(albert.name)
    print(albert.n_books)
    print(albert.write())
    fred = Philospher(name="Fredrich", n_books= 29, genre =["Amoralism", "Uberstuff"],domain= "philisim")
    fred.write()
    print(fred.n_books)
    fred.write_nonsense()
    print(fred.n_books)
    derrida = FrenchPhilosopher(name="Jaques Derrida", n_books= 188, genre=["Postmodernisim"],domain= "philisim")
    print(derrida.name)
    print(derrida.n_books)
    derrida.write()
