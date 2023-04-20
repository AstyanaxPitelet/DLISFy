from pymongo import MongoClient

class DbAccess:

    __instance = None 

    def get_instance() -> MongoClient:
        if DbAccess.__instance is None:
            DbAccess.__instance = MongoClient(host="localhost", port="27017")
        return DbAccess.__instance