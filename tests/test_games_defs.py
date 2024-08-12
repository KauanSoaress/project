import unittest
from unittest.mock import patch, Mock, MagicMock
from bson import ObjectId
from flask import Flask
from utils.games_utils.games_defs import get_games, post_games, get_game_by_name, delete_game, edit_game

class TestGamesDefs(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['MONGO_DB'] = MagicMock()
        self.mock_games_collection = Mock()
        self.app.config['MONGO_DB'].__getitem__.return_value = self.mock_games_collection
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.request_context = self.app.test_request_context()
        self.request_context.push()


    def test_get_games_success(self):
        mock_find = self.mock_games_collection.find
        mock_find.return_value = [
            {"name": "Game 1", "year": 2021},
            {"name": "Game 2", "year": 2022}
        ]

        response = get_games()

        mock_find.assert_called_once_with({}, {"_id": 0, "name": 1, "year": 1})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Games list', response.get_json()['message'])
        self.assertEqual(len(response.get_json()['games']), 2)
        self.assertEqual(response.get_json()['games'][0]['name'], 'Game 1')
        self.assertEqual(response.get_json()['games'][1]['name'], 'Game 2')

    def test_get_game_by_name_sucess(self):
        mock_find_one = self.mock_games_collection.find_one
        mock_find_one.return_value = {"name": "Game", "year": 2021, "user_id": "66a3d3e92646ece2a8c4e49c"}

        response = get_game_by_name('Game')

        mock_find_one.assert_called_once_with({'name': 'Game'}, {"_id": 0, "name": 1, "year": 1, "user_id": 1})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Game found', response.get_json()['message'])

    @patch('utils.games_utils.games_defs.verify_name')
    @patch('utils.games_utils.games_defs.verify_year')
    @patch('utils.games_utils.games_defs.verify_id')
    def test_post_games(self, mock_verify_id, mock_verify_year, mock_verify_name):
        mock_insert = self.mock_games_collection.insert_one
        mock_insert.return_value = Mock(inserted_id=ObjectId('66a3d3e92646ece2a8c4e49c'))

        mock_verify_year.return_value = True
        mock_verify_name.return_value = True
        mock_verify_id.return_value = True
    
        with self.app.test_request_context(json={"name": "Game 1", "year": 2021, "user_id": '66a3d3e92646ece2a8c4e49c'}):
            response = post_games()

            mock_insert.assert_called_once_with({"name": "Game 1", "user_id": '66a3d3e92646ece2a8c4e49c', "year": 2021, '_id': '66a3d3e92646ece2a8c4e49c'})

            self.assertEqual(response.status_code, 200)
            self.assertIn('Game created', response.get_json()['message'])

    @patch('utils.games_utils.games_defs.verify_id')
    def test_delete_game_success(self, mock_verify_id):
        mock_delete_one = self.mock_games_collection.delete_one

        mock_verify_id.return_value = True

        response = delete_game('66a3d3e92646ece2a8c4e49c')

        mock_delete_one.assert_called_once_with({'_id': ObjectId('66a3d3e92646ece2a8c4e49c')})

        self.assertEqual(response.status_code, 200)

    @patch('utils.games_utils.games_defs.verify_name')
    @patch('utils.games_utils.games_defs.verify_year')
    @patch('utils.games_utils.games_defs.verify_id')
    def test_put_games(self, mock_verify_id, mock_verify_year, mock_verify_name):
        mock_update = self.mock_games_collection.update_one

        mock_verify_year.return_value = True
        mock_verify_name.return_value = True
        mock_verify_id.return_value = True
    
        with self.app.test_request_context(json={"name": "Game 1", "year": 2021}):
            response = edit_game('66a3d3e92646ece2a8c4e49c')

            mock_update.assert_called_once_with({'_id': ObjectId('66a3d3e92646ece2a8c4e49c')}, {'$set': {'name': 'Game 1', 'year': 2021}})

            self.assertEqual(response.status_code, 200)
            self.assertIn('Game edited', response.get_json()['message'])


if __name__ == '__main__':
    unittest.main()