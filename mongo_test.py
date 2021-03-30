from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://root:s3cr37@localhost:27027')
    db = client.person_db
    persons_collection = db.persons
    p1 = {
        'first_name': 'Tommy',
        'last_name': 'Persson',
        'age': 34,
        'likes': ['Training', 'Instagram', 'Animals']
    }
    p2 = {
        'first_name': 'Anna',
        'last_name': 'Persson',
        'age': 53,
        'likes': ['Weapons', 'Body building', 'Animals'],
        'fav_music': ['Metal', 'Trash']
    }
    p1['_id'] = persons_collection.insert_one(p1).inserted_id
    p2['_id'] = persons_collection.insert_one(p2).inserted_id

    print(p1)
    print(p2)


if __name__ == '__main__':
    main()