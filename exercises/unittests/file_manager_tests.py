import unittest
from unittest.mock import patch, mock_open
from file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.txt'
        self.file_manager = FileManager(self.file_path)

    @patch('builtins.open', new_callable=mock_open, read_data='Hello, World!')
    def test_read_file(self, mock_file):
        content = self.file_manager.read_file()
        mock_file.assert_called_once_with(self.file_path, 'r')
        self.assertEqual(content, 'Hello, World!')

    @patch('builtins.open', new_callable=mock_open)
    def test_write_file(self, mock_file):
        content_to_write = 'Hello, World!'
        bytes_written = self.file_manager.write_file(content_to_write)
        mock_file.assert_called_once_with(self.file_path, mode='w')
        mock_file().write.assert_called_once_with(content_to_write)
        self.assertEqual(bytes_written, len(content_to_write))

