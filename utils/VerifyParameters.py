def verify_name(new_game):
    if 'name' not in new_game:
        return False
    if type(new_game['name']) != str:
        return False
    return True

def verify_year(new_game):
    if 'year' not in new_game:
        return False
    if type(new_game['year']) != int:
        return False
    return True

def exists_id(id, games):
    if id not in games:
        return False
    return True