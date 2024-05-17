class Book:
    def __init__(self, title, author, pages, genre, sinopsis,):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.sinopsis = sinopsis
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(
            {
                book.title,
                book.author,
                book.pages,
                book.genre,
                book.sinopsis
            }
        )
    def consult_lib(self):
        return self.books
    def consult_book(self, isbn):
        return self.books[isbn]
    def remove_book(self, isbn):
        self.books.pop[isbn]

if __name__ == "__main__":
    ejecutar = True 
    while ejecutar:
        print(".----BIENVENIDO AL SISTEMA BIBLIOTECARIO----.")
        option = int(input("¿Qué desea realizar? \n 1.Crear biblioteca. \n 2.Agregar libro \n 3.Ver Catálogo. \n 4.Quitar libro. \n 5.Salir."))
        if option == 1:
            name = input("Nombre de la Biblioteca:  ")
            biblioteca = Library(name)
            print(f"Se creó la biblioteca {name}")
        elif option ==2:
            titulo = input("Título:  ")
            autor = input("Autor/a:  ")
            pags = input("Cantidad de Páginas:  ")
            genero = input("Género:  ")
            sin = input("Sinopsis: ")
            libro = Book(titulo, autor, pags, genero, sin)
            biblioteca.add_book(libro)
        elif option ==3:
            print("Catálogo de Libros:  ")
            for i in biblioteca.consult_lib():
                print(i)
        elif option == 4:
            code = input("Ingrese el ID del libro:  ")
            biblioteca.remove_book(code)
        elif option == 5:
            print("Gracias por Visitar!!! ♥☺")
            exit()
        else:
            print("Opción no válida. Intente de nuevo.")