from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        """
            Получение жанра
        """
        return self.session.query(Genre).filter(Genre.id == gid)

    def get_all(self):
        """
            Получение жанров
        """
        return self.session.query(Genre).all()
