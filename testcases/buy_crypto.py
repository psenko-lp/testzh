def testcase(mode = '', result = {}):
    if mode == 'verify':
        pass # returns True if result as expected
    elif mode == 'POST':
        return 'POST', '/liquidity/execute', {"quote_id": result['quote_id']}
    else:
        return 'GET', '/liquidity/rfq/?side=buy&underlying=BTC&quoted_currency=USD&total=100&participant_code=YA7KWJ', {}


"""

psenko@psenko-mbp testing % python3 z.py -a lp_dev3 -t buy_crypto -p json
Loading arguments
Account name: lp_dev3
Testcase name: buy_crypto
Printout format: json
{'message': {'request_id': '1141ccfc-9df0-48a1-8a51-d63d8f743d47', 'participant_code': 'YA7KWJ', 'quoted_currency': 'USD', 'side': 'buy', 'quantity': '0.00202237', 'price': '49446.9360206094829334', 'quote_id': '07858891-1f5e-425f-8d70-65ccc1487c77', 'expire_ts': 1639615889657, 'account_group': '00SCXM', 'account_label': 'general', 'underlying': 'BTC'}}
{'message': {'request_id': '5eb35747-7864-43a9-81b5-be25549bf015', 'quote': {'request_id': '1141ccfc-9df0-48a1-8a51-d63d8f743d47', 'participant_code': 'YA7KWJ', 'quoted_currency': 'USD', 'side': 'buy', 'quantity': '0.00202237', 'price': '49446.9360206094829334', 'quote_id': '07858891-1f5e-425f-8d70-65ccc1487c77', 'expire_ts': 1639615889657, 'account_group': '00SCXM', 'account_label': 'general', 'underlying': 'BTC', 'transaction_timestamp': 1639615885110.143}, 'trade_id': '9187faa1-8e6f-4618-9bd0-2baef6f0fa50', 'status': 'Completed', 'trade_ids_list': ['9187faa1-8e6f-4618-9bd0-2baef6f0fa50', '11db9a5b-3849-4d78-ad0c-5caaa3f28d71']}}

second trade: https://portal.cert.zerohash.com/YA7KWJ/trades/11db9a5b-3849-4d78-ad0c-5caaa3f28d71

NameBella Loves
Participant Code: YA7KWJ
Settlement State: obligations_outstanding
Asset Receiving: BTC
Side: buy
Amount Receiving: null
Trading Account: N/A
Obligations Outstanding: Dec 15, 2021, 04:52:01 PM PST
Settling: false

What does it mean?


After adding participant code for new user (BCO0WB)

psenko@psenko-mbp testing % python3 z.py -a lp_dev3 -t buy_crypto -p json      
Loading arguments
Account name: lp_dev3
Testcase name: buy_crypto
Printout format: json
{'message': {'request_id': '0736daa8-add6-4df8-a25b-2d9f2cbc1711', 'participant_code': 'YA7KWJ', 'quoted_currency': 'USD', 'side': 'buy', 'quantity': '0.0020327', 'price': '49195.6511044423672947', 'quote_id': '7c95eac9-7b08-4194-bbb7-bae1a55d6894', 'expire_ts': 1639618420250, 'account_group': '00SCXM', 'account_label': 'general', 'obo_participant': {'participant_code': 'BCO0WB', 'account_group': 'YA7KWJ', 'account_label': 'general'}, 'underlying': 'BTC'}}
{'message': {'request_id': '85ce5981-aec8-49ed-998e-df830ae846d5', 'quote': {'request_id': '0736daa8-add6-4df8-a25b-2d9f2cbc1711', 'participant_code': 'YA7KWJ', 'quoted_currency': 'USD', 'side': 'buy', 'quantity': '0.0020327', 'price': '49195.6511044423672947', 'quote_id': '7c95eac9-7b08-4194-bbb7-bae1a55d6894', 'expire_ts': 1639618420250, 'account_group': '00SCXM', 'account_label': 'general', 'obo_participant': {'participant_code': 'BCO0WB', 'account_group': 'YA7KWJ', 'account_label': 'general'}, 'underlying': 'BTC', 'transaction_timestamp': 1639618415701.434}, 'trade_id': 'e99d9b65-712d-49ea-816c-d34bc104b173', 'status': 'Completed', 'trade_ids_list': ['e99d9b65-712d-49ea-816c-d34bc104b173', '9f030df4-515e-4f4a-a9bb-9c4dc4bd5d11']}}

"""