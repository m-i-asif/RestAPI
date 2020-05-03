from db import db

class itemModel(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('storeModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'Name' : self.name, 'Price' : self.price}

    @classmethod
    def find_by_name(cls, name):
        #return db.Query.filter_by(name=name).first()
        return cls.query.filter_by(name=name).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM item where name = ?"
        # results = cursor.execute(query,(name,))
        # row = results.fetchone()
        # connection.close()
        # if row:
        #     return cls(row[1],row[2])
        # return None

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    # def insert(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO item VALUES (NULL, ?, ?)"
        # cursor.execute(query,(self.name, self.price))
        # connection.commit()
        # connection.close()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    # def update_item(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "UPDATE item SET price = ? where name = ?"
    #     cursor.execute(query,(self.price, self.name))
    #     connection.commit()
    #     connection.close()

