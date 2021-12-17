def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    else:
        return 'GET', '/accounts/?account_owner=BCO0WB', {}