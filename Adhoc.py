import pymongo
try:
    client = MongoClient(mongodb+srv://nitsuga:nitsugagustin321@asignacionaulasucp-gf74h.mongodb.net/test?retryWrites=true&w=majority)
    print("Exito")
except:
    print("Fallo")
