import unittest
from unittest.mock import patch, MagicMock
from server import handle_client
from routing_table import RoutingTable

class TestServer(unittest.TestCase):

    def setUp(self):
        self.routing_table = RoutingTable()
        self.clients = {}

    @patch('socket.socket')
    def test_register_user(self, mock_socket):
        mock_socket.recv = MagicMock(return_value='REGISTER Alice'.encode('utf-8'))
        handle_client(mock_socket)

        self.assertEqual(self.routing_table.get_name_by_id(1), 'Alice')
        mock_socket.send.assert_called_with(b'REGISTERED 1')

    @patch('socket.socket')
    def test_message_delivery(self, mock_socket):
        # Регистрация двух пользователей
        self.routing_table.add_user(1, 'Alice')
        self.clients[1] = mock_socket

        mock_socket.recv = MagicMock(return_value='MESSAGE Alice Hello'.encode('utf-8'))
        handle_client(mock_socket)

        mock_socket.send.assert_called_with(b'DELIVERED')

    @patch('socket.socket')
    def test_user_not_found(self, mock_socket):
        mock_socket.recv = MagicMock(return_value='MESSAGE Bob Hello'.encode('utf-8'))
        handle_client(mock_socket)

        mock_socket.send.assert_called_with(b'USER_NOT_FOUND')

if __name__ == '__main__':
    unittest.main()