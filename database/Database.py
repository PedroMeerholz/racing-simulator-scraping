from pymongo.mongo_client import MongoClient


class Database:
    uri = "YOUR_MONGO_URI_HERE"
    client = MongoClient(uri)
    database = client['test']

    def load_car_list_to_database(self, car_list: list, platform: str):
        for car in car_list:
            data = {'name': car, 'platform': platform}
            self.database['car'].insert_one(data)

    def load_track_list_to_database(self, track_list: list, platform: str):
        for track in track_list:
            data = {'name': track, 'platform': platform}
            self.database['track'].insert_one(data)
