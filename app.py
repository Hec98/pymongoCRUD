from pymongo import MongoClient
from uuid import uuid4

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['testDB']
collection = db['registros']

datosInsert = {
    'nombre': 'Manuel',
    'email': 'manuel@gmail.com',
    'telefono': 5555555555,
    'fecha': '21-12-2021',
    'monto': 324,
    'direccion': {
        'numeroInterior': 642,
        'numeroExterior': 242,
        'calle': 'San Nicolas',
        'colonia': 'Loma bonita',
        'ciudad': 'mexico',
        'pais': 'Mexico'
    }
}

# collection.insert_one(datosInsert)

data_1 = {'_id': str(uuid4()), 'nombre': 'Juan', 'edad': 20, 'monto':324}
data_2 = {'_id': str(uuid4()), 'nombre': 'Juanito', 'edad': 21, 'monto':424}

#collection.insert_many([data_1, data_2])

# results = collection.find()
results = collection.find({'edad': 21})
res2 = []
for r in results:
    tem = []
    tem.append(r['_id'])
    tem.append(r['nombre'])
    tem.append(r['edad'])
    tem.append(r['monto'])
    res2.append(tem)

print(f'{res2}\n{type(res2)}')
#print(result)

result = collection.find_one({'edad': 20})
print(result)

# delete = collection.delete_many({'edad': 20})
# delete = collection.delete_many({}) # Delete all
# print(delete)

# collection.delete_one({'edad': 21})

# collection.update_one({"edad": 20}, {'$set': {'edad':21, 'lala': 32}})
# collection.update_many({"edad": 20}, {'$set': {'edad':21, 'lala': 32}})
# collection.update_many({"edad": 21}, {'$inc': {'edad':2}})

number_of_data = collection.count_documents({})
print(number_of_data)
