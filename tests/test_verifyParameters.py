from utils.games_utils.VerifyParameters import verify_name, verify_year, verify_id
import unittest

class TestsVerifyName(unittest.TestCase):

    def test_verify_name(self):
        data = {
            "name": "The Last of Us",
        }

        correct_data = verify_name(data)    

        self.assertTrue(correct_data, "Falha com dados corretos")
        
    def test_verify_name_field_missing(self):
        data = {
            "year": 123456,
        }

        without_name = verify_name(data)

        self.assertFalse(without_name, "Falha com campo faltando")

    def test_verify_name_type_number(self):
        data = {
            "name": 123456,
        }

        name_type_number = verify_name(data)

        self.assertFalse(name_type_number, "Falha com tipo trocado (number)")

    def test_verify_name_type_boolean(self):
        data = {
            "name": True,
        }

        name_type_boolean = verify_name(data)

        self.assertFalse(name_type_boolean, "Falha com tipo trocado (boolean)")

class TestsVerifyYear(unittest.TestCase):
    def test_verify_year(self):
        data = {
            "year": 2004,
        }

        correct_data = verify_year(data)    

        self.assertTrue(correct_data, "Falha com dados corretos")
        
    def test_verify_year_field_missing(self):
        data = {
            "name": 123456,
        }

        without_year = verify_year(data)

        self.assertFalse(without_year, "Falha com campo faltando")

    def test_verify_year_type_string(self):
        data = {
            "year": "hoje",
        }

        year_type_string = verify_year(data)

        self.assertFalse(year_type_string, "Falha com tipo trocado (string)")

    def test_verify_year_type_boolean(self):
        data = {
            "year": True,
        }

        year_type_boolean = verify_year(data)

        self.assertFalse(year_type_boolean, "Falha com tipo trocado (boolean)")

    def test_verify_year_small_field_lenght(self):
        data = {
            "year": 201,
        }

        year_small_field = verify_year(data)

        self.assertFalse(year_small_field, "Erro de tamanho do campo year (small)")

    def test_verify_year_big_field_lenght(self):
        data = {
            "year": 20112,
        }

        year_big_field = verify_year(data)

        self.assertFalse(year_big_field, "Erro de tamanho do campo year (big)")

class TestsVerifyId(unittest.TestCase):
    def test_verify_id(self):
        id = "5f7d2a9f1c9d440000f0b7d5"

        correct_id = verify_id(id)

        self.assertTrue(correct_id, "Falha com id correto")
    
    def test_verify_id_wrong_id(self):
        id = "5f7d2a9f1c9d440000f0b7d"

        wrong_id = verify_id(id)

        self.assertFalse(wrong_id, "Falha com id errado")
    
    def test_verify_id_wrong_id_type(self):
        id = 123456

        wrong_id_type = verify_id(id)

        self.assertFalse(wrong_id_type, "Falha com tipo errado (number)")
    
    def test_verify_id_wrong_id_type_boolean(self):
        id = True

        wrong_id_type_boolean = verify_id(id)

        self.assertFalse(wrong_id_type_boolean, "Falha com tipo errado (boolean)")

if __name__ == '__main__':
    unittest.main()