from bson import ObjectId

def verify_name(new_game):
    if 'name' not in new_game or type(new_game['name']) != str:
        return False
    return True

def verify_year(new_game):
    if 'year' not in new_game or type(new_game['year']) != int:
        return False
    return True

def verify_id(id):
    try:
        ObjectId(id)
    except:
        return False
    return True