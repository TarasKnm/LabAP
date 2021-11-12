from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from datetime import datetime
from models import Session, user, userStatus, ordersStatus, orders, store, goods, goodsStatus
from flask import Flask
from flask_bcrypt import Bcrypt, check_password_hash

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Goods swagger API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'firstname', 'lastname', 'email', 'password', 'phone', 'userStatus_id')


class GoodsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'isAvailable', 'photoURL', 'status')


class OrdersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'shipDate', 'complete', 'ordersStatus_id', 'user_id', 'goods_id')


class StatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


users_schema = UserSchema(many=True)

orders_schema = OrdersSchema(many=True)

goods_schema = GoodsSchema(many=True)

statuses_schema = StatusSchema(many=True)


@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)

# ______________________________________________USER______________________________________________


@app.route("/user", methods=["POST"])
def add_user():
    #try:
    username_ = request.json['username']
    firstname_ = request.json['firstName']
    lastname_ = request.json['lastName']
    email_ = request.json['email']
    password_ = request.json['password']
    pw_hash = bcrypt.generate_password_hash(password_)
    phone_ = request.json['phone']
    status_ = request.json['userStatus']

    userstatus_ = Session().query(userStatus).filter(userStatus.name.like('%' + status_ + '%')).limit(1)
    result_set = statuses_schema.dump(userstatus_)

    user_ = user(username=username_, firstname=firstname_, lastname=lastname_, email=email_,
                     password=pw_hash, phone=phone_, userStatus_id=result_set[0]['id'])

    Session().add(user_)
    Session().commit()
    return jsonify({"username": username_, "firstName": firstname_, "lastName": lastname_,
                        "email": email_, "password": str(pw_hash), "phone": phone_, "userStatus": status_})
    #except Exception as e:
        #return jsonify({"Error": "Invalid Request, please try again."})


@app.route("/user", methods=["GET"])
def get_users():
    users_ = Session().query(user)
    result_set = users_schema.dump(users_)
    for i in result_set:
        status_ = Session().query(userStatus).filter(userStatus.id == i['userStatus_id'])
        users_status_ = statuses_schema.dump(status_)
        i.pop('userStatus_id', None)
        i['userStatus'] = users_status_[0]['name']
    return jsonify(result_set)


@app.route("/user/login", methods=["GET"])   # imitate login user, does not working
def login_user():
    #try:
    username_ = request.args.get('username')
    password_ = request.args.get('password')

    users_ = Session().query(user).filter(user.username.like('%' + username_ + '%')).limit(1)
    result_set = users_schema.dump(users_)

    if not check_password_hash(result_set[0]['password'], password_):
        print(result_set['password'])
        return jsonify({'Error': 'Wrong password'})

    status_ = Session().query(userStatus).filter(userStatus.id == result_set[0]['userStatus_id'])
    users_status_ = statuses_schema.dump(status_)

    result_set[0].pop('userStatus_id', None)
    result_set[0]['userStatus'] = users_status_[0]['name']
    return jsonify(result_set)
    #except Exception as e:
        #return jsonify({"Error": "Invalid request, please try again."})


@app.route("/user/logout", methods=["GET"])   # imitate logout user, does not working
def logout_user():
    return jsonify({"Success": "Logout user"})


@app.route("/user/<string:username>", methods=["DELETE"])
def delete_user(username):

    #try:
    Session().query(user).filter(user.username == username).delete()
    Session().commit()

    #except Exception as e:
        #return jsonify({"Error": "Invalid request, please try again."})
    return jsonify({"Success": "User deleted."})


@app.route("/user/<string:username>", methods=["GET"])
def get_user(username):
    user_ = Session().query(user).filter(user.username.like('%' + username + '%')).limit(1)
    result_set = users_schema.dump(user_)

    status_ = Session().query(userStatus).filter(userStatus.id == result_set[0]['userStatus_id'])
    users_status_ = statuses_schema.dump(status_)

    result_set[0].pop('userStatus_id', None)
    result_set[0]['userStatus'] = users_status_[0]['name']
    return jsonify(result_set)


@app.route("/user/<string:username>", methods=["PUT"])
def update_user(username):

    #try:
    username_ = request.json['username']
    firstname_ = request.json['firstName']
    lastname_ = request.json['lastName']
    email_ = request.json['email']
    password_ = request.json['password']
    phone_ = request.json['phone']
    userstatus_ = request.json['userStatus']

    status_ = Session().query(userStatus).filter(userStatus.name == userstatus_).limit(1)
    users_status_ = statuses_schema.dump(status_)

    Session().query(user).filter(user.username == username). \
            update({"username": username_, "firstname": firstname_, "lastname": lastname_,
                    "email":email_, "password": password_, "phone": phone_, "userStatus_id": users_status_[0]['id']}, synchronize_session="fetch")
    Session().commit()

    #except Exception as e:
        #return jsonify({"Error": "Invalid request, please try again."})
    return jsonify({"username": username_, "firstname": firstname_, "lastname": lastname_,
                    "email":email_, "password": password_, "phone": phone_, "userStatus": userstatus_})

# ______________________________________________STORE______________________________________________


@app.route("/store/order", methods=["POST"])
def add_order():
    #try:
    goodsId_ = request.json['goodsId']
    status_ = request.json['status']
    complete_ = request.json['complete']
    userId_ = request.json['userId']
    shipDate_ = datetime.now()

    orderStatus_ = Session().query(ordersStatus).filter(ordersStatus.name.like('%' + status_ + '%')).limit(1)
    result_set = statuses_schema.dump(orderStatus_)

    order_ = orders(shipDate=shipDate_, complete=complete_, ordersStatus_id=result_set[0]['id'], user_id=userId_, goods_id=goodsId_)

    Session().add(order_)
    Session().commit()
    return jsonify({"goodsId": goodsId_, "shipDate": shipDate_, "status": status_,
                        "complete": complete_, "userId":userId_})
    #except Exception as e:
        #return jsonify({"Error": "Invalid Request, please try again."})


@app.route("/store/store", methods=["POST"])
def add_store():
    #try:
    name_ = request.json['name']
    category_ = request.json['category']
    goods_ = request.json['goods']

    store_ = store(name=name_, category=category_)

    Session().add(store_)
    Session().commit()

    for item in goods_:
        photoUrls_string = ''
        for i in item['photoUrls']:
            photoUrls_string += str(i) + ' '

        goodsstatus_ = Session().query(goodsStatus).filter(goodsStatus.name.like('%' + item['status'] + '%')).limit(1)
        result_set = statuses_schema.dump(goodsstatus_)

        new_obj = goods(name=item['name'], isAvailable=item['isAvailable'], photoURL=photoUrls_string, store_id=store_.id, goodsStatus_id=result_set[0]['id'])
        Session().add(new_obj)

    Session().commit()

    return jsonify({"name": name_, "category": category_, "goods": goods_})
    #except Exception as e:
        #return jsonify({"Error": "Invalid Request, please try again."})


@app.route("/store/order/<int:id>", methods=["GET"])
def get_order_by_id(id):
    orders_ = Session().query(orders).filter(orders.id == id)
    result_set = orders_schema.dump(orders_)
    return jsonify(result_set)


@app.route("/store/order/<int:id>", methods=["DELETE"])
def delete_order_by_id(id):
    Session().query(orders).filter(orders.id == id).delete()
    Session().commit()
    return jsonify({"Success": "Order deleted"})


@app.route("/store/goods/<int:id>", methods=["POST"])
def add_goods(id):
    #try:

    name_ = request.json['name']
    isAvailable_ = request.json['isAvailable']
    photoUrls_ = request.json['photoUrls']
    photoUrls_string = ' '.join([str(item) for item in photoUrls_])
    status_ = request.json['status']

    goodsstatus_ = Session().query(goodsStatus).filter(goodsStatus.name.like('%' + status_ + '%')).limit(1)
    result_set = statuses_schema.dump(goodsstatus_)
    new_obj = goods(name=name_, isAvailable=isAvailable_, photoURL=photoUrls_string, store_id=id, goodsStatus_id=result_set[0]['id'])

    Session().add(new_obj)
    Session().commit()
    return jsonify({"name": name_, "isAvailable": isAvailable_, "photoUrls": photoUrls_,
                        "status": status_})
   # except Exception as e:
        #return jsonify({"Error": "Invalid Request, please try again."})


@app.route("/store/goods/<int:id>", methods=["GET"])
def get_goods(id):
    goods_ = Session().query(goods).filter(goods.store_id == id)
    result_set = goods_schema.dump(goods_)
    return jsonify(result_set)

# ______________________________________________GOODS______________________________________________


@app.route("/goods/<int:id>", methods=["GET"])
def get_goods_by_id(id):
    goods_ = Session().query(goods).filter(goods.id == id)
    result_set = goods_schema.dump(goods_)
    return jsonify(result_set)


@app.route("/goods/<int:id>", methods=["DELETE"])
def delete_goods_by_id(id):

    #try:
    Session().query(goods).filter(goods.id == id).delete()
    Session().commit()

    return jsonify({"Success": "Goods deleted."})
    #except:
        #return jsonify({"Error": "Invalid request, please try again."})


@app.route("/goods/<string:name>", methods=["PUT"])
def update_goods(name):

    #try:
    name_ = request.json['name']
    isAvailable_ = request.json['isAvailable']
    photoUrls_ = request.json['photoUrls']
    photoUrls_string = ' '.join([str(item) for item in photoUrls_])
    status_ = request.json['status']

    goodsstatus_ = Session().query(goodsStatus).filter(goodsStatus.name.like('%' + status_ + '%')).limit(1)
    result_set = statuses_schema.dump(goodsstatus_)

    Session().query(goods).filter(goods.name.like('%' + name + '%')). \
            update({"name": name_, "isAvailable": isAvailable_, "photoURL": photoUrls_string,
                     "goodsStatus_id": result_set[0]['id']},
                   synchronize_session="fetch")
    Session().commit()
    #except Exception as e:
        #return jsonify({"Error": "Invalid request, please try again."})
    return jsonify(({"name": name_, "isAvailable": isAvailable_, "photoUrls": photoUrls_,
                        "status": status_}))


@app.route("/goods/<int:id>", methods=["PUT"])
def update_goods_by_id(id):

    #try:
    name_ = request.json['name']
    isAvailable_ = request.json['isAvailable']
    photoUrls_ = request.json['photoUrls']
    photoUrls_string = ' '.join([str(item) for item in photoUrls_])
    status_ = request.json['status']

    goodsstatus_ = Session().query(goodsStatus).filter(goodsStatus.name.like('%' + status_ + '%')).limit(1)
    result_set = statuses_schema.dump(goodsstatus_)

    Session().query(goods).filter(goods.id == id). \
            update({"name": name_, "isAvailable": isAvailable_, "photoURL": photoUrls_string,
                     "goodsStatus_id": result_set[0]['id']},
                   synchronize_session="fetch")
    Session().commit()
    #except Exception as e:
        #return jsonify({"Error": "Invalid request, please try again."})
    return jsonify(({"name": name_, "isAvailable": isAvailable_, "photoUrls": photoUrls_,
                        "status": status_}))


@app.route("/goods/findByStatus", methods=["GET"])   # imitate login user, does not working
def get_goods_by_status():
    status_ = request.args.get('status')
    goodsstatus_ = Session().query(goodsStatus).filter(goodsStatus.name.like('%' + status_ + '%')).limit(1)
    result_set = statuses_schema.dump(goodsstatus_)
    goods_ = Session().query(goods.id, goods.name, goods.isAvailable, goods.photoURL).filter(goods.goodsStatus_id == result_set[0]['id'])

    goods_set = goods_schema.dump(goods_)
    return jsonify(goods_set)


if __name__ == "__main__":
    app.run(debug = True)