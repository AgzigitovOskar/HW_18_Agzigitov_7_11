from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        """
            Получение директора
        """
        return self.session.query(Director).filter(Director.id == did)

    def get_all(self):
        """
            Получение директоров
        """
        return self.session.query(Director).all()
