import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
    #don't use the  __init__ when creating this class object b/c unlike the Post object we created,
    #here we don't want multiple paths or multiple databases. There is only 1 db for this project, so no need for init

    #have to say staticmethod to let python we aren't using self. Initialize is for Database as a whole
    #get me a client then the database we are going to use. This means after intilaizing Database.DATABASE will have all of our data to use in our script
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        #get the collection and insert new data
        Database.DATABASE[collection].insert(data)

    #return a mongo cursery object
    @staticmethod
    def find(collection, query):
        #get the collection and insert new data
        return Database.DATABASE[collection].find(query)

    #return the first json object
    @staticmethod
    def find_one(collection, query):
        #get the collection and insert new data
        return Database.DATABASE[collection].find_one(query)

