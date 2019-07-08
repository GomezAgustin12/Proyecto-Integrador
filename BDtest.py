import pymongo

try:
    client = pymongo.MongoClient("mongodb+srv://nitsuga:nitsugagustin321@asignacionaulasucp-gf74h.mongodb.net/test?retryWrites=true&w=majority")
except:
    print("Fail")
db = client.Simulacion
Materia = db.Materia

a=Materia.find({'Nombre':'Derecho de los Contratos'})

for x in a:
    print(x["Facultad"])
    


