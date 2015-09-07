import unittest
import json
import travispy
import traviscibuildfail as mod

78841971

class TestTravisCIBuildFail(unittest.TestCase):
	def setUp(self):
		self.build_id = 74856035
		self.travis = travispy.travispy.TravisPy()

	def test_get_build_info(self):
		incoming_data = json.loads(open('test-files/test-data.json').read())

		self.assertEqual(mod.get_build_info(incoming_data), self.build_id)

	def test_get_log(self):
		job_id = self.travis.build(self.build_id).job_ids[0] 
		test_log = open('test-files/test_log.txt').read()

		self.assertIsInstance(mod.get_log(job_id), str)

	def test_parse_errors_from_log(self):
		job_id = self.travis.build(self.build_id).job_ids[0] 
		log = mod.get_log(job_id)
		errors = [('components/devtools/actor.rs', '201', '(much) overlong line')]

		self.assertEqual(mod.parse_errors_from_log(log), errors)


if __name__ == '__main__':
	unittest.main()