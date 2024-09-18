import unittest
from unittest.mock import patch, MagicMock
from client import send_message

class TestClient(unittest.TestCase):

    @patch('socket.socket')
    def test_registration(self, mock_socket):
        mock_socket.recv = MagicMock(return_value='REGISTERED 1'.encode('utf-8'))
        send_message(mock_socket, 'REGISTER Alice')
        mock_socket.send.assert_called_with(b'REGISTER Alice')

    @patch('socket.socket')
    def test_message_send(self, mock_socket):
        mock_socket.recv = MagicMock(return_value='DELIVERED'.encode('utf-8'))
        send_message(mock_socket, 'MESSAGE Bob Hello')
        mock_socket.send.assert_called_with(b'MESSAGE Bob Hello')

if __name__ == '__main__':
    unittest.main()