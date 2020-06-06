from PySide2 import QtWidgets, QtCore
from movie import get_movies
from movie import Movie
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné club")
        self.setup_ui()
        self.populate_movies()
        self.add_movies()
        self.remove_movie()
        self.setup_connection()
         
    
    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajoutter un filme")
        self.lw_movies = QtWidgets.QListWidget()
        self.btn_removeMovies = QtWidgets.QPushButton("suprimer le(s) film(s)")

        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)
    
    def setup_connection(self):
        self.btn_addMovie.clicked.connect(self.add_movies)
        self.btn_removeMovies.clicked.connect(self.remove_movie)


    def populate_movies(self):
        movies = get_movies()

        for movies in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItemes(lw_item)

    def add_movies(self):
        movie_title = self.le_movieTitle.text()
        if not movie_title:
            return False
        
        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies()
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItems(lw_item)

    def remove_movie(self):
        print("on supprime un film")
 
app = QtWidgets.QApplication([])
win= App()
win.show()
app.exec_()