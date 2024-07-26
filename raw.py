from pymongo import MongoClient

connetion_string = "mongodb://localhost:27017/?authSource=admin"

client = MongoClient(connetion_string)
db_connection = client["pessoasData"]

collection = db_connection.get_collection("pessoas")

search_filter = { "idade": { "$gt": 20 } }

response = collection.find(search_filter)

for registry in response:
    print(registry)

client_to_insert = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

collection.insert_one(client_to_insert)