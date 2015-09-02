import configparser
import json
import unittest
from tidycommenter import parse_payload, TravisAPIProvider

class TestJSONParse(unittest.TestCase):
	def setUp(self):
		with open("test-data.json") as f:
			self.payload = json.load(f)

	def test_parse_payload(self):
		self.assertEqual("74856035", parse_payload(self.payload))

class TestTravisIntegration(unittest.TestCase):
	def setUp(self):
		config = configparser.RawConfigParser()
		config.read('config')
		github_token = config['github']['token']
		self.travis_api = TravisAPIProvider(github_token)

	def test_something_here(self):
		print(self.travis_api.get_token())

if __name__ == '__main__':
	unittest.main()