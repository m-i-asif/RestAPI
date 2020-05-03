#from restfull import *
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from model.item import itemModel


class Item(Resource):
    #dosen't have self before parser so we make it part of item class. to us it will have to call item.parser
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type = float,
                        required = True,
                        help = "Price can't be an integer or left blank")
    parser.add_argument('store_id',
                        type = int,
                        required = True,
                        help = "Every item must have a store id")

    @jwt_required()
    def get(self, name):
        item = itemModel.find_by_name(name)

        if item:
            return item.json(), 200
        return {'message' : 'item not found'}, 404


    def post(self, name):
        data = Item.parser.parse_args()
        item = itemModel(name, data['price'], data['store_id'])
        if itemModel.find_by_name(name):
            return {'message' : "item with {} already exists" .format(name)}, 400

        #itemModel.save_to_db(item)
        item.save_to_db()
        return {'message' : "item Inserted {}" .format(item.json())}, 200

        # if next(iter(filter(lambda x: x['name'] == name, items)), None) is not None:
        #     return {'message' : "item with {} already exists" .format(name)}, 400
        # #request.get_json(force=True) - funtion witout arguments looks for json and if not given throws an error, with force not errors thrown
        # #request.get_json(silen=True) - reteurn's none
        # #data = request.get_json(force=True) #gets data from the request
        # data = Item.parser.parse_args()
        # item = {'name' : name, 'price' : data['price']}
        # items.append(item)
        #return {'Message': 'Item created successfully'}, 201

    def delete (self,name):
        item = itemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'Message ' : 'item deleted'}, 200
        # if itemModel.find_by_name(name):
        #     connection = sqlite3.connect('data.db')
        #     cursor = connection.cursor()
        #     query = "DELETE from item where name = ?"
        #     cursor.execute(query,(name,))
        #     connection.commit()
        #     return {'Message ' : 'item deleted'}, 200
        return {'Message ' : 'item dose not exist'}, 404

    def put (self, name):

        #data = request.get_json(force=True)
        data = Item.parser.parse_args()
        item = itemModel.find_by_name(name)

        if item is None:
            item = itemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        itemModel.save_to_db(item)
        return {'message' : "item inserted {}" .format(item.json())}, 200




class ItemList(Resource):
    def get(self):
        #return {'items' : list(map(lambda  x:x.json(), itemModel.query.all()))}
        return {'items' : [item.json() for item in itemModel.query.all()]}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM item "
        # results = cursor.execute(query)
        # row = results.fetchall()
        # connection.close()
        # #return {'Items' : items}
        # return {'Items' : row}

