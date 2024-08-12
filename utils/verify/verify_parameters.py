from bson import ObjectId


def verify_name(new_game):
    if 'name' not in new_game or not isinstance(new_game['name'], str):
        return False
    return True


def verify_year(new_game):
    if 'year' not in new_game or not isinstance(new_game['year'], int) \
      or len(str(new_game['year'])) != 4:
        return False
    return True


def verify_id(id):
    try:
        ObjectId(id)
    except Exception:
        return False
    return True


def verify_age(new_user):
    if 'age' not in new_user or not isinstance(new_user['age'], int) or new_user['age'] < 0:
        return False
    return True
