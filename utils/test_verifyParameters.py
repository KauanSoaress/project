from VerifyParameters import verify_name, verify_year

def test_verify_name():
    data = {
        "name": "The Last of Us",
    }

    correct_data = verify_name(data)    

    assert correct_data == True, "Erro com entrada correta do campo name"
    
def test_verify_name_field_missing():
    data = {
        "year": 123456,
    }

    without_name = verify_name(data)

    assert without_name == False, "Erro de falta de campo do campo name"

def test_verify_name_type_number():
    data = {
        "name": 123456,
    }

    name_type_number = verify_name(data)

    assert name_type_number == False, "Erro de tipo do campo name (number)"

def test_verify_name_type_boolean():
    data = {
        "name": True,
    }

    name_type_boolean = verify_name(data)

    assert name_type_boolean == False, "Erro de tipo do campo name (boolean)"

def test_verify_year():
    data = {
        "year": 2004,
    }

    correct_data = verify_year(data)    

    assert correct_data == True, "Erro com entrada year correta"
    
def test_verify_year_field_missing():
    data = {
        "name": 123456,
    }

    without_year = verify_year(data)

    assert without_year == False, "Erro de falta de campo year"

def test_verify_year_type_string():
    data = {
        "year": "hoje",
    }

    year_type_string = verify_year(data)

    assert year_type_string == False, "Erro de tipo do campo year (string)"

def test_verify_year_type_boolean():
    data = {
        "year": True,
    }

    year_type_boolean = verify_year(data)

    assert year_type_boolean == False, "Erro de tipo do campo year (boolean)"

def test_verify_year_small_field_lenght():
    data = {
        "year": 201,
    }

    year_small_field = verify_year(data)

    assert year_small_field == False, "Erro de tamanho do campo year (small)"

def test_verify_year_big_field_lenght():
    data = {
        "year": 20112,
    }

    year_big_field = verify_year(data)

    assert year_big_field == False, "Erro de tamanho do campo year (big)"

if __name__ == '__main__':
    test_verify_name()
    test_verify_name_field_missing()
    test_verify_name_type_number()
    test_verify_name_type_boolean()

    test_verify_year()
    test_verify_year_field_missing()
    test_verify_year_type_string()
    test_verify_year_type_boolean()
    test_verify_year_small_field_lenght()
    test_verify_year_big_field_lenght()