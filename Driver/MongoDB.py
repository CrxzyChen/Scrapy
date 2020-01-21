from urllib import parse

import pymongo


class MongoDB:
    def __init__(self, username, password, host, port="27017", database="scrapy"):
        self.username = parse.quote_plus(username)
        self.password = parse.quote_plus(password)
        self.host = host
        self.port = port
        self.uri = "mongodb://{0}:{1}@{2}:{3}".format(self.username, self.password, self.host, self.port)
        self.client = pymongo.MongoClient(self.uri)
        self.database = database
        self.db = self.client.get_database(self.database)

    def find(self, collection, query, option):
        return self.db.get_collection(collection).find(query, option)
