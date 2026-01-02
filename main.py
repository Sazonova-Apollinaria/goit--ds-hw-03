from db import collection
from pymongo.errors import PyMongoError


#CREATE 
def add_cat():
    cat = {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    }
    try:
        collection.insert_one(cat)
        print("Кота додано 🐱")
    except PyMongoError as e:
        print(e)


#READ 
def show_all_cats():
    try:
        for cat in collection.find():
            print(cat)
    except PyMongoError as e:
        print(e)


#READ 
def find_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кота не знайдено")
    except PyMongoError as e:
        print(e)


#UPDATE 
def update_cat_age(name, age):
    try:
        collection.update_one(
            {"name": name},
            {"$set": {"age": age}}
        )
        print("Вік оновлено")
    except PyMongoError as e:
        print(e)


#UPDATE 
def add_feature(name, feature):
    try:
        collection.update_one(
            {"name": name},
            {"$push": {"features": feature}}
        )
        print("Характеристику додано")
    except PyMongoError as e:
        print(e)


#DELETE 
def delete_cat(name):
    try:
        collection.delete_one({"name": name})
        print("Кота видалено")
    except PyMongoError as e:
        print(e)


#DELETE 
def delete_all():
    try:
        collection.delete_many({})
        print("Колекцію очищено")
    except PyMongoError as e:
        print(e)