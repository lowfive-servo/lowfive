import cgi
import cgitb
import configparser
import json
import urllib.request

def parse_payload(payload):
	return str(payload["target_url"].split('/')[-1])


def get_log(api, log_id):
	pass


if __name__ == "__main__":
	print("Content-Type: text/html;charset=utf-8")
	print()
	cgitb.enable()

	config = configparser.RawConfigParser()
	config.read('config')
	github_username = config['github']['username']
	github_token = config['github']['token']

	travis_url = 'https://api.travis-ci.org'
	headers = {
		"User-Agent": "LowFive:1.0.0",
		"Accept": "application/vnd.travis-ci.2+json",
		"Host": "api.travis-ci.org"
	}

	req = urllib.request.Request(travis_url, headers=headers)

	with urllib.request.urlopen(req) as f:
		print(f.read())