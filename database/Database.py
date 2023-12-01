from pymongo.mongo_client import MongoClient


class Database:
    uri = "YOUR_MONGO_URI_HERE"
    client = MongoClient(uri)
    database = client['test']
    collection = database['car']

    def load_car_list_to_database(self, car_list, platform):
        for car in car_list:
            data = {'name': car, 'platform': platform}
            self.collection.insert_one(data)
