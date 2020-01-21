import json

from Driver import MongoDB


class Scrapy:
    def __init__(self, db_driver="MongoDB"):
        with open("config.json", "r") as file:
            config = json.loads(file.read())
        if db_driver is "MongoDB":
            self.client = MongoDB(config["mongodb"]["username"], config["mongodb"]["password"],
                                  config["mongodb"]["host"])

    def find(self, collection, query=None, option=None):
        if option is None:
            option = {}
        if query is None:
            query = {}
        self.client.find(collection, query, option)