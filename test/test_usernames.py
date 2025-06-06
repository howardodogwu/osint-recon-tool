import unittest
from modules.usernames import check_usernames

class TestUsernameModule(unittest.TestCase):
    def test_existing_username(self):
        result = check_usernames("github")
        self.assertTrue(result["GitHub"]["exists"], "GitHub username should exist")

    def test_non_existing_username(self):
        result = check_usernames("nonexistent_user_xyz")
        self.assertFalse(result["Twitter"]["exists"], "Twitter username should not exist")

if __name__ == "__main__":
    unittest.main()
