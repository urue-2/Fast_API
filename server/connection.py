from pymongo import MongoClient,errors
from .config import *
from influxdb import InfluxDBClient

#mongo db part
def mongodb_connect(mongodb_uri,port):
    try:
        c =  MongoClient(mongodb_uri,port)
        print("successfully to connected to server {}".format(mongodb_uri))
        return c
    except errors.ConnectionFailure:
         print("Failed to connect to server {}".format(mongodb_uri))

client = mongodb_connect(mongodb_uri, port)
db = client['user']
user_collection = db["user_information"]

## database CURD Operation Started ##

def dbregister(user_name,passwd):
    data_in_db = user_collection.find_one({"name": user_name})
    if data_in_db:
        return 0
    else:
        user_collection.insert_one({"name":user_name,"passwd":passwd})
        return 1

def dblogin(user_name,passwd):
    data_in_db = user_collection.find_one({"name":user_name})
    passwd_in_db = data_in_db["passwd"]
    if passwd_in_db == passwd :
        return 1
    else:
        return 0

def dbchange_passwd(user_name,new_passwd):
    query = {"name":user_name}
    newvalues = { "$set": { "passwd": new_passwd } }
    user_collection.update_one(query, newvalues)
    return 1


#influxdb part

def influxdb_connect(influxdb_uri,iport):
    try:
        c =  InfluxDBClient('127.0.0.1', iport, database='user_data')
        print("successfully to connected to server {}".format(influxdb_uri))
        return c
    except errors.ConnectionFailure:
         print("Failed to connect to server {}".format(influxdb_uri))

client = influxdb_connect(influxdb_uri,iport)

def idbinsert(user_name,acc_v,time):
    print("begin write")
    print(client.get_list_measurements())
    data = [
        {
            "measurement": "acc_velocity",
            "fields": {
                "username":user_name,
                "acc":float(acc_v),
            },
            "time": time
        }
    ]

    client.write_points(data,database='user_data')

    print("after write")
    return 1



