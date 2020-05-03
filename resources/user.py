import sqlite3
from flask_restful import Resource, reqparse
from model.user import UserModel

class UserRegister(Resource):

    #parse the request that is coming in
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = "username can't be left blank")
    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = "password can't be left blank")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201

    # def post(self):
    #     data = UserRegister.parser.parse_args()
    #     user = UserModel.find_by_username(data['name'])
    #     if user:
    #         return {'Message' : 'User {} already exists.' .format(data['name'])}
    #
    #     else:
    #         user = UserModel(data['name'], data['password'])
    #         # user.save_to_db()
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "INSERT INTO users VALUES (NULL, ?, ? )"
    #     cursor.execute(query, (data['name'], data['password']))
    #     connection.commit()
    #     connection.close()
    #     return {'Message ' : 'User Created Successfull'}, 201


