#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakey = Bakery.query.all()
    bakey_dict = []
    for bake in bakey:
        bk = bake.to_dict()
        bakey_dict.append(bk)
    response = make_response(
        jsonify(bakey_dict), 200
    )
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakey = Bakery.query.filter(Bakery.id == id).first().to_dict()
    response = make_response(
        jsonify(bakey), 200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bakey = BakedGood.query.order_by(BakedGood.price.desc()).all()
    bake = []
    for bk in bakey:
        b = bk.to_dict()
        bake.append(b)
        
    response = make_response(
        jsonify(bake), 200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    bakey = BakedGood.query.order_by(BakedGood.price.desc()).all()
    resp = bakey[0].to_dict()       
    response = make_response(
        jsonify(resp), 200
    )
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
