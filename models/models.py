class Server:
    def add():
        pass

    def remove():
        pass

class User:
    def add():
        pass

    def remove():
        pass

    def patch():
        pass


class Server(Base):
    __tablename__ = "server"

    id = Column(String, primary_key=True)

class User(Base):
    __tablename__ = "user"
    
    uuid = Column(Integer, primary_key=True)
    id = Column(String)
    server_id = (String, ForeignKey('server.id'))
    
    server = relationship(Server, backref=backref('users',
                                                  uselist=True
                                                  cascade='delete,all'))

