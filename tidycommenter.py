import cgi
import cgitb
import configparser
import json
import urllib.request

class TravisAPIProvider:
	user_agent = 'LowFive:1.0.0'
	accept = 'application/vnd.travis-ci.2+json'
	host = 'https://api.travis-ci.org'
	log_url = host + '/jobs/{job_id}/logs'
	token_url = host + '/auth/github'

	def __init__(self, gh_token):
		self.token = self.get_token(gh_token)
		headers = {
		"User-Agent": "LowFive:1.0.0",
		"Accept": "application/vnd.travis-ci.2+json",
		"Host": "api.travis-ci.org"
	}

	def get_token(self, gh_token):
		data = {"github_token":gh_token}

		data = bytes(json.dumps(data), 'utf-8').replace(b' ', b'')
		print(data)
		print(len(data))

		req = urllib.request.Request(self.token_url, data=data)
		req.add_header("User-Agent", self.user_agent)
		req.add_header("Accept", self.accept)
		req.add_header("Host", self.host)
		req.add_header("Content-Type", "application/json;charset=utf-8")
		req.add_header("Content-Length", len(data))

		with urllib.request.urlopen(req) as res:
			raw_response = res.read()

		return json.loads(raw_response)

	def get_token(self, gh_token):
		data = {
		  "scopes": [
		    "read:org", "user:email", "repo_deployment",
		    "repo:status", "write:repo_hook"
		  ],
		  "note": "temporary token to auth against travis"
		}

		data = bytes(json.dumps(data), 'utf-8')

		req = urllib.request.Request("https://api.github.com/authorizations", data=data)
		req.add_header("Host", 'api.github.com')
		req.add_header("Content-Type", "application/json")

		with urllib.request.urlopen(req) as res:
			raw_response = res.read()

		return json.loads(raw_response)

	def get_log():
		raise NotImplementedError

def parse_payload(payload):
	"""gets job id from payload"""
	return str(payload["target_url"].split('/')[-1])

def handle_payload(payload):
	travis_job_id = parse_payload(payload)

if __name__ == "__main__":
	print("Content-Type: text/html;charset=utf-8")
	print()
	cgitb.enable()

	config = configparser.RawConfigParser()
	config.read('config')
	github_username = config['github']['username']
	github_token = config['github']['token']

	info = cgi.FieldStorage()
	payload_raw = info.getfirst('payload', '')
	payload = json.loads(payload_raw)

	handle_payload(payload)