def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    else:
        return 'GET', '/liquidity/rfq/?side=buy&underlying=BTC&quoted_currency=USD&quantity=1', {}