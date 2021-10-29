from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

engine = create_engine('mysql+pymysql://root:qwerty@127.0.0.1/mydb')
engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()


class userStatus(BaseModel):
    __tablename__ = "userStatus"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))


class user(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    firstname = Column(VARCHAR(45))
    lastname = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    password = Column(VARCHAR(45))
    phone = Column(VARCHAR(45))
    userStatus_id = Column(Integer, ForeignKey(userStatus.id))

    def __str__(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n" \
               f"phone      : {self.phone}\n"


class ordersStatus(BaseModel):
    __tablename__ = "ordersStatus"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))


class orders(BaseModel):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    shipDate = Column(DateTime)
    complete = Column(Boolean)
    ordersStatus_id = Column(Integer, ForeignKey(ordersStatus.id))
    user_id = Column(Integer, ForeignKey(user.id))


class store(BaseModel):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    category = Column(VARCHAR(45))


class goodsStatus(BaseModel):
    __tablename__ = "goodsStatus"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))


class goods(BaseModel):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    isAvailable = Column(Boolean)
    photoURL = Column(VARCHAR(45))
    store_id = Column(Integer, ForeignKey(store.id))
    goodsStatus_id = Column(Integer, ForeignKey(goodsStatus.id))
    orders_id = Column(Integer, ForeignKey(orders.id))
