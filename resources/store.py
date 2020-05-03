from flask_restful import Resource, reqparse
from model.store import storeModel

class Store(Resource):

    def get (self, name):
        store = storeModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message' : 'store not found'}, 404

    def post (self, name):
        if storeModel.find_by_name(name):
            return {'message' : "store with {} already exists" .format(name)}, 400
        store = storeModel(name)

        try:
            store.save_to_db()
        except:
            return {'Message' : 'Error occured creating store'},    500

        return store.json(), 201

    def delete (self, name):
        store = storeModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'Message' : 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores' : [store.json() for store in storeModel.query.all()]}
