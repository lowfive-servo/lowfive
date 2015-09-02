import json
import unittest
from tidycommenter import parse_payload

class TestJSONParse(unittest.TestCase):
	def setUp(self):
		with open("test-data.json") as f:
			self.payload = json.load(f)

	def test_parse_payload(self):
		self.assertEqual("74856035", parse_payload(self.payload))

if __name__ == '__main__':
	unittest.main()