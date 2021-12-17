def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    else:
        method = 'GET'
        url = '/trades/' + 'e61dd98e-cc4d-416a-b08e-8fa4a7a47006'
        body = {}
        return method, url, body