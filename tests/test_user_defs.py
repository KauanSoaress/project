import unittest
from unittest.mock import patch, Mock, MagicMock
from bson import ObjectId
from flask import Flask
from utils.user_utils.user_defs import get_user, \
    get_user_by_id, delete_user, edit_user, post_user


class TestUserDefs(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['MONGO_DB'] = MagicMock()
        self.mock_user_collection = Mock()
        self.app.config['MONGO_DB'].__getitem__.return_value = \
            self.mock_user_collection
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.request_context = self.app.test_request_context()
        self.request_context.push()

    def test_get_user(self):
        mock_find = self.mock_user_collection.find
        mock_find.return_value = [
            {"name": "User 1", "age": 21},
            {"name": "User 2", "age": 22}
        ]

        response = get_user()

        mock_find.assert_called_once_with({}, {"_id": 0, "name": 1, "age": 1})

        self.assertEqual(response.status_code, 200)
        self.assertIn('User list', response.get_json()['message'])
        self.assertEqual(len(response.get_json()['user']), 2)
        self.assertEqual(response.get_json()['user'][0]['name'], 'User 1')
        self.assertEqual(response.get_json()['user'][1]['name'], 'User 2')
        self.assertEqual(response.get_json()['user'][0]['age'], 21)
        self.assertEqual(response.get_json()['user'][1]['age'], 22)

    @patch('utils.user_utils.user_defs.verify_id')
    def test_get_user_by_id(self, mock_verify_id):
        mock_find_one = self.mock_user_collection.find_one
        mock_find_one.return_value = {"name": "User", "age": 21}

        mock_verify_id.return_value = True

        response = get_user_by_id('66a3d3e92646ece2a8c4e49c')

        mock_find_one.assert_called_once_with(
            {"_id": ObjectId('66a3d3e92646ece2a8c4e49c')},
            {"_id": 0, "name": 1, "age": 1}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('User found', response.get_json()['message'])

    @patch('utils.user_utils.user_defs.verify_name')
    @patch('utils.user_utils.user_defs.verify_age')
    def test_post_user(self, mock_verify_age, mock_verify_name):
        mock_insert = self.mock_user_collection.insert_one
        mock_insert.return_value = Mock(
            inserted_id=ObjectId('66a3d3e92646ece2a8c4e49c')
        )

        mock_verify_age.return_value = True
        mock_verify_name.return_value = True

        with self.app.test_request_context(json={"name": "User 1", "age": 21}):
            response = post_user()

            mock_insert.assert_called_once_with(
                {
                    "name": "User 1",
                    "age": 21,
                    '_id': '66a3d3e92646ece2a8c4e49c'
                }
            )

            self.assertEqual(response.status_code, 200)

    @patch('utils.user_utils.user_defs.verify_id')
    def test_delete_user(self, mock_verify_id):
        mock_delete_one = self.mock_user_collection.delete_one

        mock_verify_id.return_value = True

        response = delete_user('66a3d3e92646ece2a8c4e49c')

        mock_delete_one.assert_called_once_with(
            {"_id": ObjectId('66a3d3e92646ece2a8c4e49c')}
        )

        self.assertEqual(response.status_code, 200)

    @patch('utils.user_utils.user_defs.verify_name')
    @patch('utils.user_utils.user_defs.verify_age')
    @patch('utils.user_utils.user_defs.verify_id')
    def test_edit_user(
        self,
        mock_verify_id,
        mock_verify_age,
        mock_verify_name
    ):
        mock_update_one = self.mock_user_collection.update_one

        mock_verify_id.return_value = True
        mock_verify_name.return_value = True
        mock_verify_age.return_value = True

        with self.app.test_request_context(json={"name": "User 1", "age": 21}):
            response = edit_user('66a3d3e92646ece2a8c4e49c')

            mock_update_one.assert_called_once_with(
                {"_id": ObjectId('66a3d3e92646ece2a8c4e49c')},
                {"$set": {"name": "User 1", "age": 21}}
            )

            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
