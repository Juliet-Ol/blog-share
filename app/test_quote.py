
import unittest
from .models import Quote

Quote = Quote.quote

class QuoteTest(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quote("id","content","timestamp","user_id")

    def test_init(self):
        self.assertEqual(self.new_quote,"id")
        self.assertEqual(self.new_quote,"username")
        self.assertEqual(self.new_quote,"email")
        self.assertEqual(self.new_quote,"password")


if __name__=='__main':
    unittest.main()
