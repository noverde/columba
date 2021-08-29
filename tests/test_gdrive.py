import unittest
from unittest.mock import patch

import gdrive


class TestGoogleDrive(unittest.TestCase):
    @patch("google.colab.drive.mount")
    def test_gdrive_mount(self, mock_params):
        gdrive.mount()
