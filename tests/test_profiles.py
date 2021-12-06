import os
import unittest

from columba import profiles
from unittest.mock import patch


BASE_PATH_MOCK = "/tmp"

AWS_ACCESS_KEY_ID = "1234"
AWS_SECRET_ACCESS_KEY = "xyzabc"
AWS_DEFAULT_REGION = "us-east-1"


class TestProfilesLoad(unittest.TestCase):
    def setUp(self) -> None:
        self.profile_name = "columba-unity-test"
        self.profile_path = os.path.join(BASE_PATH_MOCK, self.profile_name)

        with open(self.profile_path, "w") as f:
            f.write(f"AWS_ACCESS_KEY_ID={AWS_ACCESS_KEY_ID}\n")
            f.write(f"AWS_SECRET_ACCESS_KEY={AWS_SECRET_ACCESS_KEY}\n")
            f.write(f"AWS_DEFAULT_REGION={AWS_DEFAULT_REGION}\n")

    def tearDown(self) -> None:
        os.remove(self.profile_path)

    @patch("columba.profiles.BASE_PATH", BASE_PATH_MOCK)
    @patch("google.colab.drive.mount")
    def test_load_success(self, m_mount):
        profiles.load(self.profile_name)

        self.assertEqual(m_mount.call_count, 1)
        self.assertEqual(os.environ["AWS_ACCESS_KEY_ID"], AWS_ACCESS_KEY_ID)
        self.assertEqual(os.environ["AWS_SECRET_ACCESS_KEY"], AWS_SECRET_ACCESS_KEY)
        self.assertEqual(os.environ["AWS_DEFAULT_REGION"], AWS_DEFAULT_REGION)

    @patch("columba.profiles.BASE_PATH", BASE_PATH_MOCK)
    @patch("google.colab.drive.mount")
    def test_load_fail(self, m_mount):
        unexisting_profile = "unexisting"

        with self.assertRaises(profiles.ProfileNotFound) as ctx:
            profiles.load(unexisting_profile)

        self.assertIn(unexisting_profile, str(ctx.exception))
        self.assertEqual(m_mount.call_count, 1)
