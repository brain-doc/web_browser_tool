
import unittest
from browse_internet import browse_internet

class TestBrowseInternet(unittest.TestCase):

    def test_valid_url(self):
        url = "http://example.com"
        content = browse_internet(url)
        self.assertIn("<title>Example Domain</title>", content)

    def test_invalid_url(self):
        url = "http://invalidurl"
        content = browse_internet(url)
        self.assertIn("Failed to resolve", content)

    def test_non_existent_page(self):
        url = "http://example.com/nonexistentpage"
        content = browse_internet(url)
        self.assertIn("404", content)

if __name__ == "__main__":
    unittest.main()
