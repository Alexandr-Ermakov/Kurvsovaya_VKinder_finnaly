from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import create_all, VkinderDB


def add_result(uid, json):
    engine = create_engine('postgresql://net1:net2@localhost/netology')
    create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = VkinderDB(user=uid, search_data=json)
    session.add(result)
    session.commit()
    print('результат записан в базу\nвыход')