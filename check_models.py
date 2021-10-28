from models import Session, user, userStatus, ordersStatus, orders, store, goods, goodsStatus
from datetime import datetime

with Session() as session:
    userstatus0 = userStatus(name='admin')
    user0 = user(username='userNAME', firstname='firstNAME', lastname='lastNAME', email='email@email.com',
                 password='password', phone='0000-000-000', userStatus_id=userstatus0.id)
    ordersstatus0 = ordersStatus(name='placed')
    orders0 = orders(shipDate=datetime.now(), complete=False, ordersStatus_id=ordersstatus0.id, user_id=user0.id)
    store0 = store(name='radiorynok', category='trash')
    goodsStatus0 = goodsStatus(name='pending')
    goods0 = goods(name='razorblade', isAvailable=True, photoURL='photoURL.com', store_id=store0.id, goodsStatus_id=goodsStatus0.id,
                   orders_id=orders0.id)
    session.add(userstatus0)
    session.commit()
    session.add(user0)
    session.add(ordersstatus0)
    session.commit()
    session.add(orders0)
    session.add(store0)
    session.add(goodsStatus0)
    session.commit()
    session.add(goods0)
    session.commit()

print(session.query(user).all()[0])
