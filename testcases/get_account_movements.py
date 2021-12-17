def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    else:
        return 'GET', '/accounts/' + '45d05a72-6c97-433c-8094-05111d8826a8' + '/movements', {}