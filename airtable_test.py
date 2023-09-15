#! /usr/bin/env python

import requests as rq
import creds
from pyairtable import Api

air_api = Api(creds.api_key)
table = air_api.table('app9bUK7N5EIvUscS','tblUSwCsGaO3YiThH')
# print(table.all(fields = ['Name']))
for cust_name in table.all(fields=['Name']):
    print (cust_name['fields'])