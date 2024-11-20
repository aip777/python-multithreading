from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///customer_data.db', echo=True)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    address = Column(String)
    phone_number = Column(String)

def insert_data(data):
    Session = sessionmaker(bind=engine)
    session = Session()
    inspector = inspect(engine)
    if 'customers' in inspector.get_table_names():
        print("The table 'customers' exists!")
    else:
        Base.metadata.create_all(engine)
    new_customer = Customer(
        id=data[0],
        name=data[1],
        email=data[2],
        age=data[3],
        address=data[4],
        phone_number=data[5]
    )
    session.add(new_customer)
    session.commit()
    print("Data inserted successfully!")
