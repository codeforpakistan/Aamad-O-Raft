from mongokit import Document, Connection
#from pymongo import MongoClient
import config
import datetime

# Schema-----------------------------------------------------------------------
class Route(Document):
    __collection__ = 'routes'
    __database__= 'amdoraft'

    structure = {
        'id': int,
        'name': basestring,
        'start': basestring,
        'end': basestring,
        'stops': list
        }


class Stop(Document):
    __collection__ = 'stops'
    __database__= 'amdoraft'

    structure = {
        'id': int,
        'name': basestring,
        'latitude' : float,
        'longitude' : float
    }



# DBConnection class---------------------------------------------------------------
class DBConnection(object):

    def __init__(self):
        #mongodb_uri = "mongodb://13.76.244.22:27017"
        #mongolab_uri = "mongodb://shahid:sakmongo054@ds062818.mlab.com:62818/MongoLab-25"
        #connectionString = 'mongodb://MongoLab-25:gvoi8dKuIr9vOSAEEpW2Kim5Mo2Kb5FHzZaK.vpU1cg-@ds062818.mlab.com:62818/MongoLab-25'
        #self.client = MongoClient(mongolab_uri,
        #             connectTimeoutMS=30000,
        #             socketTimeoutMS=None,
        #             socketKeepAlive=True)
        #self.db = self.client.get_default_database()
        #self.con = Connection(mongodb_uri)
        self.con = Connection()

        self.con.register([Route])
        self.con.register([Stop])

        self.routes = self.con.Route
        self.stops = self.con.Stop
        
    def __del__(self):
        self.con.close()
        self.con.disconnect()

    def connect():        
        con = Connection()
        routes = con.amdoraft.routes
        stops = con.amdoraft.stops
        return

    def disconnect():
        return

