def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    else:
        body = {
            "first_name": "Peter",
            "last_name": "Smith III",
            "email": "email-example1@mail.com",
            "address_one": "1 Main St.",
            "address_two": "Suite 1000",
            "city": "Chicago",
            "state": "IL",
            "zip": "12345",
            "country": "United States",
            "date_of_birth": "1985-09-02",
            "id_number_type": "ssn",
            "id_number": "123456789",
            "signed_timestamp": 1603378501286,
            "metadata": {}
        }
        return 'POST', '/participants/customers/new', body