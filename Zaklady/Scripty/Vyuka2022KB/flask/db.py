from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=True)
    local_part = Column(String(64),  nullable=False)
    domain = Column(String(255), nullable=False)
    password = Column(String(60), nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.local_part}@{self.domain}', nickname='{self.password}')>"


# User.__table__
# Base.metadata.create_all(engine)
# ed_user = User(username='ed', local_part='ed', domain= 'seznam.cz',password='heslo123')
session = Session()
# session.add(ed_user)
# session.commit()
# our_user = session.query(User).filter_by(username='ed').first()
# print(our_user)
# print(ed_user is our_user)
session.add_all([User(username='wendy', local_part='wendy', domain='gmail.com', password='windy'),User(username='mary', local_part='mary', domain='gmail.com', password='marz123'),User(username='fred', local_part='fred', domain='email.com', password='freddy123')])
session.commit()
for instance in session.query(User).order_by(User.id): print(instance.username,f"{instance.local_part}@{instance.domain}")