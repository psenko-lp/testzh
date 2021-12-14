import hashlib
import hmac
import json
import sys
from base64 import b64decode, b64encode
from datetime import datetime
from typing import Any, Dict, Optional
from urllib.parse import urljoin
import argparse
import importlib

import requests
from logging import getLogger
from acc import acc

""" structure of acc.py (not included in source control):
acc = {
    'lp_dev1': {
        'API_PUBLIC_KEY' : '',
        'API_PRIVATE_KEY' : '',
        'PASSPHRASE' : ''
    },
    ...
}
"""

logger = getLogger(__name__)

URL_BASE = 'api.cert.zerohash.com'
HTTP_BASE = 'https://' + URL_BASE


def sign(api_key: str, method: str, route: str, json_body: str, timestamp: str) -> bytes:
    """Given a key and data, create and sign a payload.

    :param api_key: Key to sign the message with
    :param method: HTTP method
    :param route: Relative route. EX. /fills
    :param json_body: JSON as a string. Usually created via json.dumps(dict)
    :param timestamp: Unix Epoch time as a string
    :return: Base64 encoded digest
    """
    msg = bytes(timestamp + method + route + json_body, encoding='utf-8')
    hm = hmac.new(key=b64decode(api_key), msg=msg, digestmod=hashlib.sha256)
    return b64encode(hm.digest())


def headers() -> Dict[str, Any]:
    """Create a header template for use in HTTP requests."""
    return {
        'X-SCX-API-KEY': API_PUBLIC_KEY,
        'X-SCX-SIGNED': '',  # Put here to make sure we alway send something
        # The datetime.timestamp function is available only in Python 3.3+
        'X-SCX-TIMESTAMP': str(int(datetime.now().timestamp())),  # Unix Epoch
        'X-SCX-PASSPHRASE': PASSPHRASE
    }


def make_seed_request(method: str, url: str, body: Optional[Dict[str, str]] = None) -> requests.Response:
    """Create and send an HTTP request with a signature to the Zero Hash API.

    :param method: HTTP method
    :param url: Relative route. EX. /fills
    :param body: Dictionary for serializing into the JSON body of the request. For GET requests,
                 this can be omitted or set to an empty dict. Nothing will be sent, but it is
                 required for the signature.
    :return: requests.Response object
    """
    if body is None:
        body = {}
    h = headers()
    json_body = json.dumps(body, separators=(',', ':'))
    h['X-SCX-SIGNED'] = sign(API_PRIVATE_KEY, method, url, json_body, h['X-SCX-TIMESTAMP'])
    args = {'method': method, 'url': urljoin(HTTP_BASE, url)}
    logger.info('Making {} request to {}'.format(method, urljoin(URL_BASE, url)))
    if body:
        args['data'] = json_body
        h['Content-Type'] = 'application/json'
        logger.debug(json_body)
    args['headers'] = h

    # Since we don't know if it's a GET or POST, use the generic request function and create an
    # args dict so that we can conditionally pass data/JSON
    return requests.request(**args)

def load_args(argv):
    print("Loading arguments")
    global account, testcase, printout
    options = get_options(argv)

    if options.account is not None:
        account = options.account
        print(f"Account name: {account}")
    
    if options.testcase is not None:
        testcase = options.testcase
        print(f"Account name: {testcase}")

    if options.printout is not None:
        printout = options.printout
        print(f"Account name: {printout}")


def get_options(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-a", "--account", help="Account")
    parser.add_argument("-t", "--testcase", help="Test case")
    parser.add_argument("-p", "--printout", help="Print output")
    options = parser.parse_args(args)
    return options


def main(argv):
    global account, testcase, printout, API_PUBLIC_KEY, API_PRIVATE_KEY, PASSPHRASE
    load_args(argv)

    API_PUBLIC_KEY = acc[account]['API_PUBLIC_KEY']
    API_PRIVATE_KEY = acc[account]['API_PRIVATE_KEY']
    PASSPHRASE = acc[account]['PASSPHRASE']

    testmodule = importlib.import_module("testcases.%s" % testcase)
    method, url, body = testmodule.testcase()

    q = make_seed_request(method, url, body)
    if printout == 'json':
        print(q.json())
    else:
        print(q.status_code)
    

if __name__ == "__main__":
    main(sys.argv[1:])