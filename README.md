# FastAPI server Using MongoDB&Influxdb  


This is a  FastAPI based Web API that simulates a server while using  MongoDB & Influx database.

### Problem Statement

Build a server via fastapi to implement the following functions : receiving,parsing data and operations with database
 


### Requirements
```
uvicorn==0.15.0
pymongo==3.12.0
fastapi==0.70.0
influxdb==5.3.1
```

Run Following commond to install requirement on your machine:

`> pip install -r requirements.txt
`

### Running database

step 1 : make sure that your database server is running ( if not you can run it in Task Manager in Windows )

step 2 : open terminal / powershell in windows ( for influxdb )

step 3 : going to the folder where your database.exe is loaded

step 4 : run your database.exe ( mongodb:mongo.exe influxdb:influxd.exe )

### Running API Server
We are using Uvicorn for running FastAPI Server. 
> Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

For starting the server you need to run following commond in working directory:

`> python main.py`



### Accessing the API

Server are running on localhost `127.0.0.1` and port number `7000`, you can just type on your browser or Postman Tool:

`http://127.0.0.1:7000/`

explanation : to change the host and port for the server modify in main.py 

We are using python Request package for testing the API, You can performe diffrent CURD operation using followings:

**Mongodb :**  for all the operation for mongodb implement log.py , change parameters to what you want

**Influxdb :**  for all the operation for influxdb implement acc.py , change parameters to what you want


This is a whole process of running the FastAPI Server with MongoDB ,Influxdb Database, If you have any query, you can reach out us via email : `ruiyi_ni@126.com`
