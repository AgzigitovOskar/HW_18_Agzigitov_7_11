# Импорт  DAO
from dao.movie_dao import MovieDAO
from dao.genre_dao import GenreDAO
from dao.director_dao import DirectorDAO

from service.movie_service import MovieService
from service.genre_service import GenreService
from service.director_service import DirectorService

# импорт базы данных
from setup_db import db


movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)

genre_service = GenreService(genre_dao)
director_service = DirectorService(director_dao)
movie_service = MovieService(movie_dao) #= MovieService(movie_dao, genre_service, director_service)