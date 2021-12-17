def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    else:
        method = 'POST'
        url = '/trades'
        body = {}
        return method, url, body