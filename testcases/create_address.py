def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    else:
        body = {
            "participant_code": "YA7KWJ",
            "asset": "LTC",
        }
        return 'POST', '/deposits/digital_asset_addresses', body


"""
ISSUE (ETH, SOL, DAI, LTC):

psenko@psenko-mbp testing % python3 z.py -a lp_dev3 -t create_address -p json
Loading arguments
Account name: lp_dev3
Testcase name: create_address
Printout format: json
{'message': {}}

"""