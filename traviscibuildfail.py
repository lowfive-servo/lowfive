import cgi
import cgitb
import ConfigParser
import github3
import json
import travispy
import urllib
import re

def get_build_info(payload):
    """
    Expected Input:
    {
        ...,
        target_url : "target_url": "https://travis-ci.org/servo/servo/builds/<build_id>,
        ...
    }
    """
    return int(payload["target_url"].split("/")[-1])

def get_log(job_id):
    return urllib.urlopen('https://s3.amazonaws.com/archive.travis-ci.org/jobs/%s/log.txt' % job_id).read()

def parse_errors_from_log(log):
    return re.findall("\\033\[94m(?P<file>.+?)\\033\[0m:\\033\[93m(?P<line_num>.+?)\\033\[0m:\s\\033\[91m(?P<comment>.+?)\\033\[0m", log)

def post_comments_on_errors(errors):
    pass

def post_comments_on_error(error):
    pass

def handle_payload(payload, username, token):
    build_id = get_build_info_from_json(payload)

    t = travispy.travispy.TravisPy()
    job_id = t.build(build_id).job_ids[0] 
    log = get_log(job_id)
    errors = parse_errors_from_log(log)

if __name__ == "__main__":
    #Set up for CGI
    # print "Content-Type: text/html;charset=utf-8"
    # print

    # cgitb.enable()

    #Setup 
    config = ConfigParser.RawConfigParser()
    config.read('config/config.ini')
    username = config.get('github', 'username')
    token = config.get('github', 'token')

    # post = cgi.FieldStorage()
    # payload_raw = post.getfirst('payload','')
    # payload = json.loads(payload_raw)

    payload = json.loads(open('test/test-data.json').read())

    # entry point into application
    handle_payload(payload, username, token)