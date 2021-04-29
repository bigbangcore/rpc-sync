#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import pymysql
import time, datetime
from decimal import Decimal
import sys
import os

url="http://127.0.0.1:9902"
data = {
    "id":1,
    "method":"createtransaction",
    "jsonrpc":"2.0",
    "params":{
        "from":"1965p604xzdrffvg90ax9bk0q3xyqn5zz2vc9zpbe3wdswzazj7d144mm",
        "to":"1965p604xzdrffvg90ax9bk0q3xyqn5zz2vc9zpbe3wdswzazj7d144mm",
        "amount":1000000,
        "txfee":1000000,
        "inputs":"5de140807b1160347b1a303ec004625116901df66d2220fb3ff6a1ea0019836b0",
        "ts":1234567,
        "fork":"0000000006854ebdc236f48dbbe5c87312ea0abd7398888374b5ee9a5eb1d291",
        "data":""
        }
    }
response = requests.post(url, json=data)
print(json.loads(response.text))